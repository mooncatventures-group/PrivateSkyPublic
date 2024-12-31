from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64
import os

app = Flask(__name__)

# Mapping for encoding hex to alphabetic representation
hex_to_alpha = {
    '0': 'g', '1': 'h', '2': 'i', '3': 'j', '4': 'k', '5': 'l',
    '6': 'm', '7': 'n', '8': 'o', '9': 'p',
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 'f': 'f'
}

# Function to encrypt the message using AES-256
def encrypt_message(message, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return ciphertext

# Flask route to encode the message
@app.route('/encode', methods=['POST'])
def encode_message():
    data = request.json
    message = data.get('message')

    if not message:
        return jsonify({"error": "Message is required"}), 400

    # Generate a random 32-byte AES key and 16-byte IV
    key = os.urandom(32)
    iv = os.urandom(16)

    # Encrypt the message
    encrypted_message = encrypt_message(message, key, iv)

    # Convert encrypted message to hex
    hex_string = encrypted_message.hex()

    # Convert hex to alphabetic encoding
    alpha_encoded = ''.join(hex_to_alpha[char] for char in hex_string)

    return jsonify({
        "originalMessage": message,
        "alphabeticEncoded": alpha_encoded,
        "key": base64.b64encode(key).decode(),
        "iv": base64.b64encode(iv).decode()
    })

if __name__ == '__main__':
    app.run(port=5000)
