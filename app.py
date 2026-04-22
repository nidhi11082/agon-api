from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "").lower()

    # 🔥 STEP 1: Extract ONLY the actual input number (not rule numbers)
    match = re.search(r'input number\s*:?\s*(\d+)', query)

    if match:
        num = int(match.group(1))
    else:
        # fallback → take LAST number (usually correct input)
        nums = re.findall(r'\d+', query)
        num = int(nums[-1]) if nums else 0

    # 🔥 STEP 2: Apply rules EXACTLY

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
        output = "FIZZ"
    else:
        output = str(result)

    # 🔥 EXACT FORMAT (MOST IMPORTANT)
    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
