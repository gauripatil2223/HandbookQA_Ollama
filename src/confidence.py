def compute_confidence(scored_chunks):
    if not scored_chunks:
        return 0.0

    scores = [item["score"] for item in scored_chunks]
    s1 = scores[0]
    s2 = scores[1] if len(scores) > 1 else 0.0

    # Normalize similarity into confidence
    base = max(0.0, min(1.0, (s1 - 0.3) / 0.7))

    # Concentration factor
    concentration = min(1.0, s1 / (s2 + 1e-6)) if s2 > 0 else 1.0

    confidence = base * concentration
    return round(confidence, 2)
