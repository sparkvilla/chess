import pdb

from board import Board
from piece import King, Piece
from position import Position


class Chess:
    def __init__(self, board):
        self.board = board
        self.piece = None
        self.check = None
        self.player = 1
        self._initialize_kings_positions()

    def _initialize_kings_positions(self):
        wK = King(Position("e1"), 1)
        self.wK_paths = {wK.current.an: wK.check()}
        bK = King(Position("e8"), -1)
        self.bK_paths = {bK.current.an: bK.check()}

    def set_player(self, player):
        self.player = player

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

    @classmethod
    def _is_same_color(cls, obj_middle, obj):
        return isinstance(obj_middle, Piece) and obj_middle.color == obj.color

    @classmethod
    def _is_different_color(cls, obj_middle, obj):
        return isinstance(obj_middle, Piece) and obj_middle.color != obj.color

    def is_pinned(self):
        """
        Return True if a piece is pinned; i.e. it cannot move because covering a check
        """

        if self.player == 1:
            king = self.wK_paths
        elif self.player == -1:
            king = self.bK_paths

        for paths in king.values():
            for path in paths:
                if self.piece.current.an in path:
                    # check whether on this path there is a piece that can check the king
                    for pos_an in path:
                        obj_middle = self.board.get_obj_at_pos(pos_an)
                        if obj_middle and obj_middle.color != self.piece.color:
                            moves_obj_middle = self.get_positions(
                                obj_middle, self.piece.current.an
                            )
                            if [k for k in king.keys()][0] in moves_obj_middle:
                                if not obj_middle.current.an in self.get_positions():
                                    return True
        return False

    def _cut_path(self, path, piece):

        idx = path.index(piece.current.an)
        return path[: idx + 1]

    def is_check(self):
        if self.player == 1:
            king = self.wK_paths
        elif self.player == -1:
            king = self.bK_paths

        for paths in king.values():
            for path in paths:
                if self.piece.current.an in path:
                    moves = self.get_positions()
                    king_pos_an = [k for k in king.keys()][0]
                    if king_pos_an in moves:
                        self.check = {
                            "king_pos_an": king_pos_an,
                            "path": self._cut_path(path, self.piece),
                            "threat": self.piece,
                        }
                        return True
        return False

    def get_uncheck(self):

        selection = []

        color = self.player

        king = self.board.get_obj_at_pos(self.check["king_pos_an"])
        for pos_an in self.get_positions(king):
            if pos_an not in self.check["path"]:
                selection.append(king)

        for row in self.board.state:
            for piece in row:
                if isinstance(piece, Piece) and piece.color == color and piece != king:
                    positions = self.get_positions(piece)
                    for pos_an in positions:
                        if pos_an in self.check["path"]:
                            selection.append(piece)
        return selection

    def get_positions(self, piece=None, ignore_piece=None):
        """
        Return a list of available positions (an) for piece.

        If not specified, piece is the current set piece -> self.piece

        """
        if piece:
            piece = piece
        else:
            piece = self.piece

        obj_ignore = None
        if ignore_piece:
            obj_ignore = self.board.get_obj_at_pos(ignore_piece)
        moves = []

        if not piece:
            return moves

        # handle special case pawn
        if piece.type_ == "pawn":
            for path in piece.get_edibles():
                for pos_an in path:
                    obj_middle = self.board.get_obj_at_pos(pos_an)
                    if obj_middle and self._is_different_color(obj_middle, piece):
                        moves.append(pos_an)

        for path in piece.get_moves():
            for pos_an in path:
                obj_middle = self.board.get_obj_at_pos(pos_an)
                if not obj_middle or obj_middle == obj_ignore:
                    moves.append(pos_an)
                elif self._is_same_color(obj_middle, piece):
                    if piece.type_ == "knight":
                        continue
                    else:
                        break
                elif self._is_different_color(obj_middle, piece):
                    if piece.type_ == "pawn":
                        continue
                    else:
                        moves.append(pos_an)
                    break

        return moves

    def get_avail_and_edibl(self, positions):
        avail = []
        edibl = []
        for pos_an in positions:
            obj = self.board.get_obj_at_pos(pos_an)
            if isinstance(obj, Piece):
                edibl.append(pos_an)
            else:
                avail.append(pos_an)
        return avail, edibl

    def move_piece(self, moves, pos_end):
        if pos_end in moves:
            self.board.update_obj_at_pos(self.piece, pos_end)
            self.board.update_obj_at_pos(0, self.piece.current.an)
            self.piece.move(pos_end)
            self.player *= -1
        return self.player


if __name__ == "__main__":
    board = Board()
    chess = Chess(board)
    chess.set_piece_from_an("d1")
    print(chess.piece)
    print(chess.get_piece_avail_pos())
