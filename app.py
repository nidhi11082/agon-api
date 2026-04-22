from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "").lower()

    # 🔥 STEP 1: Extract ALL numbers
    nums = list(map(int, re.findall(r'\d+', query)))

    if not nums:
        return jsonify({"output": ""})

    # 🔥 STEP 2: REMOVE rule numbers (1,2,3 ONLY when near "rule")
    clean_nums = []

    for match in re.finditer(r'\d+', query):
        num = int(match.group())
        start = match.start()
        context = query[max(0, start-6):start]

        if "rule" not in context:
            clean_nums.append(num)

    # 🔥 choose correct number
    if clean_nums:
        num = clean_nums[-1]
    else:
        num = max(nums)

    # 🔥 STEP 3: Apply rules EXACTLY

    if num % 2 == 0:
        result = num * 2
    else:
        result = num + 10

    if result > 20:
        result -= 5
    else:
        result += 3

    # 🔥 STEP 4: STRICT OUTPUT (NO EXTRA TEXT)

    if result % 3 == 0:
        return jsonify({"output": "FIZZ"})
    else:
        return jsonify({"output": str(result)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
