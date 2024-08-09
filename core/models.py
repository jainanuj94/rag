from langchain_mistralai import ChatMistralAI
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model="llama3.1")

llm = ChatMistralAI(model="mistral-large-latest")
