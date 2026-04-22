from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "").lower()

    # 🔥 UNIVERSAL NUMBER EXTRACTION
    # Priority 1: input number
    match = re.search(r'input\s*number\s*:?\s*(\d+)', query)

    if match:
        num = int(match.group(1))
    else:
        # Priority 2: number is / given number
        match2 = re.search(r'(?:number|given)\s*(?:is|:)?\s*(\d+)', query)
        if match2:
            num = int(match2.group(1))
        else:
            # Priority 3: LAST number (ignore rule 1,2,3)
            nums = re.findall(r'\d+', query)
            num = int(nums[-1]) if nums else 0

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
