from battleship25.board import Board
from battleship25.ship import Ship
import random

class Game:
    def __init__(self):
        self.player_board = Board()
        self.player_submarine = Ship("Submarine", 2)
        self.player_cruiser = Ship("Cruiser", 2)
        self.cpu_board = Board()
        self.cpu_submarine = Ship("Submarine", 2)
        self.cpu_cruiser = Ship("Cruiser", 3)

    def place_ship(self, board: object, ship: object):
            coords = list(board.cells.keys())
            while True:
                 placement = random.sample(coords, k=ship.length)
                 if board.place(ship, placement):
                      return placement
                 
            
    def cpu_placement(self):
        self.place_ship(self.cpu_board, self.cpu_submarine)
        self.place_ship(self.cpu_board, self.cpu_cruiser)

    def player_cruiser_placement(self):
        while True:
            raw = input("Enter the squares for the Cruiser (3 spaces) (ie: A1 A2 A3): ").strip()
            coords = raw.upper().split()

            if self.player_board.place(self.player_cruiser,coords):
                return coords
                
            print("Invalid placement! Please try again")

    def player_submarine_placement(self):
        while True:
            raw = input("Enter the squares for the Submarine (2 spaces) (ie: B1 B2): ").strip()
            coords = raw.upper().split()

            if self.player_board.place(self.player_submarine,coords):
                return coords
                
            print("Invalid placement! Please try again")

    def _valid_player_shot(self, coord):
        if not self.cpu_board.is_valid_coordinate(coord):
            print("Invalid target coordinate")
            return False
        
        if self.cpu_board.cells[coord].is_fired_upon:
            print("You have already fired on this coordinate!")
            return False
    
    
    def player_shot(self):
        while True:
            coord = input("Enter the coordinates of the shot (ie: A1): ").strip().upper()

            if self._valid_player_shot(coord):
                self.cpu_board.cells[coord].fire_upon()
                return coord