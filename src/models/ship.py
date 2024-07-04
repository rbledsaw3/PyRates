from ..utils.random_engine import generate_ship_name

class Ship:
    def __init__(self, name=generate_ship_name(), ship_class="Sloop", min_nav=3, nav_cost=2, guns=4, min_crew=8, max_crew=32, hull=40, sails=20, mast=10):
        self.name = name
        self.ship_class = ship_class
        self.min_nav = min_nav
        self.nav_cost = nav_cost
        self.guns = guns
        self.min_crew = min_crew
        self.max_crew = max_crew
        self.hull = hull
        self.sails = sails
        self.mast = mast

