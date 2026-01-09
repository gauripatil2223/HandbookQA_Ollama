import ollama
from retrieve import retrieve
from answer import answer_question
from confidence import compute_confidence

def embed_query(text):
    return ollama.embeddings(
        model="nomic-embed-text",
        prompt=text
    )["embedding"]

if __name__ == "__main__":
    print("📘 Company Handbook Assistant")
    print("Ask a question about company policies, leave, remote work, or working hours.")
    print("Type 'exit' or 'quit' to leave.\n")

    while True:
         question = input(" Question: ").strip()

         if not question:
            print("Please enter a question.\n")
            continue

         if question.lower() in {"exit", "quit"}:
            print("\n Goodbye!")
            break
    

         q_embedding = embed_query(question)
         scored_chunks = retrieve(q_embedding)

         confidence = compute_confidence(scored_chunks)

         result = answer_question(question, scored_chunks, confidence)
         print(result)
