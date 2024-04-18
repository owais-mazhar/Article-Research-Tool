# Article Research Tool 📈

![Tool Preview](https://source.unsplash.com/random/1600x900/?books,library,study)

## Overview

The Article Research Tool is a web application designed to assist in article research by allowing users to input URLs for processing or ask questions to retrieve relevant information. It utilizes natural language processing techniques and retrievers to extract information from text data.

## Features

- **Input URLs:** Users can input URLs of articles or web pages to process the content.
- **Ask Questions:** Users can ask questions to retrieve relevant information from the processed text data.
- **Answer Retrieval:** The tool utilizes language models and retrievers to extract answers to user questions.
- **Source References:** Relevant sources used to generate the answers are displayed for reference.

## Getting Started

To get started with the Article Research Tool, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/owais-mazhar/article-research-tool.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

4. Access the application in your web browser:
   ```
   http://localhost:8501
   ```

## Usage

1. **Input URLs:**
   - Select the "Input URLs" option from the sidebar.
   - Enter the URLs of articles or web pages you want to process.
   - Click the "Process URLs" button to start processing.

2. **Ask a Question:**
   - Select the "Ask a Question" option from the sidebar.
   - Enter your question in the text input provided.
   - The tool will process the question and display the answer.

3. **View Sources:**
   - If relevant sources are found, they will be displayed below the answer for reference.

## Technology Stack

- **Streamlit:** Web application framework for building interactive web applications.
- **Langchain:** Natural language processing library for text processing tasks.
- **Selenium:** Web browser automation tool for web scraping and data extraction.
- **FAISS:** Library for efficient similarity search and clustering of dense vectors.
- **OpenAI:** Platform for accessing state-of-the-art natural language processing models.

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize the `README.md` template further to include any additional information or sections as needed. Let me know if you have any questions or need further assistance!
