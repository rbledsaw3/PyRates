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

        self.ship_class: str = ship_class
        self.min_crew: int = min_crew
        self.max_crew: int = max_crew
        self.cargo: int = cargo
        self.max_cargo: int = max_cargo
        self.guns: int = guns
        self.max_guns: int = max_guns
        self.ammo: int = ammo
        self.speed: int = speed
        self.max_speed: int = max_speed
        self.hull: int = hull
        self.sails: int = sails
        self.mast: int = mast
        self.min_nav: int = min_nav
        self.nav_cost: int = nav_cost
        self.upgrades: int = upgrades

class Ship:
    def __init__(self, ship_class: ShipClass, name: str = None):
        if not isinstance(ship_class, ShipClass):
            raise TypeError("ship_class must be an instance of ShipClass")
        if name is not None and not isinstance(name, str):
            raise TypeError("name must be a string for defined names or None for randomly generated names")

        self.name: str = name if name is not None else generate_ship_name()
        self.ship_class: ShipClass = ship_class.ship_class
        self.min_crew: int = ship_class.min_crew
        self.max_crew: int = ship_class.max_crew
        self.cargo: int = ship_class.cargo
        self.max_cargo: int = ship_class.max_cargo
        self.guns: int = ship_class.guns
        self.max_guns: int = ship_class.max_guns
        self.ammo: int = ship_class.ammo
        self.speed: int = ship_class.speed
        self.max_speed: int = ship_class.max_speed
        self.hull: int = ship_class.hull
        self.current_hull: int = self.hull
        self.sails: int = ship_class.sails
        self.current_sails: int = self.sails
        self.mast: int = ship_class.mast
        self.current_mast: int = self.mast
        self.min_nav: int = ship_class.min_nav
        self.nav_cost: int = ship_class.nav_cost
        self.upgrades: int = ship_class.upgrades

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
        ship_class = "Sloop", min_crew = 8, max_crew = 10, cargo = 10, max_cargo = 12,
        guns = 2, max_guns = 4, ammo = 400, speed = 131, max_speed = 132, hull = 120,
        sails = 50, mast = 30, min_nav = 1, nav_cost = 3, upgrades = 2)

PINNACE = ShipClass(
        ship_class = "Pinnace", min_crew = 25, max_crew = 31, cargo = 20, max_cargo = 29,
        guns = 4, max_guns = 7, ammo = 800, speed = 113, max_speed = 116, hull = 192,
        sails = 80, mast = 48, min_nav = 8, nav_cost = 8, upgrades = 6)

BARQUE = ShipClass(
        ship_class = "Barque", min_crew = 40, max_crew = 58, cargo = 34, max_cargo = 43,
        guns = 6, max_guns = 15, ammo = 1600, speed = 121, max_speed = 124, hull = 264,
        sails = 110, mast = 66, min_nav = 16, nav_cost = 11, upgrades = 12)

BRIG = ShipClass(
        ship_class = "Brig", min_crew = 45, max_crew = 88, cargo = 55, max_cargo = 86,
        guns = 8, max_guns = 23, ammo = 1800, speed = 116, max_speed = 122, hull = 320,
        sails = 140, mast = 120, min_nav = 18, nav_cost = 12, upgrades = 15)

CARAVEL = ShipClass(
        ship_class = "Caravel", min_crew = 50, max_crew = 75, cargo = 80, max_cargo = 120,
        guns = 8, max_guns = 20, ammo = 2000, speed = 100, max_speed = 116, hull = 288,
        sails = 120, mast = 72, min_nav = 20, nav_cost = 14, upgrades = 14)

CARGO_FLUYT = ShipClass(
        ship_class = "Cargo Fluyt", min_crew = 60, max_crew = 87, cargo = 100, max_cargo = 118,
        guns = 10, max_guns = 19, ammo = 3200, speed = 111, max_speed = 115, hull = 300,
        sails = 100, mast = 100, min_nav = 24, nav_cost = 16, upgrades = 12)

MERCHANTMAN = ShipClass(
        ship_class = "Merchantman", min_crew = 100, max_crew = 133, cargo = 168, max_cargo = 201,
        guns = 16, max_guns = 27, ammo = 2000, speed = 104, max_speed = 112, hull = 360,
        sails = 120, mast = 120, min_nav = 35, nav_cost = 19, upgrades = 14)

PRIVATEER = ShipClass(
        ship_class = "Privateer", min_crew = 70, max_crew = 150, cargo = 80, max_cargo = 120,
        guns = 20, max_guns = 35, ammo = 2500, speed = 115, max_speed = 120, hull = 300,
        sails = 210, mast = 90, min_nav = 40, nav_cost = 20, upgrades = 18)

FRIGATE = ShipClass(
        ship_class = "Frigate", min_crew = 110, max_crew = 175, cargo = 40, max_cargo = 70,
        guns = 26, max_guns = 39, ammo = 2800, speed = 112, max_speed = 116, hull = 532,
        sails = 114, mast = 114, min_nav = 55, nav_cost = 22, upgrades = 16)

FAST_GALLEON = ShipClass(
        ship_class = "Fast Galleon", min_crew = 140, max_crew = 200, cargo = 86, max_cargo = 116,
        guns = 20, max_guns = 50, ammo = 2000, speed = 107, max_speed = 115, hull = 390,
        sails = 80, mast = 117, min_nav = 65, nav_cost = 24, upgrades = 18)

SPANISH_GALLEON = ShipClass(
        ship_class = "Spanish Galleon", min_crew = 210, max_crew = 278, cargo = 242, max_cargo = 327,
        guns = 26, max_guns = 43, ammo = 1600, speed = 100, max_speed = 104, hull = 528,
        sails = 176, mast = 176, min_nav = 80, nav_cost = 27, upgrades = 20)

WAR_GALLEON = ShipClass(
        ship_class = "War Galleon", min_crew = 280, max_crew = 352, cargo = 110, max_cargo = 156,
        guns = 34, max_guns = 80, ammo = 5000, speed = 91, max_speed = 99, hull = 840,
        sails = 180, mast = 180, min_nav = 100, nav_cost = 30, upgrades = 26)

MAN_O_WAR = ShipClass(
        ship_class = "Man-O-War", min_crew = 300, max_crew = 385, cargo = 200, max_cargo = 280,
        guns = 42, max_guns = 95, ammo = 6000, speed = 100, max_speed = 104, hull = 910,
        sails = 195, mast = 195, min_nav = 110, nav_cost = 33, upgrades = 30)

if __name__ == "__main__":
    ship_classes = [SLOOP, PINNACE, BARQUE, BRIG, CARAVEL, CARGO_FLUYT, MERCHANTMAN,
                    PRIVATEER, FRIGATE, FAST_GALLEON, SPANISH_GALLEON, WAR_GALLEON, 
                    MAN_O_WAR]
    all_ships = [Ship(ship_class= sc) for sc in ship_classes]
    for ship in all_ships:
        print(ship)
