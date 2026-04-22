from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")

    q = query.lower()

    # ✅ STRICT extraction of ONLY input number
    match = re.search(r'input\s*number\s*:?\s*(\d+)', q)

    if match:
        num = int(match.group(1))
    else:
        # fallback → ignore rule numbers (take LAST meaningful number)
        nums = re.findall(r'\d+', q)
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
        answer = "FIZZ"
    else:
        answer = str(result)

    # ✅ EXACT output (critical)
    return jsonify({"output": answer.strip()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
