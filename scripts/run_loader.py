import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loader.document_loader import loadFromDirectory
from core.vector_store import vectorstore

def main():
    print("Starting the data loading process...")
    # vectorstore.delete_collection()
    print(f"Deleting {vectorstore._collection.count()} documents")
    vectorstore.reset_collection()
    print("Loading from directory.")
    loadFromDirectory()
    print(f"Inserted {vectorstore._collection.count()} documents")
    print("Loading from web.")
    # loadDocuments()
    # print("Loaded embeddings.")

    print("Data loading process completed.")

if __name__ == "__main__":
    main()