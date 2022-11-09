import pytest
from chess import Chess
from board import Board

import pdb

@pytest.fixture
def chess():
    board = Board()
    return Chess(board)


def test_set_piece_an(chess):
    # white pawn in d2
    chess.set_piece_from_an('d2')
    assert chess.piece.type_ == 'pawn' 
    assert chess.piece.color == 1  
    assert chess.piece.image == './imgs/pawn_w.png'

def test_get_piece_avail_pos(chess):
    chess.set_piece_from_an('d2')
    avail = chess.get_piece_avail_pos()
    assert avail == ['d3', 'd4']

def test_a_chess_game(chess):
    chess.set_piece_from_an('d2')
    assert chess.piece.type_ == 'pawn'
    assert chess.piece.color == 1
    chess.move_piece(chess.get_piece_avail_pos(), 'd4')

    chess.set_piece_from_an('e7')
    assert chess.piece.type_ == 'pawn'
    assert chess.piece.color == -1
    chess.move_piece(chess.get_piece_avail_pos(), 'e6')
    
    chess.set_piece_from_an('g2')
    chess.move_piece(chess.get_piece_avail_pos(), 'g3')

    chess.set_piece_from_an('d8')
    chess.move_piece(chess.get_piece_avail_pos(), 'f6')

    chess.set_piece_from_an('g1')
    chess.move_piece(chess.get_piece_avail_pos(), 'h3')

    chess.set_piece_from_an('f6')
    chess.move_piece(chess.get_piece_avail_pos(), 'f2')

    chess.board.draw_board_state()



