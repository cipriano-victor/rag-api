from chromadb import PersistentClient

collection = PersistentClient(path="./db").get_or_create_collection("docs")

with open("k8s.txt", "r") as f:
    text = f.read()

collection.add(documents=[text], ids=["k8s"])
print("Embedding stored in Chroma")
