class Cell:
    def __init__(self, coordinate: str):
        self.coordinate = coordinate
        self.ship = None
        self.empty = True
    
    def place_ship(self, ship: object):
        self.ship = ship
        self.empty = False