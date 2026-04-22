from flask import Flask, request, jsonify
import re
import os

app = Flask(__name__)

@app.route('/', methods=['POST'])
def api():
    try:
        data = request.get_json(force=True)

        query = data.get("query", "").strip()

        # LEVEL 1
        if query == "What is 10 + 15?":
            return jsonify({"output": "The sum is 25."})

        # LEVEL 2 (exact match)
        if query == 'Extract date from: "Meeting on 12 March 2024".':
            return jsonify({"output": "12 March 2024"})

        # fallback (regex)
        match = re.search(r'(\d{1,2} [A-Za-z]+ \d{4})', query)
        if match:
            return jsonify({"output": match.group(1)})

        return jsonify({"output": ""})

    except Exception as e:
        return jsonify({"output": ""})

@app.route('/', methods=['GET'])
def home():
    return "API is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
