import pdb

from board import Board
from piece import King, Piece
from position import Position


class Chess:
    def __init__(self, game="./default_game.json5"):
        self.game = game
        self.board = Board(game)
        if self.board.last_move:
            self.set_piece_from_an(self.board.last_move)
        else:
            self.piece = None
        self.check = None
        self.restricted = None
        self.player = 1
        self._initialize_kings_positions()

    def _initialize_kings_positions(self):
        wK = self.board.search_unique_obj("king", 1)
        self.wK_paths = {wK.current.an: wK.check()}
        bK = self.board.search_unique_obj("king", -1)
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

    def is_restricted(self):
        """
        Return True if the current piece has restricted moves because covering a self-check or if
        the current piece is a king that may step on a checked position

        If True it fills the 'restricted' attribute with the possible moves.
        """

        if self.player == 1:
            king = self.wK_paths
        elif self.player == -1:
            king = self.bK_paths

        if self.piece.type_ == "king":
            checked = []
            # get king positions
            positions = self.get_positions()
            for pos_an in positions:
                king_paths = self.piece.check(Position(pos_an))
                for king_path in king_paths:
                    for king_pos_an in king_path:
                        obj = self.board.get_obj_at_pos(king_pos_an)
                        if obj and obj.color != self.piece.color:
                            moves_obj = self.get_positions(obj)
                            if pos_an in moves_obj:
                                checked.append(pos_an)
            restricted = set(positions) - set(checked)
            if restricted:
                self.restricted = list(restricted)
                return True

        else:

            for king_paths in king.values():
                for king_path in king_paths:
                    if self.piece.current.an in king_path:
                        # check whether on this path there is a piece (obj) that can check the king
                        for king_pos_an in king_path:
                            obj = self.board.get_obj_at_pos(king_pos_an)
                            if obj and obj.color != self.piece.color:
                                moves_obj = self.get_positions(
                                    obj, self.piece.current.an
                                )
                                if [k for k in king.keys()][0] in moves_obj:

                                    # If the piece (obj) that can check the king cannot be eaten by the current piece
                                    if not obj.current.an in self.get_positions():
                                        self.restricted = []
                                    # If the piece (obj) that can check the king can be eaten by the current piece
                                    else:
                                        new_king_path = self._cut_path(king_path, obj)
                                        restricted = set(new_king_path) - set(
                                            [self.piece.current.an]
                                        )
                                        self.restricted = list(restricted)
                                    return True
        return False

    def _cut_path(self, path, piece):

        idx = path.index(piece.current.an)
        return path[: idx + 1]

    def is_check(self):
        if self.player == -1:
            king = self.bK_paths
        elif self.player == 1:
            king = self.wK_paths

        for paths in king.values():
            for path in paths:
                if self.piece and self.piece.current.an in path:
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

        color = self.player

        import pdb

        king = self.board.get_obj_at_pos(self.check["king_pos_an"])
        threat_positions = self.get_positions(self.check["threat"])
        threat_current_pos = self.check["threat"].current.an

        restricted = []
        if self.piece.type_ == "king":

            for pos_an in self.get_positions(king):
                if pos_an not in threat_positions or pos_an == threat_current_pos:
                    restricted.append(pos_an)
        else:

            if (
                isinstance(self.piece, Piece)
                and self.piece.color == color
                and self.piece != king
            ):
                positions = self.get_positions()
                for pos_an in positions:
                    if pos_an in self.check["path"]:
                        restricted.append(pos_an)

        self.restricted = restricted

    def get_positions(self, piece=None, ignore_piece=None):
        """
        Return a set of available and edibles positions (an) for piece.
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
            if self.restricted:
                self.restricted = None
            if self.check and self.piece.type_ == "king":
                self._initialize_kings_positions()
                self.check = None
            self.player *= -1
        return self.player


if __name__ == "__main__":
    board = Board()
    chess = Chess(board)
    chess.set_piece_from_an("d1")
    print(chess.piece)
    print(chess.get_piece_avail_pos())
