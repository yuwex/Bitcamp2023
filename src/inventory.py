from item import Item

class Inventory:

    doubloons: int
    items: list[Item]

    def __init__(self):
        self.doubloons = 0
   
    def buy(self, item: Item) -> str:
        if not item.owned:
            if (self.doubloons >= item.cost):
                self.items.append(item)
                item.owned = True
                self.doubloons -= item.cost

                return f"Sold! You now own {item.name}!\n It costs {item.costToUpgrade} doubloonss to upgrade this item!"

            else:
                return f"Arrrr!! You don't have enough doubloons for this item!\nYou need {item.cost - self.doubloons} more doubloons!"
                
        else:
            return "You already own this item sailor! Try and buy something else..."
        
    def sell_back(self, item: Item) -> str:
        if item.owned:
                item.owned = False
                print ("Sold! You parted with " + item.name + " in exchange for "  + item.cost * 0.75 + " doubloons!")
                self.doubloons += (item.cost * 0.75)

                return f"Sold! You parted with {item.name} in exchange for {item.cost * 0.75} doubloons!"
        else:
            return "You don't own this matey! Try and sell something you already own!"


