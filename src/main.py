from simplegmail import Gmail

gmail = Gmail()

messages = gmail.get_unread_inbox()
for m in messages:
    print(f"{m.sender}")