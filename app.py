from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

def solve_query(query):
    numbers = list(map(int, re.findall(r'\d+', query)))

    if "+" in query or "add" in query:
        return f"The sum is {sum(numbers)}."

    elif "-" in query or "subtract" in query:
        return f"The difference is {numbers[0] - numbers[1]}."

    elif "*" in query or "multiply" in query:
        return f"The product is {numbers[0] * numbers[1]}."

    elif "/" in query or "divide" in query:
        return f"The result is {numbers[0] / numbers[1]}."

    return "I cannot understand the question."

@app.route('/', methods=['POST'])
def api():
    data = request.get_json()
    query = data.get("query", "")

    return jsonify({
        "output": solve_query(query)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
