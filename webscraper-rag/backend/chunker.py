import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings

try:
    from langchain.embeddings.groq import GroqEmbeddings
except ImportError:  # type: ignore
    GroqEmbeddings = None  # type: ignore


def get_embeddings():
    """Return the configured embeddings provider."""
    if os.getenv("USE_GROQ", "false").lower() == "true" and GroqEmbeddings is not None:
        return GroqEmbeddings()
    return OpenAIEmbeddings()


def split_text(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_text(text)
