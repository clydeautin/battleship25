from battleship25.cell import Cell

class Board:
    def __init__(self):
        self.cells = {}
        self._generate_cells()

    #A leading underscore in Python means “this is internal, don’t call it from outside the class.”
    def _generate_cells(self):
        rows = ["A", "B", "C", "D"]
        cols = ["1", "2", "3", "4"]

        for row in rows:
            for col in cols:
                coord = f"{row}{col}"
                self.cells[coord] = Cell(coord)

    def is_valid_coordinate(self, coord: str) -> bool:
        return coord in self.cells
    
    def is_valid_placement(self, ship: object, placement: list[str]) -> bool:
        ship_n = ship.length
        placement_n = len(placement)
        if ship_n != placement_n:
            return False
        #checks if every coordinate in the placement array is valid on game board
        #check if a ship currently occupies one of the cells
        for x in placement:
            if self.is_valid_coordinate(x) is False:
                return False
            if self.cells[x].ship is not None:
                return False
        
        # need to determine if ship is place horizontally or vertically
        row_nums = []
        col_nums = []

        for x in placement:
            row_nums.append(ord(x[0]))
            col_nums.append(int(x[1:]))

        #determine orientation by converting row nums into a set to remove duplicates so that if all rows are the same we only get one value
        same_row = len(set(row_nums)) == 1
        same_col = len(set(col_nums)) == 1

        # horizontal: same row, columns consecutive
        if same_row and self._consecutive(col_nums):
            return True
        
        # vertical: same column, rows consecutive
        if same_col and self._consecutive(row_nums):
            return True
        
        return False

    def _consecutive(self, nums: list[int]) -> bool:
        nums = sorted(nums)

        for i in range(len(nums) - 1):
            current = nums[i]
            next_val = nums[i + 1]

            if next_val - current != 1:
                return False
        
        return True
    
    def place(self, ship: object, placement: list[str]):
        if self.is_valid_placement(ship, placement)  == False:
            return False
        
        for x in placement:
            self.cells[x].place_ship(ship)
        
        return True

    def render(self, reveal=False) -> str: 
        rows = ["A", "B", "C", "D"]
        cols = ["1", "2", "3", "4"]

        lines = []
        lines.append("  " + " ".join(cols))
        
        for row in rows:
            row_cells = []
            for col in cols:
                coord = f"{row}{col}"
                row_cells.append(self.cells[coord].render(reveal))
            lines.append(f"{row} " + " ".join(row_cells))
        
        return "\n".join(lines)