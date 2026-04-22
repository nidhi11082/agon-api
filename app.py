from flask import Flask, request, jsonify
import anthropic
import os

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a precise rule-following calculator. 
The user will give you a query with rules and an input number.
Apply ALL rules in order exactly as stated.
Respond with ONLY the final output value — no explanation, no extra text, no punctuation.
Just the raw answer like: FIZZ or 15 or whatever the result is."""

@app.route("/", methods=["POST"])
def solve():
    data = request.get_json()
    query = data.get("query", "")

    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=64,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": query}
        ]
    )

    answer = message.content[0].text.strip()
    return jsonify({"output": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
