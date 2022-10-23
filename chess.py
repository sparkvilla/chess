from piece import Piece
from board import Board
from position import Position
import pdb

class Chess:

    def __init__(self, board):
         self.board = board
         self.player = 1
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

    def _is_middle_same_color(self, obj_middle):
        return isinstance(obj_middle, Piece) and obj_middle.color == self.piece.color

    def _is_middle_different_color(self, obj_middle):
        return isinstance(obj_middle, Piece) and obj_middle.color != self.piece.color

    def get_piece_avail_pos(self):
        avail = []
        if not self.piece:
            return avail

        if self.piece.type_ == 'knight':
            for pos_an in self.piece.get_moves():
                obj_middle = self.board.get_obj_at_pos(pos_an)
                if self._is_middle_same_color(obj_middle):
                    continue
                avail.append(pos_an)
            return avail

        for path in self.piece.get_moves():
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

        if self.piece.type_ == 'knight':
            for pos_an in self.piece.get_moves():
                obj_middle = self.board.get_obj_at_pos(pos_an)
                if self._is_middle_same_color(obj_middle):
                    continue
                if self._is_middle_different_color(obj_middle):
                    edibles.append(pos_an)
            return edibles

        if self.piece.type_ == 'pawn':
            for path in self.piece.get_edibles():
                for pos_an in path:
                    obj_middle = self.board.get_obj_at_pos(pos_an)
                    if obj_middle and self._is_middle_different_color(obj_middle):
                        edibles.append(pos_an)
            return edibles

        for path in self.piece.get_moves():
            for pos_an in path:
                obj_middle = self.board.get_obj_at_pos(pos_an)
                if self._is_middle_same_color(obj_middle):
                    break
                if self._is_middle_different_color(obj_middle):
                    edibles.append(pos_an)
                    break
        return edibles

    def look_for_auto_check(self, obj_to_move):
        king = self.board.search_unique_obj('king', obj_to_move.color)

        paths = []

        for path in king.check():
            #print(path)
            for pos_an in path:
                obj_middle = self.board.get_obj_at_pos(pos_an)
                if obj_middle in (0, obj_to_move):
                    continue
                if obj_middle.color == king.color and obj_middle != obj_to_move:
                    break

                # look whether a pawn can check the king
                if obj_middle.type_ == 'pawn' and obj_middle.color != king.color:
                    for pt in obj_middle.get_edibles():
                        for pt_pos in pt:
                            if king.current.an == pt_pos:
                                paths.append(pt)

                # look whether this object can check the king
                elif isinstance(obj_middle, Piece) and obj_middle.color != king.color:
                    for pt in obj_middle.get_moves():
                        for pt_pos in pt:
                            if king.current.an == pt_pos:
                                paths.append(pt)
        return paths

    def look_for_check(self, avail):
        
        paths = []

        for pos in avail:
            for path in self.piece.check(Position(pos)):
                print(path)
                for pos_an in path:
                    obj_middle = self.board.get_obj_at_pos(pos_an)
                    if obj_middle == 0:
                        continue
                    if obj_middle.color == self.piece.color:
                        break
                    # look whether a pawn can check the king
                    if obj_middle.type_ == 'pawn' and obj_middle.color != self.piece.color:
                        for pt in obj_middle.get_edibles():
                            for pt_pos in pt:
                                if pos == pt_pos:
                                    paths.append(pt)

                    # look whether a knight can check the king
                    elif obj_middle.type_ == 'knight' and obj_middle.color != self.piece.color:
                        print(f'If king move to {pos} will be checked by {obj_middle.type_}')
                        print(f'found {pos_an}')
                        paths.append([pos])

                    # look whether this object can check the king
                    elif isinstance(obj_middle, Piece) and obj_middle.color != self.piece.color:
                        for pt in obj_middle.get_moves():
                            for pt_pos in pt:
                                if pos == pt_pos:
                                    print(f'If king move to {pos} will be checked by {obj_middle.type_}')
                                    print(f'found {pos}')
                                    paths.append(pt)

        return paths

    def move_piece(self, pos, pos_end):
        if pos_end in pos:
            self.board.update_obj_at_pos(self.piece, pos_end)
            self.board.update_obj_at_pos(0, self.piece.current.an)
            self.piece.move(pos_end)
            self.player *= -1
        return self.player    


if __name__ == '__main__':
    board = Board()
    chess = Chess(board)
    chess.set_piece_from_an('d1')
    print(chess.piece)
    print(chess.get_piece_avail_pos())
