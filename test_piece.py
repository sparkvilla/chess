from piece import *


def test_king_get_moves():
    wK = King(Position("e1"), 1)
    assert wK.get_moves() == [["e2"], [], ["d1"], ["f1"], ["f2"], [], ["d2"], []]


def test_king_check():
    wK = King(Position("e1"), 1)
    assert wK.check() == [
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


def test_king_check_at_new_pos():
    wK = King(Position("e1"), 1)
    assert wK.check(Position("e2")) == [
        ["e3", "e4", "e5", "e6", "e7", "e8"],
        ["e1"],
        ["d2", "c2", "b2", "a2"],
        ["f2", "g2", "h2"],
        ["f3", "g4", "h5"],
        ["d1"],
        ["d3", "c4", "b5", "a6"],
        ["f1"],
        ["d4", "f4", "c3", "c1", "g3", "g1"],
    ]


def test_pawn_get_moves():
    wP = Pawn(Position("e2"), 1)
    assert wP.get_moves() == [["e3", "e4"]]


def test_pawn_get_edibles():
    wP = Pawn(Position("e2"), 1)
    assert wP.get_edibles() == [
        ["f3"],
        ["d3"],
    ]


def test_bishop_get_moves():
    wB = Bishop(Position("e2"), 1)
    assert wB.get_moves() == [
        ["f3", "g4", "h5"],
        ["d1"],
        ["d3", "c4", "b5", "a6"],
        ["f1"],
    ]


def test_knight_get_moves():
    wT = Knight(Position("b1"), 1)
    assert wT.get_moves() == [["a3", "c3", "d2"]]


def test_rook_get_moves():
    wR = Rook(Position("a1"), 1)
    assert wR.get_moves() == [
        ["a2", "a3", "a4", "a5", "a6", "a7", "a8"],
        [],
        [],
        ["b1", "c1", "d1", "e1", "f1", "g1", "h1"],
    ]


def test_queen_get_moves():
    wR = Queen(Position("d1"), 1)
    assert wR.get_moves() == [
        ["d2", "d3", "d4", "d5", "d6", "d7", "d8"],
        [],
        ["c1", "b1", "a1"],
        ["e1", "f1", "g1", "h1"],
        ["e2", "f3", "g4", "h5"],
        [],
        ["c2", "b3", "a4"],
        [],
    ]
