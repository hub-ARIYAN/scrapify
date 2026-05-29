import os
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from .vectorstore import get_vectorstore


def build_qa_chain():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    llm = ChatOpenAI(temperature=0)
    return RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)


def answer_question(question: str) -> str:
    qa = build_qa_chain()
    return qa.run(question)
