from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")

    # STEP 1: Extract the correct input number
    match = re.search(r'input\s*number\s*(\d+)', query.lower())
    
    if match:
        num = int(match.group(1))
    else:
        # fallback → take last number in query
        nums = re.findall(r'\d+', query)
        if not nums:
            return jsonify({"output": ""})
        num = int(nums[-1])

    # STEP 2: Apply rules

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
        answer = "FIZZ"
    else:
        answer = str(result)

    # STEP 3: Return exact format
    return jsonify({
        "output": answer
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
