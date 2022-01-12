from collections import namedtuple
import pdb

Position = namedtuple('Position', 'pos_an')
pos = Position('a1')

class Piece:
    # Should be an abstract class

    NUMBERS_AN = ('1', '2', '3', '4', '5', '6', '7', '8')
    LETTERS_AN = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

    def __init__(self, position):
        self.counter = 0
        self.color = None
        self.current_pos = position
        self.new_pos = position

    def _is_valid_position(self, value):
        if len(value) != 2:
            return False
        if value[0] not in self.LETTERS_AN or value[1] not in self.NUMBERS_AN:
            return False
        return True

    @property
    def current_pos(self):
        return self._current_pos

    @current_pos.setter
    def current_pos(self, value):
        if self.counter == 0:
            assert self._is_valid_position(value), f"'{value}' is not a valid position!"
        # fill cursors
        self.curr_pos_let = self.LETTERS_AN.index(value[0])
        self.curr_pos_num = self.NUMBERS_AN.index(value[1])
        self._current_pos = value

    @property
    def new_pos(self):
        return self._new_pos

    @new_pos.setter
    def new_pos(self, value):
        assert self._is_valid_position(value), f"'{value}' is not a valid position!"
        # fill cursors
        self.new_pos_let = self.LETTERS_AN.index(value[0])
        self.new_pos_num = self.NUMBERS_AN.index(value[1])
        self._new_pos = value

    def right(self, steps):
        let = self.LETTERS_AN[self.curr_pos_let + steps]
        return let + self.current_pos[1]

    def left(self, steps):
        let = self.LETTERS_AN[self.curr_pos_let - steps]
        return let + self.current_pos[1]

    def up(self, steps):
        num = self.NUMBERS_AN[self.curr_pos_num + steps]
        return self.current_pos[0] + num

    def down(self, steps):
        num = self.NUMBERS_AN[self.curr_pos_num - steps]
        return self.current_pos[0] + num

    def diag_pos_down(self, steps):
        let = self.LETTERS_AN[self.curr_pos_let - steps]
        num = self.NUMBERS_AN[self.curr_pos_num - steps]
        return let + num

    def diag_pos_up(self, steps):
        let = self.LETTERS_AN[self.curr_pos_let + steps]
        num = self.NUMBERS_AN[self.curr_pos_num + steps]
        return let + num

    def diag_neg_down(self, steps):
        let = self.LETTERS_AN[self.curr_pos_let + steps]
        num = self.NUMBERS_AN[self.curr_pos_num - steps]
        return let + num

    def diag_neg_up(self, steps):
        let = self.LETTERS_AN[self.curr_pos_let - steps]
        num = self.NUMBERS_AN[self.curr_pos_num + steps]
        return let + num

    def is_right(self):
        return (self.curr_pos_let < self.new_pos_let) \
                and (self.curr_pos_num == self.new_pos_num)

    def is_left(self):
        return  (self.curr_pos_let > self.new_pos_let) \
                and (self.curr_pos_num == self.new_pos_num)

    def is_up(self):
        return (self.curr_pos_let == self.new_pos_let) \
                and (self.curr_pos_num < self.new_pos_num)

    def is_down(self):
        return (self.curr_pos_let == self.new_pos_let) \
               and (self.curr_pos_num > self.new_pos_num)

    def is_diagonal(self):
        return abs(self.curr_pos_let - self.new_pos_let) == \
               abs(self.curr_pos_num - self.new_pos_num)

    def is_diagonal_pos_up(self):

        return (self.curr_pos_let < self.new_pos_let) \
                and (self.curr_pos_num < self.new_pos_num)

    def is_diagonal_pos_down(self):

        return (self.curr_pos_let > self.new_pos_let) \
                and (self.curr_pos_num > self.new_pos_num)

    def is_diagonal_neg_up(self):

        return (self.curr_pos_let > self.new_pos_let) \
                and (self.curr_pos_num < self.new_pos_num)

    def is_diagonal_neg_down(self):

        return (self.curr_pos_let < self.new_pos_let) \
                and (self.curr_pos_num > self.new_pos_num)

    def is_l_down_rigth(self):
        return (self.curr_pos_let + 1  == self.new_pos_let) \
                and (self.curr_pos_num - 2 == self.new_pos_num)

    def is_l_down_left(self):
        return (self.curr_pos_let - 1  == self.new_pos_let) \
                and (self.curr_pos_num - 2 == self.new_pos_num)

    def is_l_left_up(self):
        return (self.curr_pos_let - 2  == self.new_pos_let) \
                and (self.curr_pos_num + 1 == self.new_pos_num)

    def is_l_left_down(self):
        return (self.curr_pos_let - 2  == self.new_pos_let) \
                and (self.curr_pos_num - 1 == self.new_pos_num)

    def is_l_up_rigth(self):
        return (self.curr_pos_let + 1  == self.new_pos_let) \
                and (self.curr_pos_num + 2 == self.new_pos_num)

    def is_l_up_left(self):
        return (self.curr_pos_let - 1  == self.new_pos_let) \
                and (self.curr_pos_num + 2 == self.new_pos_num)

    def is_l_right_up(self):
        return (self.curr_pos_let + 2  == self.new_pos_let) \
                and (self.curr_pos_num + 1 == self.new_pos_num)

    def is_l_right_down(self):
        return (self.curr_pos_let + 2  == self.new_pos_let) \
                and (self.curr_pos_num - 1 == self.new_pos_num)

    def squares_up(self, stop=True):
        """
        Return all positions expressed in algebric notation (an) along upward 
        direction between curr_pos and new_pos
        """

        new_pos = self.new_pos_num
        if not stop:
            new_pos = 7

        squares = []

        for step in range(1, (new_pos - self.curr_pos_num) + 1):
            squares.append(self.up(step))

        return squares

    def squares_down(self, stop=True):
        """
        Return all positions expressed in algebric notation (an) along downward 
        direction between curr_pos and new_pos
        """
        new_pos = self.new_pos_num
        if not stop:
            new_pos = 0

        squares = []

        for step in range(1, (self.curr_pos_num - new_pos) + 1):
            squares.append(self.down(step))

        return squares

    def squares_right(self, stop=True):
        """
        Return all positions expressed in algebric notation (an) to the right 
        of curr_pos between  new_pos and current_pos
        """

        new_pos = self.new_pos_let
        if not stop:
            new_pos = 7

        squares = []

        for step in range(1, (new_pos - self.curr_pos_let) + 1):
            squares.append(self.right(step))

        return squares

    def squares_left(self, stop=True):
        """
        Return all positions expressed in algebric notation (an) to the left 
        of curr_pos between new_pos and current_pos
        """

        new_pos = self.new_pos_let
        if not stop:
            new_pos = 0

        squares = []

        for step in range(1, (self.curr_pos_let - new_pos) + 1):
            squares.append(self.left(step))

        return squares

    def squares_diag_pos_up(self, stop=True):
        """
        Return all positions expressed in algebric notation (an) along the positive 
        diagonal in upword direction between curr_pos and new_pos
        """
        new_pos = self.new_pos_let
        if not stop:
            new_pos = 7

        squares = []

        for step in range(1, (new_pos - self.curr_pos_let) + 1):
            squares.append(self.diag_pos_up(step))

        return squares

    def squares_diag_pos_down(self, stop=True):
        """
        Return all positions expressed in algebric notation (an) along the positive 
        diagonal in downword direction between curr_pos and new_pos
        """
        new_pos = self.new_pos_num
        if not stop:
            new_pos = 0

        squares = []

        for step in range(1, (self.curr_pos_num - new_pos) + 1):
            squares.append(self.diag_pos_down(step))

        return squares

    def squares_diag_neg_up(self, stop=True):
        """
        Return all positions expressed in algebric notation (an) along the negative 
        diagonal in upword direction between curr_pos and new_pos
        """
        new_pos = self.new_pos_num
        if not stop:
            new_pos = 7

        squares = []

        for step in range(1, (new_pos - self.curr_pos_num) + 1):
            squares.append(self.diag_neg_up(step))

        return squares

    def squares_diag_neg_down(self, stop=True):
        """
        Return all positions expressed in algebric notation (an) along the negative 
        diagonal in downword direction between curr_pos and new_pos
        """
        new_pos = self.new_pos_num
        if not stop:
            new_pos = 0

        squares = []

        for step in range(1, (self.curr_pos_num - new_pos) + 1):
            squares.append(self.diag_neg_down(step))

        return squares

    def move(self):
        self.current_pos = self.new_pos
        self.counter += 1
        return self.current_pos

    def get_path(self):
        pass


