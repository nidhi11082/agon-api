from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # Extract all numbers
    numbers = list(map(int, re.findall(r'\d+', query)))

    # Sum only even numbers
    even_sum = sum(n for n in numbers if n % 2 == 0)

    # Return STRICT format (no spaces, no text)
    return jsonify({"output": str(even_sum)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
