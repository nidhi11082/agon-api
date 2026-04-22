from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")
    q = query.lower()

    # 🔥 STEP 1: STRONG NUMBER EXTRACTION

    # Priority 1: explicit "input number"
    match = re.search(r'input\s*number\s*:?\s*(\d+)', q)

    if match:
        num = int(match.group(1))
    else:
        # Priority 2: numbers NOT near "rule"
        candidates = []
        for m in re.finditer(r'\d+', q):
            n = int(m.group())
            start = m.start()
            context = q[max(0, start-8):start]

            if "rule" not in context:
                candidates.append(n)

        if candidates:
            # take LAST valid candidate (most reliable)
            num = candidates[-1]
        else:
            # fallback → largest number
            nums = list(map(int, re.findall(r'\d+', q)))
            num = max(nums) if nums else 0

    # 🔥 STEP 2: APPLY RULES EXACTLY

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
