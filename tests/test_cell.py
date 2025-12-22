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

def test_cell_can_tell_its_fired_upon():
    cell = Cell("B4")
    cruiser = Ship("Cruiser", 3)
    cell.place_ship(cruiser)
    assert cell.is_fired_upon == False
    cell.fire_upon()
    assert cell.ship.health == 2
    assert cell.is_fired_upon == True

def test_cell_render_state():
    cell_1 = Cell("B4")
    assert cell_1.render() == "."
    cell_1.fire_upon()
    assert cell_1.render() == "M"

def test_cell_render_with_ship():
    cell_2 = Cell("C3")
    cruiser = Ship("Cruiser", 3)
    cell_2.place_ship(cruiser)
    assert cell_2.render() == "."
    assert cell_2.render(True) == "S"
    cell_2.fire_upon()
    assert cell_2.render() == "H"
    cruiser.hit()
    cruiser.hit()
    assert cruiser.sunk() == True
    assert cell_2.render() == "X"
