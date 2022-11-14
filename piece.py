from position import Position


class Piece:
    def __init__(self, position):
        self.counter = 0
        self.color = None
        self.current = position

    def get_moves(self):
        # This should be replaced with notImplemented error
        pass

    def move(self, pos_an):
        self.current.an = pos_an
        self.counter += 1


class King(Piece):
    def __init__(self, position, color, image=None):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = "king"

    def get_moves(self):
        moves = []
        allowed = [
            self.current.get_up_pos,
            self.current.get_down_pos,
            self.current.get_left_pos,
            self.current.get_right_pos,
            self.current.get_diag_p_up_pos,
            self.current.get_diag_p_down_pos,
            self.current.get_diag_n_up_pos,
            self.current.get_diag_n_down_pos,
        ]
        for move in allowed:
            moves.append(move(1))
        return moves

    def check(self, new_pos=None):
        """
        All potential positions that can check the king if positioned in a new_pos
        """
        directions = []
        allowed = [
            self.current.get_up_pos,
            self.current.get_down_pos,
            self.current.get_left_pos,
            self.current.get_right_pos,
            self.current.get_diag_p_up_pos,
            self.current.get_diag_p_down_pos,
            self.current.get_diag_n_up_pos,
            self.current.get_diag_n_down_pos,
            self.current.get_l_pos,
        ]

        for move in allowed:
            directions.append(move(pos=new_pos))
        return directions


class Queen(Piece):
    def __init__(self, position, color, image=None):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = "queen"

    def get_moves(self):
        moves = []
        allowed = [
            self.current.get_up_pos,
            self.current.get_down_pos,
            self.current.get_left_pos,
            self.current.get_right_pos,
            self.current.get_diag_p_up_pos,
            self.current.get_diag_p_down_pos,
            self.current.get_diag_n_up_pos,
            self.current.get_diag_n_down_pos,
        ]
        for move in allowed:
            moves.append(move())
        return moves


class Rook(Piece):
    def __init__(self, position, color, image=None):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = "rook"

    def get_moves(self):
        moves = []
        allowed = [
            self.current.get_up_pos,
            self.current.get_down_pos,
            self.current.get_left_pos,
            self.current.get_right_pos,
        ]
        for move in allowed:
            moves.append(move())
        return moves


class Bishop(Piece):
    def __init__(self, position, color, image=None):
        super().__init__(position)
        self.color = color
        self.type_ = "bishop"
        self.image = image

    def get_moves(self):
        moves = []
        allowed = [
            self.current.get_diag_p_up_pos,
            self.current.get_diag_p_down_pos,
            self.current.get_diag_n_up_pos,
            self.current.get_diag_n_down_pos,
        ]
        for move in allowed:
            moves.append(move())
        return moves


class Pawn(Piece):
    def __init__(self, position, color, image=None):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = "pawn"

    def get_moves(self):
        moves = []
        allowed_white = [self.current.get_up_pos]

        allowed_black = [self.current.get_down_pos]

        allowed = allowed_white if self.color == 1 else allowed_black

        for move in allowed:
            if self.counter == 0:
                moves.append(move(2))
            else:
                moves.append(move(1))
        return moves

    def get_edibles(self):
        moves = []

        allowed_to_eat_white = [
            self.current.get_diag_p_up_pos,
            self.current.get_diag_n_up_pos,
        ]

        allowed_to_eat_black = [
            self.current.get_diag_p_down_pos,
            self.current.get_diag_n_down_pos,
        ]

        allowed = allowed_to_eat_white if self.color == 1 else allowed_to_eat_black

        for move in allowed:
            moves.append(move(1))
        return moves


class Knight(Piece):
    def __init__(self, position, color, image=None):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = "knight"

    def get_moves(self):

        return [self.current.get_l_pos()]


if __name__ == "__main__":
    wK = King(Position("e1"), 1, "img")
    print(wK.get_moves())
    print(wK.check(Position("e2")))
    print(wK.counter)
