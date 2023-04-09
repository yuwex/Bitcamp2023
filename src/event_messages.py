import json
import random
from typing import Any

class EventMessages:
    on_email: list[str]
    on_read: list[str]

    def __init__(self, file: str = "event_messages.json"):
        with open(file, "r") as f:
            data = json.loads(f.read())
            self.on_email: list[str] = data["on_email"]
            self.on_read: list[str] = data["on_read"]
            self.on_buy_success: list[str] = data["on_buy_success"]
            self.on_buy_expensive: list[str] = data['on_buy_expensive']
            self.on_buy_owned: list[str] = data['on_buy_owned']
            self.on_sell_success: list[str] = data['on_sell_success']
            
            # character class messages
            self.on_multiple_unread: list[str] = data['on_multiple_unread']
            self.on_one_unread: list[str] = data['on_one_unread']
            self.on_all_emails_read: list[str] = data['on_all_emails_read']
            self.on_one_unread: list[str] = data['on_one_unread']

            
    def email_response(self) -> str:
        return random.choice(self.on_email)
    
    def read_response(self) -> str:
        return random.choice(self.on_read)
    
    def buy_success(self, item: str, upgrade_cost: int) -> str:
        return random.choice(self.on_buy_success).format(item=item, upgradeCost=upgrade_cost)
    
    def buy_expensive(self, cost: int) -> str:
        return random.choice(self.on_buy_expensive).format(cost=cost)

    def buy_owned(self) -> str:
        return random.choice(self.on_buy_owned)
    
    def sell_success(self, item: str, cost: int) -> str:
        return random.choice(self.on_sell_success).format(item=item, cost=cost)
    
    def all_emails_read(self) -> str:
        return random.choice(self.on_all_emails_read)
    def one_unread(self) -> str:
        return random.choice(self.on_one_unread)
    def multiple_unread(self) -> str:
        return random.choice(self.on_multiple_unread)
   

if __name__ == "__main__":
    em = EventMessages("src/event_messages.json")
    print(em.read_response())
    print(em.email_response())
    print(em.buy_success("Sword", 50))
    print(em.buy_expensive(100))
    print(em.buy_owned())
    print(em.sell_success("Shield", 22))
    print(em.all_emails_read())
    print(em.one_unread())
    print(em.multiple_unread())
