class PostOffice:
    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}

    def send_message(self, sender, recipient, message_body, urgent=False):
        if recipient not in self.boxes:
            raise KeyError("Recipient does not exist.")

        self.message_id += 1
        message_details = {
            'id': self.message_id,
            'body': message_body,
            'sender': sender,
        }
        if urgent:
            self.boxes[recipient].insert(0, message_details)
        else:
            self.boxes[recipient].append(message_details)
        return self.message_id

    def read_inbox(self, username, n=None):
        """Retrieve up to N messages from a user's inbox and mark them as read."""
        if username not in self.boxes:
            raise KeyError("User does not exist.")

        messages = self.boxes[username][:n] if n else self.boxes[username]
        self.boxes[username] = self.boxes[username][len(messages):]  # Remove read messages
        return messages

    def search_inbox(self, username, query):
        """Search for messages containing the query string in a user's inbox."""
        if username not in self.boxes:
            raise KeyError("User does not exist.")

        return [msg for msg in self.boxes[username] if query in msg['body']]
