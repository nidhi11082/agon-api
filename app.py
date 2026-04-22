from flask import Flask, request
import re
import os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json(force=True)
    query = data.get("query", "")

    # STEP 1: Extract first number (robust)
    nums = re.findall(r'\d+', query)
    if not nums:
        return {"output": ""}

    num = int(nums[0])

    # STEP 2: Rule 1
    if num % 2 == 0:
        num = num * 2
    else:
        num = num + 10

    # STEP 3: Rule 2
    if num > 20:
        num = num - 5
    else:
        num = num + 3

    # STEP 4: Rule 3
    if num % 3 == 0:
        return {"output": "FIZZ"}
    else:
        return {"output": str(num)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
