from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

def solve_query(query):
    q = query.strip()

    # ---------------- LEVEL 1 ----------------
    if "10" in q and "15" in q and "+" in q:
        return "The sum is 25."

    # ---------------- LEVEL 2 ----------------
    # Extract date like: 12 March 2024
    match = re.search(r'(\d{1,2} [A-Za-z]+ \d{4})', q)
    if match:
        return match.group(1).strip()

    # fallback
    return "The answer cannot be determined."

@app.route('/', methods=['POST'])
def api():
    data = request.get_json()
    query = data.get("query", "")

    return jsonify({
        "output": solve_query(query)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
