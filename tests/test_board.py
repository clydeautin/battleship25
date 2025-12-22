import pytest
from battleship25.cell import Cell
from battleship25.ship import Ship
from battleship25.board import Board

def test_board_has_cells():
    board = Board()
    assert len(board.cells) == 16
    assert type(board.cells) == dict
    assert "A1" in board.cells
    assert isinstance(board.cells["A1"], Cell)

def test_validating_coordinates():
    board = Board()
    assert board.is_valid_coordinate("A1") == True
    assert board.is_valid_coordinate("B4") == True
    assert board.is_valid_coordinate("Z9") == False
    assert board.is_valid_coordinate("C22") == False

def test_valid_placement():
    board = Board()
    cruiser = Ship("Cruiser", 3)
    submarine = Ship("Submarine", 2)
    # number of coordinates in the array should be the same as the length of the ship:
    assert board.is_valid_placement(cruiser, ["A1", "A2"]) == False
    assert board.is_valid_placement(submarine, ["A1", "A2", "A3"]) == False
    # check coordinates are consecutive
    assert board.is_valid_placement(cruiser, ["A1", "A2", "A4"]) == False
    assert board.is_valid_placement(submarine, ["A1", "C1"]) == False
    # coordinates are not diagonal
    assert board.is_valid_placement(cruiser, ["A1", "B2", "C3"]) == False
    assert board.is_valid_placement(submarine, ["C2", "D3"]) == False
    # If all the previous checks pass then the placement should be valid:
    assert board.is_valid_placement(cruiser, ["A1", "A2", "A3"]) == True
    assert board.is_valid_placement(submarine, ["C3", "D3"]) == True
