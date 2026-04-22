from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # ---- STEP 1: STRICT MATCH (best accuracy) ----
    matches = re.findall(r'([A-Z][a-z]+)\s+scored\s+(\d+)', query)

    if matches:
        winner = max(matches, key=lambda x: int(x[1]))[0]
        return {"output": winner}

    # ---- STEP 2: FALLBACK (robust handling) ----
    words = query.split()

    pairs = []
    current_name = None

    for word in words:
        # detect name
        if word.istitle():
            current_name = word

        # detect number
        if word.isdigit() and current_name:
            pairs.append((current_name, int(word)))
            current_name = None

    if pairs:
        winner = max(pairs, key=lambda x: x[1])[0]
        return {"output": winner}

    # ---- STEP 3: FINAL SAFETY ----
    return {"output": ""}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
