from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # Extract all names
    names = re.findall(r'[A-Z][a-z]+', query)

    # Extract all numbers
    scores = list(map(int, re.findall(r'\d+', query)))

    # Safety check
    if not names or not scores:
        return {"output": ""}

    # Match names with scores in order
    pairs = list(zip(names, scores))

    # Find max
    winner = max(pairs, key=lambda x: x[1])[0]

    return {
        "output": winner
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
