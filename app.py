from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # Improved strict regex (handles punctuation properly)
    matches = re.findall(r'([A-Z][a-z]+)\s+scored\s+(\d+)', query)

    if not matches:
        return {"output": ""}

    # Find highest scorer
    winner = max(matches, key=lambda x: int(x[1]))[0]

    return {
        "output": winner
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
