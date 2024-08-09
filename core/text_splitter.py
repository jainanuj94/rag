from langchain_text_splitters import (
    Language,
    RecursiveCharacterTextSplitter,
)
from langchain_text_splitters import MarkdownHeaderTextSplitter


# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=7500, chunk_overlap=150)
md_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN, chunk_size=7500, chunk_overlap=150
)

headers_to_split_on = [
    ("###", "Header 1"),
    ("####", "Header 2"),
    ("#####", "Header 3"),
]

# MD splits
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on, strip_headers=False
)
