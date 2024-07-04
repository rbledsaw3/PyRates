from ..utils.random_engine import generate_ship_name

class Ship:
    def __init__(self, name=None, ship_class="Sloop", min_nav=3, nav_cost=2, guns=4, min_crew=8, max_crew=32, hull=40, sails=20, mast=10):
        self.name = name if name is not None else generate_ship_name()
        self.ship_class = ship_class
        self.min_nav = min_nav
        self.nav_cost = nav_cost
        self.guns = guns
        self.min_crew = min_crew
        self.max_crew = max_crew
        self.hull = hull
        self.sails = sails
        self.mast = mast

    def __repr__(self):
        return (f"Ship(name={self.name}, ship_class={self.ship_class}, min_nav={self.min_nav}, "
                f"nav_cost={self.nav_cost}, guns={self.guns}, min_crew={self.min_crew}, "
                f"max_crew={self.max_crew}, hull={self.hull}, sails={self.sails}, mast={self.mast})")

if __name__ == "__main__":
    ships = [Ship() for _ in range(10)]
    for ship in ships:
        print(ship)
