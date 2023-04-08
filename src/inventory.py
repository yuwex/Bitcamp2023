from item import Item

class Inventory:

    doubloons: int
    items: list[Item]

    def __init__(self):
        self.doubloons = 0
   
    def buy(self, item: Item) -> bool:
        if not item.owned:
            if (self.doubloons >= item.cost):
                self.items.append(item)
                item.owned = True
                self.doubloons -= item.cost

                return "bought"

            else:
                return "expensive"
                
        else:
            return "owned"
        
    def sell_back(self, item: Item) -> str:
        if item.owned:
                item.owned = False
                self.doubloons += (item.cost * 0.75)

                return "sold"


