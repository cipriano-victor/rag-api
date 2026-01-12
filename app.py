from fastapi import FastAPI
from chromadb import PersistentClient
from ollama import Client
from os import getenv
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MODEL_NAME = getenv("MODEL_NAME", "tinyllama")
OLLAMA_HOST = getenv("OLLAMA_HOST", "http://host.docker.internal:11434")
logging.info(f"Using model: {MODEL_NAME}")
logging.info(f"Using host: {OLLAMA_HOST}")

app = FastAPI()
collection = PersistentClient(path="./db").get_or_create_collection("docs")
ollama_client = Client(host=OLLAMA_HOST)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/query")
def query(q: str):
    """Query the knowledge base."""
    logging.info(f"Query asked: {q}")
    results = collection.query(query_texts=[q], n_results=1)
    context = results["documents"][0][0] if results["documents"] else ""

    answer = ollama_client.generate(
        model=MODEL_NAME,
        prompt=f"Context:\n{context}\n\nQuestion: {q}\n\nAnswer clearly and concisely:"
    )

    return {"answer": answer["response"]}

@app.post("/add")
def add_knowledge(text: str):
    """Add new content to the knowledge base dynamically."""
    logging.info(f"Adding new content to knowledge base: {text} (id will be generated)")
    try:
        from uuid import uuid4

        doc_id = str(uuid4())        
        collection.add(documents=[text], ids=[doc_id])
        
        return {
            "status": "success",
            "message": "Content added to knowledge base",
            "id": doc_id
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }
