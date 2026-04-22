from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def extract_number(query: str) -> int:
    """
    Extract the most relevant number from query safely.
    Priority:
    1. Numbers outside 'rule' statements
    2. Otherwise, last number in query
    """
    # Remove rule statements safely
    cleaned = re.sub(r'rule\s*\d+.*?(?=rule|$)', '', query, flags=re.IGNORECASE)

    nums = re.findall(r'\d+', cleaned)

    if nums:
        return int(nums[-1])

    # fallback: last number anywhere
    all_nums = re.findall(r'\d+', query)
    if all_nums:
        return int(all_nums[-1])

    return 0


def apply_rules(num: int) -> str:
    """
    Apply transformation rules cleanly.
    """

    # Step 1: even / odd
    if num % 2 == 0:
        result = num * 2
    else:
        result = num + 10

    # Step 2: threshold rule
    if result > 20:
        result -= 5
    else:
        result += 3

    # Step 3: FIZZ rule
    if result % 3 == 0:
        return "FIZZ"

    return str(result)


@app.route("/", methods=["POST"])
def solve():
    try:
        data = request.get_json(force=True)

        if not data or "query" not in data:
            return jsonify({"error": "Invalid input"}), 400

        query = str(data["query"])

        num = extract_number(query)
        output = apply_rules(num)

        return jsonify({"output": output})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
