from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")
    q = query.lower()

    num = None

    # 🔥 STEP 1: Extract number near keywords (MOST IMPORTANT)
    patterns = [
        r'input\s*number\s*:?\s*(\d+)',
        r'number\s*:?\s*(\d+)',
        r'given\s*(\d+)',
        r'input\s*:?\s*(\d+)'
    ]

    for p in patterns:
        match = re.search(p, q)
        if match:
            num = int(match.group(1))
            break

    # 🔥 STEP 2: Fallback (ignore rule numbers)
    if num is None:
        nums = list(map(int, re.findall(r'\d+', q)))
        filtered = [n for n in nums if n > 3]

        if filtered:
            num = filtered[-1]
        else:
            num = nums[-1] if nums else 0

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
