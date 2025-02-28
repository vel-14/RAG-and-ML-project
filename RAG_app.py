import streamlit as st
import fitz
import pdfplumber
from io import BytesIO
from PIL import Image
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variable
load_dotenv()

# Configure Goggle API with the API key from environment variable
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text = ""
    images = []
    tables = []

    for pdf in pdf_docs:
        # Extract text and images using PyMuPDF
        document = fitz.open(stream=pdf.read(), filetype="pdf")
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text += page.get_text()

            for img in page.get_images(full=True):
                xref = img[0]
                base_image = document.extract_image(xref)
                image_bytes = base_image["image"]
                images.append(Image.open(BytesIO(image_bytes)))

        # Extract tables using pdfplumber
        pdf.seek(0)  # Reset the pointer to beginning of the file
        with pdfplumber.open(BytesIO(pdf.read())) as pdf_file:
            for page in pdf_file.pages:
                extracted_tables = page.extract_tables()
                tables.extend(extracted_tables)

    return text, images, tables

def get_text_chunks(text):
    # Split the text into chunks for processing
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    # Create an embedding model and build a FAISS vector store from text chunks
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    # Save the vector store locally
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    # Prompt template for answering questions based on the context
    prompt_template = """
    Answer the question as detailed as possible from the provided context. Make sure to provide all the details. If the answer is not in
    the provided context, just say, 'Answer is not available in the context.' Don't provide the wrong answer.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """

    # Chat model and prompt template for the QA chain
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    # Load the FAISS vector store and perform a similarity search
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)

    st.write("Reply: ", response)

def main():
    # Set up the Streamlit app configuration and layout
    st.set_page_config(page_title="Chat PDF")
    st.header("Chat with PDF using Gemini💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    # Process the uploaded PDF files
                    raw_text, images, tables = get_pdf_text(pdf_docs)
                    text_chunks = get_text_chunks(raw_text)
                    get_vector_store(text_chunks)
                    st.success("Done")
            else:
                st.warning("Please upload at least one PDF file.")

if __name__ == "__main__":
    main()
