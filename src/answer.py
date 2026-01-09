import ollama
from validate import validate_response

SYSTEM_PROMPT = """
You are a handbook question-answering assistant.

Rules:
- Use ONLY the provided handbook excerpts.
- Do NOT infer or guess
- If the answer is not explicitly present, say:
  "The handbook does not specify this."
- Respond ONLY in valid JSON with this format:

{
  "answer": string,
  "confidence": number between 0 and 1,
  "sources": [
    { "section": string }
  ]
}
"""

def answer_question(question, scored_chunks, confidence, max_retries=3):
    context = "\n".join(
        f"{i+1}. ({item['chunk']['metadata']['section']}) {item['chunk']['text']}"
        for i, item in enumerate(scored_chunks)
    )

    prompt = f"""
Question:
{question}

Handbook excerpts:
{context}

Confidence score to use: {confidence}
"""

    for _ in range(max_retries):
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        content = response["message"]["content"]
        parsed = validate_response(content)

        if parsed:
            parsed["confidence"] = confidence
            return parsed

    return {
        "answer": "The handbook does not specify this.",
        "confidence": 0.0,
        "sources": []
    }
