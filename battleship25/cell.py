class Cell:
    def __init__(self, coordinate: str):
        self.coordinate = coordinate
        self.ship = None
        self.empty = True
        self.is_fired_upon = False
    
    def place_ship(self, ship: object):
        self.ship = ship
        self.empty = False

    def fire_upon(self):
        self.is_fired_upon = True
        if self.ship is not None:
            self.ship.hit() 

    def render(self, reveal=False) -> str:
        if not self.is_fired_upon:
            if self.ship and reveal:
                return "S"
            return "."
        if self.ship:
            return "X" if self.ship.sunk() else "H"
        return "M"   