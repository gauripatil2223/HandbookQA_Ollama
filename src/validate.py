import json

REQUIRED_KEYS = {"answer", "confidence", "sources"}

def validate_response(text: str):
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None

    if not REQUIRED_KEYS.issubset(data.keys()):
        return None

    if not isinstance(data["sources"], list):
        return None

    return data
