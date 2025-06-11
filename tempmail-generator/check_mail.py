import requests

# Paste the previously obtained token here
TOKEN = "" # noqa


HEADERS = {
    "Authorization": f"Bearer {TOKEN}"
}


def get_messages(page=1):
    # Sends a GET request to retrieve a list of messages from a specific page
    url = f"https://api.mail.tm/messages?page={page}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()  # Raise an error for bad HTTP responses (like 401 or 404) # noqa
    return resp.json()  # Return the response as a Python dictionary


def get_message_detail(message_id):
    # Sends a GET request to retrieve the details of a specific message
    url = f"https://api.mail.tm/messages/{message_id}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()


def main():
    try:
        messages = get_messages()  # Fetch the first page of messages
        total = messages.get("hydra:totalItems", 0)  # Get the total number of messages
        print(f"Total number of messages: {total}")

        if total == 0:
            print("No messages found.")
            return

        first_msg = messages["hydra:member"][0]  # Get the first message from the list
        msg_id = first_msg['id']  # Extract the ID of the first message
        detail = get_message_detail(msg_id)  # Fetch detailed info of the message

        print("\n--- Message Details ---")
        print("Subject:", detail.get('subject'))
        print("From:", detail.get('from', {}).get('address'))
        print("Date:", detail.get('createdAt'))
        print("Content:\n", detail.get('text') or "(No text content)")

    except requests.HTTPError as e:
        print("HTTP Error:", e)
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
