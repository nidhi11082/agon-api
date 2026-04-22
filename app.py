from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # Extract (Name, Score) pairs
    matches = re.findall(r'([A-Z][a-z]+)\s+scored\s+(\d+)', query)

    # Find highest scorer
    max_score = -1
    winner = ""

    for name, score in matches:
        score = int(score)
        if score > max_score:
            max_score = score
            winner = name

    # 🚨 CRITICAL: return ONLY name (no extra text)
    return {
        "output": winner
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
