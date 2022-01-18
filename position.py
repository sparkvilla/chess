import pdb

class Position:

    NUMBERS_AN = ('8', '7', '6', '5', '4', '3', '2', '1')
    LETTERS_AN = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

    MAPPING = {}

    @classmethod
    def _gen_coordinates(cls):
        for y in range(8):
            for x in range(8):
                yield x, y

    @classmethod
    def init(cls):
        for x, y in Position._gen_coordinates():
            Position.MAPPING[Position.LETTERS_AN[x]
                             + Position.NUMBERS_AN[y]] = x, y
            Position.MAPPING[x, y] = Position.LETTERS_AN[x] \
                                        + Position.NUMBERS_AN[y]
    def __init__(self, an):
        self.an = an

    @classmethod
    def _is_valid_an(cls, value):
        if len(value) != 2:
            return False
        if value[0] not in cls.LETTERS_AN or value[1] not in cls.NUMBERS_AN:
            return False
        return True

    @classmethod
    def _is_valid_coord(cls, value):
        if not isinstance(value, tuple) and len(value) == 2:
            return False
        range_ = range(0, 9)
        if value[0] not in range_  or value[1] not in range_:
            return False
        return True

    @property
    def an(self):
        return self._an

    @an.setter
    def an(self, value):
        assert self._is_valid_an(value), f"'{value}' is not a valid position!"
        self.x = Position.MAPPING.get(value)[0]
        self.y = Position.MAPPING.get(value)[1]
        self._an = value

    @classmethod
    def to_an(cls, coord):
        assert cls._is_valid_coord(coord), f"'{coord}' not valid coortdinates!"
        return cls.MAPPING.get(coord)

    @classmethod
    def to_coord(cls, an):
        assert cls._is_valid_an(an), f"'{an}' not valid algebric notation!"
        return cls.MAPPING.get(an)

    @classmethod
    def from_coord(cls, coord):
        assert cls._is_valid_coord(coord), f"'{coord}' not valid coortdinates!"
        return Position(cls.MAPPING.get(coord))

    def get_up_pos(self, steps=None, pos=None):
        """
        Return coordinates in upward direction from the current position (excluded)
        to the position found after a number of steps. If steps is None goes until
        the end position.

        """
        stop = 0
        pos_start = self
        pos_up = []

        if pos:
            pos_start = pos

        if steps:
            stop = pos_start.y - steps
            if stop < 0:
                return pos_up
        for new_y in range(pos_start.y-1, stop-1, -1):
            pos_up.append(self.to_an((pos_start.x , new_y)))
        return pos_up

    def get_down_pos(self, steps=None, pos=None):
        """
        Return coordinates in upward direction from the current position (excluded)
        to the position found after a number of steps. If steps is None goes until
        the end position.

        """
        stop = 7
        pos_start = self
        pos_down = []

        if pos:
            pos_start = pos

        if steps:
            stop = pos_start.y + steps
            if stop > 7:
                return pos_down
        for new_y in range(pos_start.y+1, stop+1):
            pos_down.append(self.to_an((pos_start.x , new_y)))
        return pos_down

    def get_left_pos(self, steps=None, pos=None):
        """
        Return coordinates in upward direction from the current position (excluded)
        to the position found after a number of steps. If steps is None goes until
        the end position.

        """
        stop = 0
        pos_start = self
        pos_left = []

        if pos:
            pos_start = pos

        if steps:
            stop = pos_start.x - steps
            if stop < 0:
                return pos_left
        for new_x in range(pos_start.x-1, stop-1, -1):
            pos_left.append(self.to_an((new_x, pos_start.y)))
        return pos_left

    def get_right_pos(self, steps=None, pos=None):
        """
        Return coordinates in upward direction from the current position (excluded)
        to the position found after a number of steps. If steps is None goes until
        the end position.

        """
        stop = 7
        pos_start = self
        pos_right = []

        if pos:
            pos_start = pos

        if steps:
            stop = pos_start.x + steps
            if stop > 7:
                return pos_right
        for new_x in range(pos_start.x+1, stop+1):
            pos_right.append(self.to_an((new_x, pos_start.y)))
        return pos_right

    def get_diag_p_up_pos(self, steps=None, pos=None):
        """
        Return coordinates in upward direction from the current position (excluded)
        to the position found after a number of steps. If steps is None goes until
        the end position.

        """
        stop_x = 7
        stop_y = 0
        pos_start = self
        pos_diag_p_up = []

        if pos:
            pos_start = pos

        if steps:
            stop_x = pos_start.x + steps
            stop_y = pos_start.y - steps
            if stop_x > 7 or stop_y < 0:
                return pos_diag_p_up

        range_x = range(pos_start.x+1, stop_x+1)
        range_y = range(pos_start.y-1, stop_y-1, -1)

        for new_x, new_y in zip(range_x, range_y):
            pos_diag_p_up.append(self.to_an((new_x, new_y)))
        return pos_diag_p_up

    def get_diag_p_down_pos(self, steps=None, pos=None):
        """
        Return coordinates in upward direction from the current position (excluded)
        to the position found after a number of steps. If steps is None goes until
        the end position.

        """
        stop_x = 0
        stop_y = 7
        pos_start = self
        pos_diag_p_down = []

        if pos:
            pos_start = pos

        if steps:
            stop_x = pos_start.x - steps
            stop_y = pos_start.y + steps
            if stop_x < 0 or stop_y > 7:
                return pos_diag_p_down

        range_x = range(pos_start.x-1, stop_x-1, -1)
        range_y = range(pos_start.y+1, stop_y+1)

        for new_x, new_y in zip(range_x, range_y):
            pos_diag_p_down.append(self.to_an((new_x, new_y)))
        return pos_diag_p_down

    def get_diag_n_up_pos(self, steps=None, pos=None):
        """
        Return coordinates in upward direction from the current position (excluded)
        to the position found after a number of steps. If steps is None goes until
        the end position.

        """
        stop_x = 0
        stop_y = 0
        pos_start = self
        pos_diag_n_up = []

        if pos:
            pos_start = pos

        if steps:
            stop_x = pos_start.x - steps
            stop_y = pos_start.y - steps
            if stop_x < 0 or stop_y < 0:
                return pos_diag_n_up

        range_x = range(pos_start.x-1, stop_x-1, -1)
        range_y = range(pos_start.y-1, stop_y-1, -1)

        for new_x, new_y in zip(range_x, range_y):
            pos_diag_n_up.append(self.to_an((new_x, new_y)))
        return pos_diag_n_up

    def get_diag_n_down_pos(self, steps=None, pos=None):
        """
        Return coordinates in upward direction from the current position (excluded)
        to the position found after a number of steps. If steps is None goes until
        the end position.

        """
        stop_x = 7
        stop_y = 7
        pos_start = self
        pos_diag_n_down = []

        if pos:
            pos_start = pos

        if steps:
            stop_x = pos_start.x + steps
            stop_y = pos_start.y + steps
            if stop_x > 7 or stop_y > 7:
                return pos_diag_n_down

        range_x = range(pos_start.x+1, stop_x+1)
        range_y = range(pos_start.y+1, stop_y+1)

        for new_x, new_y in zip(range_x, range_y):
            pos_diag_n_down.append(self.to_an((new_x, new_y)))
        return pos_diag_n_down

    def get_l_pos(self, pos=None):
        """
        Return coordinates in upward direction from the current position (excluded)
        to the position found after a number of steps. If steps is None goes until
        the end position.

        """
        pos_start = self
        pos_l = []

        if pos:
            pos_start = pos

        l_down_left = pos_start.x - 1, pos_start.y + 2
        l_down_right = pos_start.x + 1, pos_start.y + 2
        l_up_left = pos_start.x - 1, pos_start.y - 2
        l_up_right = pos_start.x + 1, pos_start.y - 2
        l_left_up = pos_start.x - 2, pos_start.y - 1
        l_left_down = pos_start.x - 2, pos_start.y + 1
        l_right_up = pos_start.x + 2, pos_start.y - 1
        l_right_down = pos_start.x + 2, pos_start.y + 1

        l_coords = [l_down_left, l_down_right, l_up_left, l_up_right, l_left_up,
                    l_left_down, l_right_up, l_right_down]

        for new_x, new_y in l_coords:
            if not 0 <= new_x <= 7 or not 0 <= new_y <= 7:
                continue
            pos_l.append(self.to_an((new_x, new_y)))
        return pos_l

Position.init()


if __name__ == '__main__':
    p = Position('d5')
    print(p.get_l_pos())
