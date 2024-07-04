from ..utils.random_engine import generate_ship_name

class ShipClass:
    def __init__(self, ship_class: str, min_crew: int, max_crew: int, cargo: int,
                 max_cargo: int, guns: int, max_guns: int, ammo: int,
                 speed: int, max_speed: int, hull: int, sails: int, mast: int,
                 min_nav: int, nav_cost: int, upgrades: int):
        if not isinstance(ship_class, str):
            raise TypeError("ship_class must be a string")
        if not all(isinstance(param, int) for param in 
                   [min_crew, max_crew, cargo, max_cargo, guns, max_guns, ammo,
                    speed, max_speed, hull, sails, mast, min_nav, nav_cost, upgrades]):
            raise TypeError("All parameters except ship_class must be integers")
        if any(param < 0 for param in 
               [min_crew, max_crew, cargo, max_cargo, guns, max_guns, ammo,
                speed, max_speed, hull, sails, mast, min_nav, nav_cost, upgrades]):
            raise ValueError("Integer parameters must not be negative")

        self.ship_class = ship_class
        self.min_crew = min_crew
        self.max_crew = max_crew
        self.cargo = cargo
        self.max_cargo = max_cargo
        self.guns = guns
        self.max_guns = max_guns
        self.ammo = ammo
        self.speed = speed
        self.max_speed = max_speed
        self.hull = hull
        self.sails = sails
        self.mast = mast
        self.min_nav = min_nav
        self.nav_cost = nav_cost
        self.upgrades = upgrades

class Ship:
    def __init__(self, ship_class: ShipClass, name: str = None):
        if not isinstance(ship_class, ShipClass):
            raise TypeError("ship_class must be an instance of ShipClass")
        if name is not None and not isinstance(name, str):
            raise TypeError("name must be a string for defined names or None for randomly generated names")

        self.name = name if name is not None else generate_ship_name()
        self.ship_class = ship_class.ship_class
        self.min_crew = ship_class.min_crew
        self.max_crew = ship_class.max_crew
        self.cargo = ship_class.cargo
        self.max_cargo = ship_class.max_cargo
        self.guns = ship_class.guns
        self.max_guns = ship_class.max_guns
        self.ammo = ship_class.ammo
        self.speed = ship_class.speed
        self.max_speed = ship_class.max_speed
        self.hull = ship_class.hull
        self.current_hull = self.hull
        self.sails = ship_class.sails
        self.current_sails = self.sails
        self.mast = ship_class.mast
        self.current_mast = self.mast
        self.min_nav = ship_class.min_nav
        self.nav_cost = ship_class.nav_cost
        self.upgrades = ship_class.upgrades

    def __repr__(self):
        hull_condition = (self.current_hull / self.hull) * 100
        sails_condition = (self.current_sails / self.sails) * 100
        mast_condition = (self.current_mast / self.mast) * 100
        return (f"{self.name}:\n"
                f"    Class: {self.ship_class}, Minimum/Maximum Crew: {self.min_crew}/{self.max_crew},\n"
                f"    Cargo Hold/Maximum Cargo: {self.cargo}/{self.max_cargo}, Cannons/Maximum Cannons: {self.guns}/{self.max_guns},\n"
                f"    Ammunition Hold: {self.ammo}, Speed/Maximum Speed: {self.speed}/{self.max_speed},\n"
                f"    Hull Condition: {hull_condition:.2f}%, Sail Condition: {sails_condition:.2f}%, Mast Condition: {mast_condition:.2f}%\n"
                f"    Required Navigation Skill: {self.min_nav}, Navigation Cost: {self.nav_cost},\n"
                f"    Available Upgrades: {self.upgrades}\n")

# Pre-defined ship classes:

SLOOP = ShipClass(
        ship_class="Sloop", min_crew=8, max_crew=10, cargo=10, max_cargo=12,
        guns=2, max_guns=4, ammo=400, speed=131, max_speed=132, hull=120,
        sails=50, mast=30, min_nav=1, nav_cost=3, upgrades=2)

PINNACE = ShipClass(
        ship_class="Pinnace", min_crew=25, max_crew=31, cargo=20, max_cargo=29,
        guns=4, max_guns=7, ammo=800, speed=113, max_speed=116, hull=192,
        sails=80, mast=48, min_nav=8, nav_cost=8, upgrades=6)

BARQUE = ShipClass(
        ship_class="Barque", min_crew=40, max_crew=58, cargo=34, max_cargo=43,
        guns=6, max_guns=15, ammo=1600, speed=121, max_speed=124, hull=264,
        sails=110, mast=66, min_nav=16, nav_cost=11, upgrades=12)

BRIG = ShipClass(
        ship_class="Brig", min_crew=45, max_crew=88, cargo=55, max_cargo=86,
        guns=8, max_guns=23, ammo=1800, speed=116, max_speed=122, hull=320,
        sails=140, mast=120, min_nav=18, nav_cost=12, upgrades=15)

if __name__ == "__main__":
    sloops = [Ship(ship_class=SLOOP) for _ in range(3)]
    for sloop in sloops:
        print(sloop)
    pinnaces = [Ship(ship_class=PINNACE) for _ in range(3)]
    for pinnace in pinnaces:
        print(pinnace)
    barques = [Ship(ship_class=BARQUE) for _ in range(3)]
    for barque in barques:
        print(barque)
    brigs = [Ship(ship_class=BRIG) for _ in range(3)]
    for brig in brigs:
        print(brig)
