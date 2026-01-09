import json

def chunk_handbook(text):
    sections = text.split("\n## ")
    chunks = []

    for i, section in enumerate(sections):
        lines = section.strip().split("\n")
        title = lines[0].strip()
        body = " ".join(lines[1:]).strip()

        if not body:
            continue

        chunks.append({
            "id": f"section_{i}",
            "text": body,
            "metadata": {
                "section": title
            }
        })

    return chunks


if __name__ == "__main__":
    with open("data/handbook.md") as f:
        handbook = f.read()

    chunks = chunk_handbook(handbook)

    with open("data/chunks.json", "w") as f:
        json.dump(chunks, f, indent=2)
