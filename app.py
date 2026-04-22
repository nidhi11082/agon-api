from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "").lower()

    # Extract the input number (robust)
    match = re.search(r'number\s*(\d+)', query)
    if not match:
        match = re.search(r'(\d+)', query)

    if not match:
        return {"output": ""}

    num = int(match.group(1))

    # Rule 1
    if num % 2 == 0:
        num = num * 2
    else:
        num = num + 10

    # Rule 2
    if num > 20:
        num = num - 5
    else:
        num = num + 3

    # Rule 3
    if num % 3 == 0:
        return {"output": "FIZZ"}
    else:
        return {"output": str(num)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
