from core.vector_store import vectorstore
from core.models import model
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from langchain_core.prompts import ChatPromptTemplate
from langchain.tools.retriever import create_retriever_tool

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

system_prompt = (
    """You are a helpful assistant. Help me find the answer based on the following context:
    {context}"""
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

combine_docs_chain = create_stuff_documents_chain(model, prompt)
rag_chain = create_retrieval_chain(retriever, combine_docs_chain)