from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "").strip()

    # 🔒 Extract numbers safely
    numbers = [int(x) for x in re.findall(r'\d+', query)]

    # 🔒 Sum even numbers only
    even_sum = 0
    for n in numbers:
        if n % 2 == 0:
            even_sum += n

    # 🔥 RETURN CLEAN STRING (NO EXTRA SPACES)
    return jsonify({"output": f"{even_sum}"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
