from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # Extract names (capitalized words)
    names = re.findall(r'\b[A-Z][a-z]+\b', query)

    # Extract numbers
    numbers = list(map(int, re.findall(r'\d+', query)))

    # If mismatch, return safely
    if len(names) < 2 or len(numbers) < 2:
        return {"output": ""}

    # Pair names with numbers in order
    pairs = list(zip(names, numbers))

    # Get max scorer
    winner = max(pairs, key=lambda x: x[1])[0]

    return {
        "output": winner
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
