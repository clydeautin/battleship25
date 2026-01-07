from battleship25.board import Board
from battleship25.ship import Ship
import random

class Game:
    def __init__(self):
        self.player_board = Board()
        self.player_submarine = Ship("Submarine", 2)
        self.player_cruiser = Ship("Cruiser", 3)
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
        return True
    
    
    def player_shot(self):
        while True:
            coord = input("Enter the coordinates of the shot (ie: A1): ").strip().upper()

            if self._valid_player_shot(coord):
                self.cpu_board.cells[coord].fire_upon()
                return coord
 
            
    def cpu_shot(self):
        all_coordinates = self.player_board.cells.keys()

        unhit_coords = [
            coord
            for coord in all_coordinates
            if not self.player_board.cells[coord].is_fired_upon
        ]

        target = random.choice(unhit_coords)
        self.player_board.cells[target].fire_upon()
        return target

    def player_turn_result(self, coord: str) -> str:
        cell = self.cpu_board.cells[coord]

        if cell.ship is None:
            return f"Your shot on {coord} was a miss"
        
        if cell.ship.sunk():
            return f"Your hit on {coord} sunk the enemy {cell.ship.name}.!"
        
        return f"Your shot on {coord} was a hit!"
    
    def cpu_turn_result(self, coord: str) -> str:
        cell = self.player_board.cells[coord]

        if cell.ship is None:
            return f"CPU fired on {coord} and missed"
        
        if cell.ship.sunk():
            return f"CPU hit {coord} and sunk your {cell.ship.name}!"
        
        return f"CPU fired on {coord} and hit your {cell.ship.name}"
    
    def full_turn(self):
        while self.player_cruiser.health > 0 and self.player_submarine.health > 0 or self.cpu_cruiser.health > 0 and self.cpu_submarine.health > 0:
            print("=============COMPUTER BOARD============= \n")
            print(self.cpu_board.render())
            
            print("=============PLAYER BOARD============= \n")
            print(self.player_board.render(True))

            player_shot_coords = self.player_shot()
            cpu_shot_coords = self.cpu_shot()

            self.player_turn_result(player_shot_coords)
            self.cpu_turn_result(cpu_shot_coords)

        if self.player_cruiser.health == 0 and self.player_submarine.health == 0:
            print("computer win!")
        elif self.cpu_cruiser.health == 0 and self.cpu_submarine.health == 0:
            print("player win!")

    def start(self):
        print("Welcome to the Battleship Game!")

        start_answer = input('Enter p to play. Enter q to quit.').strip().upper()

        if start_answer == 'P':
            self.play()
        else:
            print('Thanks for playing!')

    def play(self):
        
        self.cpu_placement()

        print(
            "I have laid out my ships on the grid .\n"
            "You now need ot lay out your two ships on the grid.\n"
            "The Cruiser is three units long and the Submarine is two units long.\n"
        )
        print(self.player_board.render(reveal=True))

        self.player_cruiser_placement()

        self.player_submarine_placement()

        self.full_turn()

        return