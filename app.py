from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "").lower()

    # 🔥 STEP 1: Extract ONLY correct input number

    # Remove "rule X" parts completely
    cleaned = re.sub(r'rule\s*\d+[^.]*', '', query)

    # Extract numbers after cleaning
    nums = list(map(int, re.findall(r'\d+', cleaned)))

    if nums:
        num = nums[-1]   # reliable after cleaning
    else:
        # fallback
        all_nums = list(map(int, re.findall(r'\d+', query)))
        num = max(all_nums) if all_nums else 0

    # 🔥 STEP 2: Apply rules

    if num % 2 == 0:
        result = num * 2
    else:
        result = num + 10

    if result > 20:
        result -= 5
    else:
        result += 3

    # 🔥 STEP 3: STRICT OUTPUT

    if result % 3 == 0:
        return jsonify({"output": "FIZZ"})
    else:
        return jsonify({"output": str(result)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
