# Chat with PDF Using Gemini

This project is a web application that allows users to interact with PDF files through a chat interface. It uses Tesseract OCR to extract text from PDFs, processes this text, and provides a conversational AI model to answer questions about the content of the PDFs.

## Features

- **Upload PDF Files**: Allows users to upload multiple PDF files.
- **Text Extraction**: Extracts text, images, and tables from the uploaded PDFs.
- **Text Chunking**: Splits extracted text into manageable chunks.
- **Vector Store**: Stores text chunks in a FAISS vector store for efficient similarity searches.
- **Conversational AI**: Uses a generative AI model to answer questions based on the content of the PDFs.

## Requirements

- **Python 3.9+**
- **Pip** (Python package manager)

## Installation

Follow these steps to set up and run the application:

1. **Clone the Repository**

    ```sh
    git clone https://github.com/vel-14/RAG-and-ML-project.git
    cd your-repository
    ```

2. **Create a Virtual Environment**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    Install the required Python packages using `pip`:

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**

    Create a `.env` file in the root directory of the project with the following content:

    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    ```

    Replace `your_google_api_key_here` with your actual Google API key. 

5. **Run the Application**

    Start the Streamlit application by running:

    ```sh
    streamlit run app.py
    ```

    The application will be available at `http://localhost:8501`.

## Usage

1. **Open the Application**

    Go to the URL provided by Streamlit (usually `http://localhost:8501`).

2. **Upload PDF Files**

    Use the sidebar to upload PDF files. You can upload multiple files at once.

3. **Process PDFs**

    Click the "Submit & Process" button after uploading the PDF files. The application will process the files and extract text, images, and tables.

4. **Ask Questions**

    Once the processing is complete, you can type your questions into the input box. The application will use the conversational AI model to answer your questions based on the content of the PDFs.

## Code Explanation

- **Imports and Configuration**: The necessary libraries are imported, and environment variables are loaded using `dotenv`.

- **PDF Processing**:
  - `get_pdf_text(pdf_docs)`: Extracts text, images, and tables from the provided PDFs.
  
- **Text Chunking**:
  - `get_text_chunks(text)`: Splits the extracted text into chunks for processing.

- **Vector Store**:
  - `get_vector_store(text_chunks)`: Creates and saves a FAISS vector store from the text chunks.

- **Conversational Chain**:
  - `get_conversational_chain()`: Defines and sets up the conversational AI model and prompt template.

- **User Input Handling**:
  - `user_input(user_question)`: Handles user questions by performing a similarity search and generating a response using the conversational chain.

- **Main Function**:
  - `main()`: Configures the Streamlit app, handles user interactions, and coordinates the PDF processing and question answering.


