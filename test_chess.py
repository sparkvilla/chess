import pytest
from chess import Chess
from board import Board
from position import Position

import pdb


@pytest.fixture
def game001():
    chess = Chess("./test_game_001.json5")
    return chess


@pytest.fixture
def game002():
    chess = Chess("./test_game_002.json5")
    return chess


@pytest.fixture
def game003():
    chess = Chess("./test_game_003.json5")
    return chess


@pytest.fixture
def game004():
    chess = Chess("./test_game_004.json5")
    return chess


# ******** GAME 1 *************************


def test_chess_last_move(game001):
    assert game001.board.last_move == "h4"


def test_chess_current_piece(game001):
    assert game001.piece.type_ == "queen"
    assert game001.piece.color == -1
    assert game001.piece.current.an == "h4"


def test_chess_wK_paths(game001):
    # get all positions from which the white king can be checked for this game
    assert game001.wK_paths == {
        "e1": [
            ["e2", "e3", "e4", "e5", "e6", "e7", "e8"],
            [],
            ["d1", "c1", "b1", "a1"],
            ["f1", "g1", "h1"],
            ["f2", "g3", "h4"],
            [],
            ["d2", "c3", "b4", "a5"],
            [],
            ["d3", "f3", "c2", "g2"],
        ]
    }


def test_bQ_positions(game001):
    # get available and edible positions for current piece -> bQ (it was the last move)
    assert game001.get_positions() == [
        "h5",
        "h6",
        "h7",
        "h8",
        "h3",
        "h2",
        "h1",
        "g4",
        "f4",
        "e4",
        "d4",
        "c4",
        "b4",
        "a4",
        "g3",
        "f2",
        "g5",
        "f6",
        "e7",
        "d8",
    ]


def test_wP_is_restricted(game001):
    game001.board.draw_board_state()
    # set current piece to wP in f2
    game001.set_piece_from_an("f2")
    assert game001.is_restricted() == True
    game001.restricted == []


# ******** GAME 2 *************************


def test_wQ_position(game002):
    game002.board.draw_board_state()
    # set current piece to wQ in f2
    game002.set_piece_from_an("f2")
    assert game002.get_positions() == [
        "f3",
        "f4",
        "f5",
        "f6",
        "f7",
        "f8",
        "e2",
        "g2",
        "h2",
        "g3",
        "h4",
        "e3",
        "d4",
        "c5",
        "b6",
        "a7",
        "g1",
    ]


def test_wQ_is_restricted(game002):
    game002.board.draw_board_state()
    # set current piece to wQ in f2
    game002.set_piece_from_an("f2")
    assert game002.is_restricted() == True
    assert "h4" and "g3" in game002.restricted


# ******** GAME 3 *************************


def test_wR_is_restricted(game003):
    game003.board.draw_board_state()
    # set current piece to wQ in f2
    game003.set_piece_from_an("e3")
    assert game003.is_restricted() == True
    assert "e2" and "e4" and "e5" and "e6" and "e7" in game003.restricted


# ******** GAME 4 *************************


def test_wQ_and_wP_are_restricted(game004):
    game004.board.draw_board_state()
    # set current piece to wQ in f2
    game004.set_piece_from_an("e3")
    assert game004.is_restricted() == True
    assert "e2" and "e4" and "e5" and "e6" and "e7" in game004.restricted
    game004.set_piece_from_an("d2")
    assert game004.is_restricted() == True
    assert game004.restricted == ["c3"]
