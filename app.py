from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def extract_number(query: str) -> int:
    """
    Extract the correct number robustly.
    Handles:
    - negative numbers
    - decimals
    - mixed text
    """

    # Remove all "rule ..." parts (case insensitive, multiline safe)
    cleaned = re.sub(r'rule\s*\d+.*?(?=rule|$)', '', query, flags=re.IGNORECASE | re.DOTALL)

    # Extract numbers (int + float + negative)
    nums = re.findall(r'-?\d+\.?\d*', cleaned)

    if nums:
        return int(float(nums[-1]))  # safest conversion

    # fallback: from original query
    all_nums = re.findall(r'-?\d+\.?\d*', query)
    if all_nums:
        return int(float(all_nums[-1]))

    return 0


def apply_rules(num: int) -> str:

    # Even / Odd
    if num % 2 == 0:
        result = num * 2
    else:
        result = num + 10

    # Threshold
    if result > 20:
        result -= 5
    else:
        result += 3

    # FIZZ rule
    if result % 3 == 0:
        return "FIZZ"

    return str(result)


@app.route("/", methods=["POST"])
def solve():
    try:
        data = request.get_json(force=True)

        query = str(data.get("query", ""))

        num = extract_number(query)
        output = apply_rules(num)

        return jsonify({"output": output})

    except Exception:
        return jsonify({"output": "0"})  # safe fallback


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
