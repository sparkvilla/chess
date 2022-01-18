from piece import Piece
from board import Board

class Chess:

    def __init__(self, board):
         self.board = board
         self.player = None
         self.piece = None

    def get_piece_from_coords(self, x, y):
        """
        Get the object at coordinates (x, y) using the pygame
        positioning system and set it to piece

        x: int
           x coordinate from 0 to 8000
        y: int
           y coordinate from 0 to 8000

        """
        return self.board.get_obj_from_mouse(x, y)

    def set_piece_from_coords(self, x, y):
        """
        Get the object at coordinates (x, y) using the pygame
        positioning system and set it to piece

        x: int
           x coordinate from 0 to 8000
        y: int
           y coordinate from 0 to 8000

        """
        self.piece = self.get_piece_from_coords(x, y)

    def get_piece_from_an(self, an):
        """
        Get the object using algebraic notation and set it to piece

        an: str
           e.g. 'a1', 'd5' etc..
        """
        return self.board.get_obj_at_pos(an)

    def set_piece_from_an(self, an):
        """
        Get the object using algebraic notation and set it to piece

        an: str
           e.g. 'a1', 'd5' etc..
        """
        self.piece = self.get_piece_from_an(an)


    def get_piece_avail_pos(self):
        avail = []
        if not self.piece:
            return avail
        for path in self.piece.get_moves():
            print(path)
            for pos_an in path:
                obj_middle = self.board.get_obj_at_pos(pos_an)
                if obj_middle == 0:
                    avail.append(pos_an)
                else:
                    break
        return avail

    def get_piece_edible_pos(self):
        edibles = []
        if not self.piece:
            return edibles
        for path in self.piece.get_moves():
            for pos_an in path:
                obj_middle = self.board.get_obj_at_pos(pos_an)
                if isinstance(obj_middle, Piece) and obj_middle.color == self.piece.color:
                    break
                if isinstance(obj_middle, Piece) and obj_middle.color != self.piece.color:
                    edibles.append(pos_an)
                    break
        return edibles

    def move_piece(self, pos, pos_end):
        if pos_end in pos:
            self.board.update_obj_at_pos(self.piece, pos_end)
            self.board.update_obj_at_pos(0, self.piece.current.an)
            self.piece.move(pos_end)


if __name__ == '__main__':
    board = Board()
    chess = Chess(board)
    chess.get_piece_from_an('d1')
    print(chess.piece)
    print(chess.get_piece_avail_pos())
    chess.get_piece_from_an('d7')
    print(chess.piece)
    print(chess.get_piece_avail_pos())
    chess.get_piece_from_an('d8')
    print(chess.piece)
    print(chess.get_piece_avail_pos())
    chess.get_piece_from_an('d6')
    print(chess.piece)
    print(chess.get_piece_avail_pos())
