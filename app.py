import streamlit as st
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import SeleniumURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()

# Set Page Configurations
st.set_page_config(
    page_title="Article Research Tool",
    page_icon="📚",
    layout="centered",  # Centered layout for better visibility
)

# Add Background Image
st.markdown(
    """
    <style>
    .reportview-container {
        background: url('https://source.unsplash.com/random/1600x900/?books,library,study') no-repeat center center;
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
background_image = "https://source.unsplash.com/random/1600x900/?books,library,study"
st.image(background_image, use_column_width=True)
# Title
st.title("Article Research Tool 📈")

# Create Tabs for URLs and Question
tabs = st.sidebar.radio("Select Option", ["Input URLs", "Ask a Question"])

if tabs == "Input URLs":
    st.markdown(
        "<h2 style='text-align: center; color: white;'>Input URLs</h2>",
        unsafe_allow_html=True,
    )
    urls = []
    for i in range(3):
        url = st.text_input(f"URL {i+1}", "")
        urls.append(url)

    process_url_clicked = st.button("Process URLs", key="process_url")

    if process_url_clicked:
        loader = SeleniumURLLoader(urls=urls)
        st.text("Data Loading...Started...✅✅✅")
        data = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(
            separators=["\n\n", "\n", ".", ","], chunk_size=1000
        )
        st.text("Text Splitter...Started...✅✅✅")
        docs = text_splitter.split_documents(data)
        st.text("Embedding Vector Updated...✅✅✅")

elif tabs == "Ask a Question":
    st.markdown(
        "<h2 style='text-align: center; color: white;'>Ask a Question</h2>",
        unsafe_allow_html=True,
    )
    query = st.text_input("Question: ", "")

    if query:
        st.text("Processing...🔄")
        embeddings = OpenAIEmbeddings()
        llm = OpenAI(temperature=0.9, max_tokens=500)
        model = FAISS.load_local(
            "S_MODEL", embeddings, allow_dangerous_deserialization=True
        )
        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm, retriever=model.as_retriever()
        )
        result = chain({"question": query}, return_only_outputs=True)
        st.header("Answer")
        st.write(result["answer"])

        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")
            for source in sources_list:
                st.write(source)
