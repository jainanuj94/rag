from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document

from core.embedding import embeddings
from core.text_splitter import text_splitter
from core.vector_store import vectorstore


class CustomWebLoader(WebBaseLoader):
    def load(self):
        results = []
        for url in self.web_paths:
            response = requests.get(url)
            content = extract_main_content(response.text)
            metadata = {"source": url}
            results.append(Document(page_content=content, metadata=metadata))
        return results


def get_all_links(url, base_url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        full_url = urljoin(base_url, link['href'])
        if full_url.startswith(base_url) and full_url not in links:
            links.append(full_url)
    return links


def extract_main_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Find the main content area (adjust these selectors based on the website's structure)
    main_content = soup.find('main') or soup.find('div', class_='content') or soup.find('article')

    if main_content:
        # Extract text from paragraphs and headers within the main content
        content = ' '.join(
            [p.get_text(strip=True) for p in main_content.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'])])
    else:
        # Fallback to extracting all visible text if main content area is not found
        content = ' '.join(soup.stripped_strings)

    return content


def loadDocuments():
    base_url = "https://docs.conductor-oss.org/devguide/concepts/"
    start_url = "https://docs.conductor-oss.org/devguide/concepts/index.html"
    pd.DataFrame()
    loadFromLinks(base_url, embeddings, start_url, text_splitter)


def loadFromLinks(base_url, embeddings, start_url, text_splitter):
    # Get all links
    all_links = get_all_links(start_url, base_url)
    loaders = [CustomWebLoader(url) for url in all_links]
    # Load all documents
    all_documents = []
    for loader in loaders:
        documents = loader.load()
        all_documents.extend(documents)
    # Split the documents
    split_docs = text_splitter.split_documents(all_documents)
    # Create and persist the vector store
    vectorstore.add_documents(split_docs)
