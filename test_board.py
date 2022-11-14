import pytest
from chess import Chess
from board import Board

import pdb


@pytest.fixture
def board():
    board = Board()
    return board


def test_board_get_obj_at_pos(board):
    obj = board.get_obj_at_pos("d1")
    assert obj.type_ == "queen"
    assert obj.color == 1
