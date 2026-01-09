import faiss
import numpy as np

embeddings = np.load("data/embeddings.npy")

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)  # inner product
faiss.normalize_L2(embeddings)

index.add(embeddings)
faiss.write_index(index, "data/faiss.index")

print(f"FAISS index built with {index.ntotal} vectors")
