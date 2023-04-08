class Character:
    level: int
    name: str
    def announce_email(self):
        print("You have a new email!")
    def announce_unread(self):
        if (numUnread <= 0):
          print("You have x unread emails!")
        elif (numUnread == 1):
          print("You have an unread email!")
        elif (numUnread > 1):
          print("You have " + numUnread +  " unread emails!")
    def get_score(self):
    