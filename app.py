from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # extract numbers
    numbers = list(map(int, re.findall(r'\d+', query)))

    # sum even numbers
    even_sum = sum(n for n in numbers if n % 2 == 0)

    # ✅ RETURN NUMBER (NOT STRING)
    return jsonify({"output": even_sum})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