class King(Piece):
    def __init__(self, position, color, image):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = 'king'

    def get_path(self):
        squares = None

        if self.is_diagonal():
            # along positive diag upward
            if self.is_diagonal_pos_up():
                squares = self.squares_diag_pos_up()
            # along positive diag downward
            elif self.is_diagonal_pos_down():
                squares = self.squares_diag_pos_down()
            # along negative diag upward
            elif self.is_diagonal_neg_up():
                squares = self.squares_diag_neg_up()
            # along negative diag downward
            elif self.is_diagonal_neg_down():
                squares = self.squares_diag_neg_down()
        elif self.is_up():
            squares = self.squares_up()
        elif self.is_down():
            squares = self.squares_down()
        elif self.is_left():
            squares = self.squares_left()
            # castling
            if len(squares) == 2 and self.counter == 0:
                return squares
        elif self.is_right():
            squares = self.squares_right()
            # castling
            if len(squares) == 2 and self.counter == 0:
                return squares

        if squares and len(squares) == 1: return squares

        print('not allowed')
        self.new_pos = self.current_pos


class Queen(Piece):
    def __init__(self, position, color, image):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = 'queen'

    def get_path(self):
        if self.is_diagonal():
            if self.is_diagonal_pos_up():
                squares = self.squares_diag_pos_up()
            elif self.is_diagonal_neg_up():
                squares = self.squares_diag_neg_up()
            elif self.is_diagonal_pos_down():
                squares = self.squares_diag_pos_down()
            elif self.is_diagonal_neg_down():
                squares = self.squares_diag_neg_down()
            return squares
        elif self.is_up():
            return self.squares_up()
        elif self.is_down():
            return self.squares_down()
        elif self.is_left():
            return self.squares_left()
        elif self.is_right():
            return self.squares_right()

        print('not allowed')
        self.new_pos = self.current_pos


