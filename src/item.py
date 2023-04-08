class Item:
    name: str
    type: str
    owned: bool
    cost: int
    costToUpgrade: int
    level: int
    

    def __init__(self, name, type, owned, cost, costToUpgrade, level):
        self.name = name
        self.type = type
        self.owned = owned
        if (type == "ability"):
            self.cost = 10
            self.costToUpgrade = 5
            self.level = 1
        elif (type == "cosmetic"):
            self.cost = 5
            self.costToUpgrade = 2
            self.level = -1
        else:
            self.cost = -1
            self.costToUpgrade = -1
            self.level = -1
 






            
