from typing import Dict, Literal

Nations = Literal["British", "Spanish", "French", "Dutch", "Pirate", "German", "Portuguese"]

class Stats:
    def __init__(self, health: int, navigation: int, fencing: int, gunnery: int,
                 leadership: int, charm: int, luck: int, wit: int, trade: int,
                 status: Dict[Nations, str], marquees: Dict[Nations, str]):
        self.health = health
        self.navigation = navigation
        self.fencing = fencing
        self.gunnery = gunnery
        self.leadership = leadership
        self.charm = charm
        self.luck = luck
        self.wit = wit
        self.trade = trade
        self.status = status
        self.marquees = marquees

    def __str__(self):
        return (f"Health: {self.health}\nNavigation: {self.navigation}\n"
                f"Fencing: {self.fencing}\nGunnery: {self.gunnery}\nLeadership: {self.leadership}\n"
                f"Charm: {self.charm}\nLuck: {self.luck}\nWit: {self.wit}\nTrade: {self.trade}\n"
                f"Status: {self.status}\nMarquees: {self.marquees}")
    
    def __repr__(self):
        return (f"Stats(health={self.health}, navigation={self.navigation}, fencing={self.fencing},"
                f"gunnery={self.gunnery}, leadership={self.leadership}, charm={self.charm},"
                f"luck={self.luck}, wit={self.wit}, trade={self.trade}, status={self.status},"
                f"marquees={self.marquees}")

    def __eq__(self, other):
        return (self.health == other.health and self.navigation == other.navigation and
                self.fencing == other.fencing and self.gunnery == other.gunnery and
                self.leadership == other.leadership and self.charm == other.charm and
                self.luck == other.luck and self.wit == other.wit and self.trade == other.trade and
                self.status == other.status and self.marquees == other.marquees)

    def __ne__(self, other):
        return not self.__eq__(other)



class Player:
    def __init__(self, name: str, stats: Stats):
        self.name = name
        self.stats = stats

    def __str__(self):
        return f"Name: {self.name}\nStats: {self.stats}"

    def __repr__(self):
        return f"Player(name={self.name}, stats={self.stats})"

    def __eq__(self, other):
        return self.name == other.name and self.stats == other.stats

    def __ne__(self, other):
        return not self.__eq__(other)

def main():
    stats = Stats(health=100, navigation=10, fencing=10, gunnery=10, leadership=10,
                  charm=10, luck=10, wit=10, trade=10, status={}, marquees={})
    player = Player(name="Jack Sparrow", stats=stats)
    print(player)

if __name__ == "__main__":
    main()
