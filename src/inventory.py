from item import Item

class Inventory:

    doubloons: int

    def __init__(self):
        self.doubloons = 0
   
    def buy(self, item: Item):
        if (item.owned == False):
            if (self.doubloons >= item.cost):
                item.owned = True
                print ("Sold! You now own " + item.name + "!\n It costs " + item.costToUpgrade + " doubloonss to upgrade this item!")
                points -= item.cost
            else:
                print ("Arrrr!! You don't have enough doubloons for this item! \n You need " + item.cost - self.doubloons + " more doubloons!")
        else:
            print ("You already own this item sailor! Try and buy something else...")
    def sell_back(self, item: Item):
        if (item.owned == True):
                item.owned = False
                print ("Sold! You parted with " + item.name + " in exchange for "  + item.cost * 0.75 + " doubloons!")
                self.doubloons += (item.cost * 0.75)
        else:
            print ("You don't own this matey! Try and sell something you already own!")


