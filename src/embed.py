import json
import ollama
import numpy as np

def embed_text(text: str):
    return ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )["embedding"]

if __name__ == "__main__":
    with open("data/chunks.json") as f:
        chunks = json.load(f)

    embeddings = []
    for chunk in chunks:
        embeddings.append(embed_text(chunk["text"]))

    embeddings = np.array(embeddings).astype("float32")

    np.save("data/embeddings.npy", embeddings)
