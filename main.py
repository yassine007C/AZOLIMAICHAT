from flask import Flask, request, jsonify, render_template
from openai import OpenAI

app = Flask(__name__)

# Set your API key and base URL
YOUR_API_KEY = "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"
client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    user_message = data.get('message')

    messages = [
        {
            "role": "system",
            "content": (
                "You are Hema, a friendly, witty, and wise AI assistant. "
                "Engage with the user in a warm and helpful manner."
            ),
        },
        {
            "role": "user",
            "content": user_message
        },
    ]

    response = client.chat.completions.create(
        model="sonar-pro",  # Use a vision-capable model
        messages=messages,
        stream=False
    )
    assistant_reply = response.choices[0].message.content
    return jsonify({'reply': assistant_reply})
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
