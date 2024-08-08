# scripts/ask_question.py

import sys

sys.path.append('.')  # Add the parent directory to the Python path

from core.vector_store import rag_chain


def ask_question(qa, question):
    result = qa.invoke({"input": question})

    # print(f"{result}")
    print(f"Question: {question}")
    print(f"Answer: {result['answer']}")
    print("\nSources:")
    for doc in result['context']:
        print(f"- {doc.metadata['source']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:])
        ask_question(rag_chain, question)
    else:
        print("Please provide a question as a command-line argument.")
        print("Usage: python scripts/ask_question.py 'Your question here'")
