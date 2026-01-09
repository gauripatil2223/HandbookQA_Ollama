import faiss
import json
import numpy as np

index = faiss.read_index("data/faiss.index")

with open("data/chunks.json") as f:
    CHUNKS = json.load(f)

def retrieve(question_embedding, k=4):
    query = np.array([question_embedding]).astype("float32")
    faiss.normalize_L2(query)

    scores, indices = index.search(query, k)

    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue
        results.append({
            "chunk": CHUNKS[idx],
            "score": float(score)
        })

    return results

