from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # STEP 1: Extract only the actual math part
    # Look for pattern like: "What is 13 + 7"
    match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', query)

    if not match:
        return {"output": ""}

    a = int(match.group(1))
    op = match.group(2)
    b = int(match.group(3))

    # STEP 2: Compute result safely
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a // b if b != 0 else 0
    else:
        result = 0

    # STEP 3: Return ONLY the number (important!)
    return {
        "output": str(result)
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
