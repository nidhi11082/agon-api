from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")
    q = query.lower()

    # 🔥 STEP 1: Find all numbers with positions
    matches = list(re.finditer(r'\d+', q))

    candidates = []

    for m in matches:
        num = int(m.group())
        start = m.start()

        # Check if this number is part of "rule"
        context_before = q[max(0, start-10):start]

        if "rule" not in context_before:
            candidates.append(num)

    # 🔥 STEP 2: Select correct number
    if candidates:
        # usually only one valid → pick it
        num = candidates[0]
    else:
        # fallback → largest number (safe)
        nums = [int(m.group()) for m in matches]
        num = max(nums) if nums else 0

    # 🔥 STEP 3: Apply rules

    if num % 2 == 0:
        result = num * 2
    else:
        result = num + 10

    if result > 20:
        result -= 5
    else:
        result += 3

    # 🔥 STEP 4: Output EXACT

    if result % 3 == 0:
        return jsonify({"output": "FIZZ"})
    else:
        return jsonify({"output": str(result)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
