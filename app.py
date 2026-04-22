from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    q = query.lower()

    # -------- LEVEL 3 (STRICT + SAFE) --------
    if "odd" in q:
        num_match = re.search(r'\d+', q)
        if num_match:
            num = int(num_match.group())
            if num % 2 != 0:
                return jsonify({"output": "YES"})
            else:
                return jsonify({"output": "NO"})

    if "even" in q:
        num_match = re.search(r'\d+', q)
        if num_match:
            num = int(num_match.group())
            if num % 2 == 0:
                return jsonify({"output": "YES"})
            else:
                return jsonify({"output": "NO"})

    return jsonify({"output": ""})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
