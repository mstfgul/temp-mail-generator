import requests
import random
import string

BASE_URL = "https://api.mail.tm"


def get_domains():
    url = f"{BASE_URL}/domains"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['hydra:member']


def create_account(username, domain, password):
    url = f"{BASE_URL}/accounts"
    payload = {
        "address": f"{username}@{domain}",
        "password": password
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()


def get_token(address, password):
    url = f"{BASE_URL}/token"
    payload = {
        "address": address,
        "password": password
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()['token']


def get_messages(token, page=1):
    url = f"{BASE_URL}/messages?page={page}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_message_detail(token, message_id):
    url = f"{BASE_URL}/messages/{message_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def random_username(length=10):
    # Generate username with lowercase letters and digits
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def random_password(length=12):
    # Generate strong password with letters, digits and special characters
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))


def main():
    # 1. Get domains
    domains = get_domains()
    if not domains:
        print("No domains available.")
        return
    domain = domains[0]['domain']
    print(f"Selected domain: {domain}")

    # 2. Generate random username and password
    username = random_username()
    password = random_password()
    print(f"Generated username: {username}")
    print(f"Generated password: {password}")

    # 3. Create account
    account = create_account(username, domain, password)
    print(f"Account created: {account['address']}")

    # 4. Get token
    token = get_token(account['address'], password)
    print(f"Token received: {token}")

    # 5. List messages
    messages = get_messages(token)
    total = messages.get('hydra:totalItems', 0)
    print(f"Total messages: {total}")

    if total > 0:
        msg_id = messages['hydra:member'][0]['id']
        # 6. Get details of the first message
        detail = get_message_detail(token, msg_id)
        print("First message details:")
        print(f"Subject: {detail['subject']}")
        print(f"From: {detail['from']['address']}")
        print(f"Content: {detail['text']}")
    else:
        print("No messages found.")


if __name__ == "__main__":
    main()
