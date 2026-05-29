import os
from langchain.vectorstores import Chroma
from .chunker import get_embeddings

PERSIST_DIR = os.path.join(os.path.dirname(__file__), "db")


def get_vectorstore():
    embeddings = get_embeddings()
    return Chroma(
        collection_name="web_pages",
        embedding_function=embeddings,
        persist_directory=PERSIST_DIR,
    )


def upsert_texts(texts, metadatas, ids=None):
    vectorstore = get_vectorstore()
    vectorstore.add_texts(texts=texts, metadatas=metadatas, ids=ids)
    vectorstore.persist()
    return vectorstore
