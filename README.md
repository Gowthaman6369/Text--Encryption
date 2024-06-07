
## Setup

### Prerequisites

- Python 3.x
- Git

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Gowthaman6369/Text-Encryption.git
    cd Text-Encryption
    ```

2. **Create and activate a virtual environment**:
    - On Windows:
      ```sh
      python -m venv venv
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. **Run the Flask application**:
    ```sh
    python app.py
    ```

2. **Access the application**:
    - Open a web browser and go to `http://127.0.0.1:5000/`.

### Usage

- Enter text in the input field.
- Click the "Encrypt" button to encrypt the text.
- Click the "Decrypt" button to decrypt the text.

### Troubleshooting

If you encounter a `TemplateNotFound` error, ensure your project structure is correct, and the `templates` directory contains `index.html`.

### Accessing the Application from Other Devices

To access the application from your phone or another device on the same network:

1. Modify `app.py` to run on all network interfaces:
    ```python
    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
    ```

2. Run the application:
    ```sh
    python app.py
    ```

3. Find your computer's IP address:
    - On Windows: Run `ipconfig` in Command Prompt and look for the IPv4 Address.
    - On macOS/Linux: Run `ifconfig` in Terminal and look for the inet address.

4. Open a web browser on your phone and go to `http://<your-ip-address>:5000`.


