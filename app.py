from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    pairs = []

    # Pattern 1: "Alice scored 80"
    pairs += re.findall(r'([A-Z][a-z]+)\s+(?:scored|got|has)\s+(\d+)', query)

    # Pattern 2: "Alice 80"
    pairs += re.findall(r'([A-Z][a-z]+)\s+(\d+)', query)

    # Pattern 3: "80 Alice"
    reverse_pairs = re.findall(r'(\d+)\s+([A-Z][a-z]+)', query)
    pairs += [(name, num) for num, name in reverse_pairs]

    if not pairs:
        return {"output": ""}

    # Remove duplicates (important)
    unique = {}
    for name, num in pairs:
        unique[name] = int(num)

    # Find highest
    winner = max(unique.items(), key=lambda x: x[1])[0]

    return {
        "output": winner
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
