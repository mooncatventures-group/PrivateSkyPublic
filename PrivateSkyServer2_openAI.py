from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your OpenAI API key
OPENAI_API_KEY = "YOUR_API_KEY_HERE"

@app.route('/encode', methods=['POST'])
def encode_message():
    data = request.get_json()

    # Get mode and message from the request
    mode = data.get('mode', 'mode2')  # Default to mode2
    message = data.get('message', '')

    # Example hex generation based on mode (stub logic for Sub-Lex)
    if mode == 'mode2':
        hex_string = ''.join(format(ord(char), 'x') for char in message)
    elif mode == 'mode3':
        hex_string = ''.join(format(ord(char), 'x').replace('0', 'g') for char in message)
    else:
        return jsonify({"error": "Invalid mode"}), 400

    # Pass the hex string to OpenAI for narrative generation
    prompt = (
        f"Generate any 300-character or more story about a dragon using all the characters in the string (append the hex string). "
        f"The story should include one occurrence of each character: {hex_string}"
    )
    generated_story = call_openai_api(prompt)

    return jsonify({
        "hex": hex_string,
        "story": generated_story
    })


def call_openai_api(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        choices = result.get("choices", [])
        if choices:
            return choices[0].get("message", {}).get("content", "")
        else:
            return "No content returned."
    else:
        return f"Error: {response.status_code}, {response.text}"


if __name__ == '__main__':
    app.run(debug=True)
