import pytest
from battleship25.cell import Cell
from battleship25.board import Board

def test_board_has_cells():
    board = Board()
    assert len(board.cells) == 16
    assert type(board.cells) == dict
    assert "A1" in board.cells
    assert isinstance(board.cells["A1"], Cell)

