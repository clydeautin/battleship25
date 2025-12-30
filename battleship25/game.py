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
        self.cpu_cruiser = Ship("Cruiser", 2)

    def cpu_cruiser_placement(num_of_coords):
            board_cells = ["A1", "A2", "A3", "A4",
                            "B1", "B2", "B3", "B4",
                            "C1", "C2", "C3", "C4",
                            "D1", "D2", "D3", "D4"]
            