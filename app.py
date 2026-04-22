from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    q = query.lower()

    # ---- LEVEL 4 (ROBUST) ----
    if "sum" in q and "even" in q:
        numbers = list(map(int, re.findall(r'\d+', q)))
        even_sum = sum(n for n in numbers if n % 2 == 0)

        # 🔒 STRICT OUTPUT (NO EXTRA CHARACTERS)
        return jsonify({"output": str(even_sum)})

    return jsonify({"output": ""})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
