# 8.py

emails = ("a@example.com", "b@example.com")
message = {'subject': "You have an email.",
           'message': "This is an email to you."}

template = """
From: <{0[0]}>
To: <{0[1]}>
Subject: {message[subject]} {message[message]}
"""

print(template.format(emails, message=message))
