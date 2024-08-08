import logging

from langchain_community.document_loaders import DirectoryLoader

from core.text_splitter import text_splitter, markdown_splitter
from core.vector_store import vectorstore
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.documents import Document


logger = logging.getLogger(__name__)


def loadFromDirectory():
    text_loader_kwargs = {"autodetect_encoding": True, "mode": "elements"}
    loader = DirectoryLoader('/Users/jainanuj94/kli-repos/optimus-docs/docs',
                             glob="**/*.md",
                             loader_cls=UnstructuredMarkdownLoader,
                             loader_kwargs=text_loader_kwargs,
                             show_progress=True)
    # loader = UnstructuredMarkdownLoader('/Users/jainanuj94/kli-repos/optimus-docs/docs')
    documents = loader.load()

    splits = text_splitter.split_documents(documents)

    for split in splits:
        split.metadata = sanitize_metadata(split.metadata)

    vectorstore.add_documents(splits)


def sanitize_metadata(metadata):
    sanitized = {}
    for key, value in metadata.items():
        if key == 'eng' and isinstance(value, list):
            sanitized[key] = ' '.join(value)  # Join all elements into a single string
        elif isinstance(value, (str, int, float, bool)):
            sanitized[key] = value
        elif isinstance(value, list) and len(value) > 0:
            sanitized[key] = str(value[0])
        else:
            sanitized[key] = str(value)
    return sanitized

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
