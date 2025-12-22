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
