import pytest
from chess import Chess
from board import Board
from position import Position

import pdb


@pytest.fixture
def chess():
    board = Board()
    chess = Chess(board)
    return chess


@pytest.fixture
def bQ_h3(chess):
    # place black Queen in h3
    chess.player = -1
    chess.set_piece_from_an("d8")
    chess.move_piece(["h3"], "h3")
    return chess


@pytest.fixture
def bQ_h4(chess):
    # place black Queen in h3
    chess.player = -1
    chess.set_piece_from_an("d8")
    chess.move_piece(["h4"], "h4")
    return chess


@pytest.fixture
def wP_h3(chess):
    # place white Pawn in h3
    chess.set_piece_from_an("h2")
    chess.move_piece(["h3"], "h3")
    return chess


@pytest.fixture
def wP_f3(chess):
    # place white Pawn in h3
    chess.set_piece_from_an("f2")
    chess.move_piece(["f3"], "f3")
    return chess


def test_pawn_get_positions(chess):
    chess.set_piece_from_an("g2")
    assert chess.get_positions() == ["g3", "g4"]
    assert chess.player == 1


def test_knight_get_positions(chess):
    chess.set_piece_from_an("b1")
    assert chess.player == 1
    assert chess.get_positions() == ["a3", "c3"]


def test_pawn_can_eat_queen_get_positions(bQ_h3):
    bQ_h3.set_piece_from_an("g2")
    assert bQ_h3.get_positions() == ["h3", "g3", "g4"]
    assert bQ_h3.player == 1


def test_w_knight_can_eat_b_queen_get_positions(bQ_h3):
    bQ_h3.set_piece_from_an("g1")
    assert bQ_h3.get_positions() == ["f3", "h3"]
    assert bQ_h3.player == 1


def test_w_knight_cannot_eat_w_pawn_get_positions(wP_h3):
    wP_h3.player = 1
    wP_h3.set_piece_from_an("g1")
    assert wP_h3.get_positions() == ["f3"]
    assert wP_h3.player == 1


def test_w_pawn_is_pinned(bQ_h4):
    bQ_h4.player = 1
    bQ_h4.set_piece_from_an("f2")
    assert bQ_h4.is_pinned() == True
    bQ_h4.board.draw_board_state()


def test_w_king_is_not_pinned(bQ_h4):
    bQ_h4.player = 1
    bQ_h4.set_piece_from_an("e1")
    assert bQ_h4.is_pinned() == False
    bQ_h4.board.draw_board_state()


def test_w_pawn_is_not_pinned_because_can_eat_the_queen(bQ_h4):
    bQ_h4.player = 1
    bQ_h4.set_piece_from_an("f2")
    bQ_h4.move_piece(["f3"], "f3")
    bQ_h4.player = 1
    bQ_h4.set_piece_from_an("g2")
    bQ_h4.move_piece(["g3"], "g3")
    bQ_h4.player = 1
    bQ_h4.set_piece_from_an("g3")
    assert bQ_h4.is_pinned() == False
    bQ_h4.board.draw_board_state()


def test_w_king_in_check(wP_f3):
    wP_f3.set_piece_from_an("d8")
    wP_f3.move_piece(["h4"], "h4")
    wP_f3.board.draw_board_state()
    assert wP_f3.is_check() == True


def test_w_king_in_check_get_uncheck(wP_f3):
    wP_f3.set_piece_from_an("d8")
    wP_f3.move_piece(["h4"], "h4")
    assert wP_f3.is_check() == True
    assert wP_f3.get_uncheck()[0].current.an == "g2"
    wP_f3.board.draw_board_state()


# @pytest.fixture
# def game(chess):
#    chess.set_piece_from_an("e2")
#    chess.move_piece(chess.get_piece_avail_pos(), "e3")
#
#    chess.set_piece_from_an("e7")
#    chess.move_piece(chess.get_piece_avail_pos(), "e6")
#
#    chess.set_piece_from_an("d2")
#    chess.move_piece(chess.get_piece_avail_pos(), "d4")
#
#    chess.set_piece_from_an("d8")
#    chess.move_piece(chess.get_piece_avail_pos(), "h4")
#
#    chess.set_piece_from_an("a2")
#    chess.move_piece(chess.get_piece_avail_pos(), "a3")
#
#    chess.set_piece_from_an("b8")
#    chess.move_piece(chess.get_piece_avail_pos(), "c6")
#
#    chess.set_piece_from_an("a3")
#    chess.move_piece(chess.get_piece_avail_pos(), "a4")
#
#    chess.set_piece_from_an("c6")
#    chess.move_piece(chess.get_piece_avail_pos(), "d4")
#
#    return chess


# def test_pawn_set_piece_an(chess):
#    chess.set_piece_from_an("d2")
#    assert chess.piece.current.an == "d2"
#    assert chess.piece.type_ == "pawn"
#    assert chess.piece.color == 1
#    assert chess.piece.image == "./imgs/pawn_w.png"
#
#
# def test_get_pawn_avail_pos(game):
#    game.set_piece_from_an("e3")
#    avail = game.get_piece_avail_pos()
#    assert avail == ["d4", "e4"]
#
#
# def test_get_queen_avail_pos(game):
#    game.set_piece_from_an("h4")
#    avail = game.get_piece_avail_pos()
#    assert avail == [
#        "h5",
#        "h6",
#        "h3",
#        "h2",
#        "g4",
#        "f4",
#        "e4",
#        "g3",
#        "f2",
#        "g5",
#        "f6",
#        "e7",
#        "d8",
#    ]
#
#
# def test_get_queen_avail_pos_non_set(game):
#    obj = game.board.get_obj_at_pos("h4")
#    avail = game.get_piece_avail_pos(obj)
#    assert avail == [
#        "h5",
#        "h6",
#        "h3",
#        "h2",
#        "g4",
#        "f4",
#        "e4",
#        "g3",
#        "f2",
#        "g5",
#        "f6",
#        "e7",
#        "d8",
#    ]
#
#
# def test_get_queen_avail_pos_non_set_ignore_pawn(game):
#    game.set_piece_from_an("f2")
#    obj = game.board.get_obj_at_pos("h4")
#    avail = game.get_piece_avail_pos(obj, game.piece.current.an)
#    assert avail == [
#        "h5",
#        "h6",
#        "h3",
#        "h2",
#        "g4",
#        "f4",
#        "e4",
#        "g3",
#        "f2",
#        "e1",
#        "g5",
#        "f6",
#        "e7",
#        "d8",
#    ]
#
#
# def test_is_pawn_pinned(game):
#    game.set_piece_from_an("f2")
#    assert game.is_piece_pinned() == True
#
#
# def test_is_king_checked(game):
#    game.board.draw_board_state()
#    game.set_piece_from_an("f2")
#    assert game.is_piece_pinned() == True
#
#
# def test_is_king_checked(game):
#    game.board.draw_board_state()
#    game.set_piece_from_an("f2")
#    assert game.is_piece_pinned() == True
