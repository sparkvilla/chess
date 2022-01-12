from piece import Piece
from board import Board

class Chess:
    
    def __init__(self, board):
         self.board = board
         self.player = None
         self.current_piece = None
         self.new_position = None

    def get_obj_from_coords(self, x, y):
        """
        This uses the gui chessboard coords ref system
        """
        return self.board.get_obj_from_mouse(x, y)

    def get_obj_from_an(self, an):
        return self.board.get_obj_at_pos(an)

    def get_an(self, x, y):
        """
        This uses the internal chessboard coords ref system
        """
        return self.board.COORDS[y//100, x//100]

    def get_coords(self, an):
        return self.board.COORDS[an]

    def get_obj_middle(self, path):
        obj_middle = None
        for pos in path:
            obj_middle = self.get_obj_from_an(pos)
            if isinstance(obj_middle, Piece): 
                break
        return obj_middle

    def king_check(self, color):

        # get the king obj
        obj_king = self.board.search_for_obj('king', color)

        checkers = []

        for an in obj_king.squares_up(stop=False):
            obj = self.get_obj_from_an()
            if obj.color == color:
                break
            checkers.append(obj)

    def move(self, obj_start, obj_end, pos_end):
        # if player select empty square
        if not obj_start:
            print(self.board.state)
            return
        pos_start = obj_start.current_pos 
        # if end position is empty
        if obj_end == 0:
            obj_start.new_pos = pos_end
            path = obj_start.get_path()
            if not path:
                return
            else:
                if not self.get_obj_middle(path):
                    obj_start.move()
                    self.board.update_obj_at_pos(pos_end, obj_start)
                    self.board.update_obj_at_pos(pos_start, 0)
                    print(self.board.state)
        # if end position has piece of different color (eat it!)
        elif isinstance(obj_end, Piece) and obj_start.color != obj_end.color:
            obj_start.new_pos = pos_end
            path = obj_start.get_path()
            if not path:
                return
            else:
                print(pos_end)
                obj_middle = self.get_obj_middle(path)
                if not obj_middle or obj_middle.current_pos == pos_end:
                    obj_start.move()
                    print(path)
                    self.board.update_obj_at_pos(pos_end, obj_start)
                    self.board.update_obj_at_pos(pos_start, 0)
                    print(self.board.state)


    def draw_board(self, screen):
        return self.board.draw_board(screen)


board = Board()
chess = Chess(board)
