from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def solve(query: str) -> str:
    # Extract the input number from the query
    match = re.search(r'input number[:\s]+(\d+)', query, re.IGNORECASE)
    if not match:
        # Try to find any number in the query
        numbers = re.findall(r'\b(\d+)\b', query)
        if not numbers:
            return "unknown"
        n = int(numbers[-1])
    else:
        n = int(match.group(1))

    # Rule 1
    if n % 2 == 0:
        result = n * 2
    else:
        result = n + 10

    # Rule 2
    if result > 20:
        result -= 5
    else:
        result += 3

    # Rule 3
    if result % 3 == 0:
        return "FIZZ"
    else:
        return str(result)

@app.route('/', methods=['POST'])
def handle():
    data = request.get_json()
    query = data.get('query', '')
    answer = solve(query)
    return jsonify({"output": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
