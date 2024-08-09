from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain_ollama.llms import OllamaLLM
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder, PromptTemplate

from core.embedding import embeddings

vectorstore = Chroma(embedding_function=embeddings, persist_directory="./chroma_db")
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

model = OllamaLLM(model="llama3.1")

llm = ChatMistralAI(model="mistral-large-latest")

retriever_tool = create_retriever_tool(
    retriever,
    "optimus_search",
    "Search for information about Optimus. For any questions about Optimus, you must use this tool!",
)

# combine_docs_chain = create_stuff_documents_chain(model, prompt)
# rag_chain = create_retrieval_chain(retriever)

tools = [retriever_tool]

# agent = create_tool_calling_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)