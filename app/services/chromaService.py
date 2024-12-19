import chromadb

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("dreams_db")


def get_dreams_docs(query:str):
    results = collection.query(
    query_texts=["que es un simbolo?"],
    n_results=4
)
    
    result = [f"- {doc}" for sublist in results['documents'] for doc in sublist]
    relevant_documents = "\n\n".join(result)
    return relevant_documents

