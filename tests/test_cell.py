import pytest
from battleship25.cell import Cell
from battleship25.ship import Ship

def test_cell_has_coordinate():
    cell = Cell("B4")
    assert cell.coordinate == "B4"
    assert cell.ship == None
    assert cell.empty == True

def test_cell_can_hold_ship():
    cruiser = Ship("Cruiser", 3)
    cell = Cell("B4")
    cell.place_ship(cruiser)
    assert cell.ship == cruiser
    assert cell.empty == False

