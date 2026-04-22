from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "").lower()

    # Extract number (robust)
    nums = re.findall(r'\d+', query)
    if not nums:
        return {"output": ""}

    num = int(nums[0])

    # RULE 1: detect even/odd rule from text
    if "even" in query and "double" in query:
        if num % 2 == 0:
            num *= 2
        else:
            num += 10

    # RULE 2: detect threshold logic
    if "> 20" in query or "greater than 20" in query:
        if num > 20:
            num -= 5
        else:
            num += 3

    # RULE 3: detect divisibility rule
    if "divisible by 3" in query:
        if num % 3 == 0:
            return {"output": "FIZZ"}
        else:
            return {"output": str(num)}

    # fallback
    return {"output": str(num)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
