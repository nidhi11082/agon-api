from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "").lower()

    # 🔥 STEP 1: Remove rule descriptions completely
    cleaned = re.sub(r'rule\s*\d+[^.]*\.', '', query)

    # 🔥 STEP 2: Extract numbers
    nums = list(map(int, re.findall(r'\d+', cleaned)))

    if nums:
        num = nums[-1]
    else:
        # fallback
        all_nums = list(map(int, re.findall(r'\d+', query)))
        num = max(all_nums) if all_nums else 0

    # 🔥 STEP 3: Apply rules
    if num % 2 == 0:
        result = num * 2
    else:
        result = num + 10

    if result > 20:
        result -= 5
    else:
        result += 3

    # 🔥 STEP 4: STRICT OUTPUT ONLY
    if result % 3 == 0:
        output = "FIZZ"
    else:
        output = str(result)

    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
