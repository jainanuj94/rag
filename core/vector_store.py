import getpass
import os

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_anthropic import ChatAnthropic
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_mistralai import ChatMistralAI

from core.embedding import embeddings

os.environ["MISTRAL_API_KEY"] = getpass.getpass()

vectorstore = Chroma(embedding_function=embeddings, persist_directory="./chroma_db")
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

system_prompt = (
    """Based on below context give answer. If you dont know dont answer.

    Context:
    {context}
    """
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

model = OllamaLLM(model="codellama")

llm = ChatMistralAI(model="mistral-large-latest")

combine_docs_chain = create_stuff_documents_chain(model, prompt)
rag_chain = create_retrieval_chain(retriever, combine_docs_chain)