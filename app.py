from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "").lower()

    # 🔥 STEP 1: Remove ALL rule sentences completely
    query = re.sub(r'rule\s*\d+.*?(?=rule|$)', '', query)

    # 🔥 STEP 2: Extract numbers AFTER cleaning
    nums = re.findall(r'\d+', query)

    if nums:
        num = int(nums[-1])   # safest choice
    else:
        num = 0

    # 🔥 STEP 3: Apply rules
    if num % 2 == 0:
        result = num * 2
    else:
        result = num + 10

    if result > 20:
        result -= 5
    else:
        result += 3

    # 🔥 STEP 4: STRICT OUTPUT
    if result % 3 == 0:
        return jsonify({"output": "FIZZ"})
    else:
        return jsonify({"output": str(result)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
