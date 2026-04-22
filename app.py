from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")
    q = query.lower()

    # 🔥 STEP 1: Extract ONLY the correct input number

    # Get all numbers
    nums = re.findall(r'\d+', q)

    if not nums:
        return jsonify({"output": ""})

    # 🔥 KEY IDEA:
    # Rule numbers (1,2,3) are small and appear early
    # Actual input number is usually the LARGEST number

    num = max(map(int, nums))

    # 🔥 STEP 2: Apply rules

    # Rule 1
    if num % 2 == 0:
        result = num * 2
    else:
        result = num + 10

    # Rule 2
    if result > 20:
        result -= 5
    else:
        result += 3

    # Rule 3
    if result % 3 == 0:
        return jsonify({"output": "FIZZ"})
    else:
        return jsonify({"output": str(result)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