class Rook(Piece):
    def __init__(self, position, color, image):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = 'rook'

    def get_path(self):
        if self.is_up():
            return self.squares_up()
        if self.is_down():
            return self.squares_down()
        if self.is_left():
            return self.squares_left()
        if self.is_right():
            return self.squares_right()

        print('not allowed')
        self.new_pos = self.current_pos


class Bishop(Piece):
    def __init__(self, position, color, image):
        super().__init__(position)
        self.color = color
        self.type_ = 'bishop'
        self.image = image

    def get_path(self):
        if self.is_diagonal():
            # along positive diag upward
            if self.is_diagonal_pos_up():
                return self.squares_diag_pos_up()
            # along positive diag downward
            if self.is_diagonal_pos_down():
                return self.squares_diag_pos_down()
            # along negative diag upward
            if self.is_diagonal_neg_up():
                return self.squares_diag_neg_up()
            # along negative diag downward
            if self.is_diagonal_neg_down():
                return self.squares_diag_neg_down()

        print('not allowed')
        self.new_pos = self.current_pos


class Pawn(Piece):
    def __init__(self, position, color, image):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = 'pawn'

    def get_path(self):
        squares = None

        if self.is_diagonal():
            if self.is_diagonal_pos_up() and self.color == 'white':
                squares = self.squares_diag_pos_up()
            elif self.is_diagonal_neg_up() and self.color == 'white':
                squares = self.squares_diag_neg_up()
            if self.is_diagonal_pos_down() and self.color == 'black':
                squares = self.squares_diag_pos_down()
            elif self.is_diagonal_neg_down() and self.color == 'black':
                squares = self.squares_diag_neg_down()
        elif self.is_up() and self.color== 'white':
            squares = self.squares_up()
            if len(squares) == 2 and self.counter == 0:
                return squares
        elif self.is_down() and self.color== 'black':
            squares = self.squares_down()
            if len(squares) == 2 and self.counter == 0:
                return squares

        if squares and len(squares) == 1: return squares

        print('not allowed')
        self.new_pos = self.current_pos


class Knight(Piece):
    def __init__(self, position, color, image):
        super().__init__(position)
        self.color = color
        self.image = image
        self.type_ = 'knight'

    def get_path(self):

        is_l = [self.is_l_down_left(), self.is_l_down_rigth(), self.is_l_left_up(), \
                self.is_l_left_down(), self.is_l_up_rigth(), self.is_l_up_left(), \
                self.is_l_right_up(), self.is_l_right_down()]

        if any(is_l):
            return [self.new_pos]

        print('not allowed')
        self.new_pos = self.current_pos

if __name__ == '__main__':

    k = Knight('d5', 'white')
    k.new_pos = 'e3'
    print(k.get_path())
    k.new_pos = 'c3'
    print(k.get_path())
    k.new_pos = 'b4'
    print(k.get_path())
    k.new_pos = 'b6'
    print(k.get_path())
    k.move()
    k.new_pos = 'd7'


#p = Pawn('a1', 'white')
#p.new_pos= 'a3'
#print(p.get_path())
#p.move()
#p.new_pos= 'b3'
#p.get_path()
#p.new_pos= 'b4'
#print(p.get_path())
#p.move()
#print(p.current_pos)

#q = Queen('e4', 'white')
#q.new_pos= 'f5'
#print(q.get_path())
#q.move()
#q.new_pos = 'c8'
#print(q.get_path())
#q.move()
#q.new_pos = 'h3'
#print(q.get_path())
#q.move()
#print(q.current_pos)
#q.new_pos = 'b3'
#print(q.get_path())
#q.move()
#print(q.current_pos)
