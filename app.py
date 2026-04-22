from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "").lower()

    # Replace word operators with symbols
    query = query.replace("plus", "+")
    query = query.replace("minus", "-")
    query = query.replace("multiplied by", "*")
    query = query.replace("times", "*")
    query = query.replace("into", "*")
    query = query.replace("divided by", "/")

    # Extract numbers and operator (robust)
    match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', query)

    if not match:
        return {"output": ""}

    a = int(match.group(1))
    op = match.group(2)
    b = int(match.group(3))

    # Compute result
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

    # Return ONLY number as string
    return {
        "output": str(result)
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
