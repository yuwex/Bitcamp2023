import json
import random

class EventMessages:
    on_email: list[str]
    on_read: list[str]

    def __init__(self, file: str = "event_messages.json"):
        with open(file, "r") as f:
            data = json.loads(f.read())
            self.on_email = data["on_email"]
            self.on_read = data["on_read"]
        
    def get_email_response(self) -> str:
        return random.choice(self.on_email)
    
    def get_read_response(self) -> str:
        return random.choice(self.on_read)

if __name__ == "__main__":
    em = EventMessages("src/event_messages.json")
    print(em.get_email_response())
    print(em.get_read_response())
