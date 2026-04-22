from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # STRICT pattern: Name scored Number
    matches = re.findall(r'([A-Z][a-z]+)\s+scored\s+(\d+)', query)

    # If no matches, return empty safely
    if not matches:
        return {"output": ""}

    # Find highest scorer
    winner = ""
    max_score = -1

    for name, score in matches:
        score = int(score)
        if score > max_score:
            max_score = score
            winner = name

    # RETURN EXACT FORMAT (CRITICAL)
    return {
        "output": winner
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
