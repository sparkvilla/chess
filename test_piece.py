import pytest
from piece import Piece

import pdb

@pytest.fixture
def p_e4():
    return Piece('e4')

def test_curr_pos_eq_next_pos(p_e4):
    assert p_e4.current_pos == p_e4.new_pos

def test_cursors_curr_ex_new(p_e4):
    assert p_e4.new_pos_let == p_e4.curr_pos_let
    assert p_e4.new_pos_num == p_e4.curr_pos_num

def test_right_1step(p_e4):
    assert p_e4.right(1) == 'f4'

def test_right_2steps(p_e4):
    assert p_e4.right(2) == 'g4'

def test_left_3steps(p_e4):
    assert p_e4.left(3) == 'b4'

def test_diag_pos_up_2steps(p_e4):
    assert p_e4.diag_pos_up(2) == 'g6'

def test_diag_pos_down_3steps(p_e4):
    assert p_e4.diag_pos_down(3) == 'b1'

def test_diag_neg_up_2steps(p_e4):
    assert p_e4.diag_neg_up(2) == 'c6'

def test_diag_neg_down_3steps(p_e4):
    assert p_e4.diag_neg_down(3) == 'h1'

def test_diag_neg_down_3steps(p_e4):
    assert p_e4.diag_neg_down(3) == 'h1'

def test_assign_next_pos():
    p = Piece('a1')
    p.new_pos = 'd1'
    assert p.current_pos == 'a1'
    assert p.new_pos == 'd1'

def test_squares_up_pos():
    p = Piece('e4')
    p.new_pos = 'e6'
    assert p.squares_up() == ['e5', 'e6']

def test_squares_up_pos_no_stop():
    p = Piece('e4')
    assert p.squares_up(stop=False) == ['e5', 'e6', 'e7', 'e8']

def test_squares_diag_pos():
    p = Piece('e4')
    p.new_pos = 'h7'
    assert p.squares_diag_pos_up() == ['f5', 'g6', 'h7']
    p.new_pos = 'b1'
    assert p.squares_diag_pos_down() == ['d3', 'c2', 'b1']

def test_squares_diag_pos_no_stop():
    p = Piece('a1')
    p.new_pos = 'h8'
    assert p.squares_diag_pos_up(stop=False) == ['b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8']

def test_squares_diag_neg():
    p = Piece('e4')
    p.new_pos = 'a8'
    assert p.squares_diag_neg_up() == ['d5', 'c6', 'b7', 'a8']
    p.new_pos = 'h1'
    assert p.squares_diag_neg_down() == ['f3', 'g2', 'h1']
