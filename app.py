from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")

    q = query.lower()

    # 🔥 ONLY capture number after "input number"
    match = re.search(r'input number\s*:?[\s]*(\d+)', q)

    if match:
        num = int(match.group(1))
    else:
        nums = re.findall(r'\d+', q)
        num = int(nums[-1]) if nums else 0

    # Apply rules
    if num % 2 == 0:
        result = num * 2
    else:
        result = num + 10

    if result > 20:
        result -= 5
    else:
        result += 3

    # 🔥 STRICT OUTPUT
    if result % 3 == 0:
        return jsonify({"output": "FIZZ"})
    else:
        return jsonify({"output": str(result)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
