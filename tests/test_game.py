import pytest
from battleship25.game import Game
from battleship25.board import Board

def test_game_inits():
    game = Game()

    assert isinstance(game.player_board, Board)
    assert isinstance(game.cpu_board, Board)
    assert game.player_board is not None
    assert game.cpu_board is not None