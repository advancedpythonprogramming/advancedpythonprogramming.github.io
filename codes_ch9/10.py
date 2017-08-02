# 10.py

class EMail:
    def __init__(self, from_addr, to_addr, subject, message):
        self.from_addr = from_addr
        self.to_addr = to_addr
        self.subject = subject
        self.message = message

email = EMail("a@example.com", "b@example.com", "You have an email.",
              "\nThe message is useless.\n\nBye!")

template = """
From: <{0.from_addr}>
To: <{0.to_addr}>
Subject: {0.subject}
{0.message}"""
print(template.format(email))
