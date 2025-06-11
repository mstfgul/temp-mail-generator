# 📬 Temp Mail Usage

This project uses the [mail.tm](https://mail.tm) API to create a temporary email address and read incoming messages.

## 🔧 Requirements

- Python 3.7 or higher
- `requests` library (`pip install requests`)

## 🚀 How to Use

1. Run `main.py`:
   ```bash
   python main.py

2. The script will automatically:
   - Generate a random email address and password
   - Create an account on mail.tm
   - Retrieve an authentication token
   - Check the inbox
   - Display the content of the first message (if available)

3. To check messages with an existing token:
   - Open `read_messages.py`
   - Paste your token into the `TOKEN` variable
   - Run:
     ```bash
     python read_messages.py
     ```
