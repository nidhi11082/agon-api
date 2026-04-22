from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # Extract correct (name, score) pairs ONLY
    matches = re.findall(r'([A-Z][a-z]+)\s+scored\s+(\d+)', query)

    # If nothing matched, fallback (safety)
    if not matches:
        return {"output": ""}

    # Find highest scorer
    winner = max(matches, key=lambda x: int(x[1]))[0]

    # Return EXACT expected format
    return {
        "output": winner
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
