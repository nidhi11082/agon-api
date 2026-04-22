from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")
    q = query.lower()

    # 🔥 STEP 1: Extract correct input number (robust)
    
    # Try patterns in priority order
    patterns = [
        r'input\s*number\s*:?\s*(\d+)',
        r'number\s*is\s*(\d+)',
        r'given\s*(\d+)',
        r'number\s*:?\s*(\d+)'
    ]

    num = None

    for p in patterns:
        match = re.search(p, q)
        if match:
            num = int(match.group(1))
            break

    # Fallback → take LAST number (ignore Rule 1,2,3)
    if num is None:
        nums = re.findall(r'\d+', q)
        if nums:
            num = int(nums[-1])
        else:
            num = 0

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

    # 🔥 STEP 3: EXACT RESPONSE FORMAT
    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
