from flask import Flask, render_template, request, jsonify
from cryptography.fernet import Fernet
import os

app = Flask(__name__)

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Set the path for templates folder
template_dir = os.path.abspath('encryption/templates')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.json.get('text')
    if text:
        encrypted_text = cipher_suite.encrypt(text.encode()).decode()
        return jsonify({'encrypted_text': encrypted_text})
    return jsonify({'error': 'No text provided'}), 400

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_text = request.json.get('encrypted_text')
    if encrypted_text:
        try:
            decrypted_text = cipher_suite.decrypt(encrypted_text.encode()).decode()
            return jsonify({'decrypted_text': decrypted_text})
        except Exception as e:
            print(str(e))
            return jsonify({'error': 'Invalid encrypted text'}), 400
    return jsonify({'error': 'No encrypted text provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)

