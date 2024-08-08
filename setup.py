# setup.py
from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "langchain-ollama",
        "ollama",
        "chromadb",
        "sentence-transformers",
        "python-magic",
        "langchain_community",
        "langchain_chroma",
        "unstructured",
        "unstructured[md]",
        "pandas"
    ],
)
