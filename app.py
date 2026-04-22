from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")
    q = query.lower()

    # 🔥 STEP 1: Extract the correct number

    # Priority 1: after "input number"
    match = re.search(r'input\s*number\s*:?\s*(\d+)', q)

    if match:
        num = int(match.group(1))
    else:
        # Priority 2: numbers after "number"
        match2 = re.search(r'number\s*:?\s*(\d+)', q)
        if match2:
            num = int(match2.group(1))
        else:
            # Priority 3: take LAST number (ignore rule 1,2,3)
            nums = re.findall(r'\d+', q)
            num = int(nums[-1]) if nums else 0

    # 🔥 STEP 2: Apply rules dynamically

    # Rule 1
    if "even" in q and "double" in q:
        if num % 2 == 0:
            result = num * 2
        else:
            result = num + 10
    else:
        result = num

    # Rule 2
    if "result >" in q or "greater than" in q:
        threshold_match = re.search(r'>(\s*)(\d+)', q)
        threshold = int(threshold_match.group(2)) if threshold_match else 20

        if result > threshold:
            result -= 5
        else:
            result += 3

    # Rule 3
    if "divisible by 3" in q:
        if result % 3 == 0:
            return jsonify({"output": "FIZZ"})
        else:
            return jsonify({"output": str(result)})

    # fallback
    return jsonify({"output": str(result)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
