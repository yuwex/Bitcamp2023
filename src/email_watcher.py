from simplegmail import Gmail
from simplegmail.message import Message

class Watcher:

    gmail: Gmail

    unread: list[Message]

    def __init__(self):
        self.gmail = Gmail()
        self.unread = []
        self.update()

    """
    Returns the number of read emails since the last update
    """
    def update(self) -> int:
        old_unread = self.unread
        new_unread = self.gmail.get_unread_inbox()
        new_unread_ids = [m.id for m in new_unread]


        read_messages: list[Message] = []

        for m in old_unread:
            if m.id not in new_unread_ids:
                read_messages.append(m)

        self.unread = new_unread

        return len(read_messages)
        
    """
    Returns the number of unread emails
    """
    def get_unread_count(self):
        return len(self.unread)

