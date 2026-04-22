from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # Extract numbers
    numbers = re.findall(r'\d+', query)

    # Sum only even numbers
    total = sum(int(n) for n in numbers if int(n) % 2 == 0)

    # 🚨 CRITICAL: return EXACT string, no formatting issues
    return {
        "output": str(total)
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
