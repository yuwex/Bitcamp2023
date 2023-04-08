import email_watcher

class Character:
    level: int
    name: str
    def announce_email(self):
        print("You have a new email!")
    def announce_unread(self):
        numUnread = email_watcher.Watcher.get_unread_count()
        if (numUnread <= 0):
          return "caughtup"
        elif (numUnread == 1):
          return "oneunread"
        elif (numUnread > 1):
          return "oneunread"    
    def get_score(self):
        #score increases when user interacts with email (read, delete, archive, reply, forward, etc.)
        #for read emails
        numRead = email_watcher.Watcher.update()
        level += numRead

        