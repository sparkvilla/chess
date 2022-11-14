import itertools
import sys
import pygame
from pygame.locals import *
from position import Position
from piece import Piece, King, Queen, Rook, Bishop, Knight, Pawn
import pdb

pygame.init()

TILE_SIZE = 100
WIDTH, HEIGHT = 8 * TILE_SIZE, 8 * TILE_SIZE

COLOR_GRAY = (169,169,169)
COLOR_YELLOW = (255,255,51)
COLOR1 = (238,238,210)
COLOR2 = (118,150,86)

BACKGROUND = pygame.Surface((WIDTH, HEIGHT))
colors = itertools.cycle((COLOR1, COLOR2))
text_font = pygame.font.SysFont(None, 26) # type -> 'pygame.font.Font'

class Board:

    def __init__(self):
        self.init_board()

    def init_board(self):
        self.state = [[0 for y in range(8)] for x in range(8)]
        self.state[7][4] = King(Position('e1'), 1, './imgs/king_w.png')
        self.state[7][3] = Queen(Position('d1'), 1, './imgs/queen_w.png')
        self.state[7][2] = Bishop(Position('c1'), 1, './imgs/bishop_w.png')
        self.state[7][5] = Bishop(Position('f1'), 1, './imgs/bishop_w.png')
        self.state[7][1] = Knight(Position('b1'), 1, './imgs/knight_w.png')
        self.state[7][6] = Knight(Position('g1'), 1, './imgs/knight_w.png')
        self.state[7][0] = Rook(Position('a1'), 1, './imgs/rook_w.png')
        self.state[7][7] = Rook(Position('h1'), 1, './imgs/rook_w.png')

        self.state[0][4] = King(Position('e8'), -1, './imgs/king_b.png')
        self.state[0][3] = Queen(Position('d8'), -1, './imgs/queen_b.png')
        self.state[0][2] = Bishop(Position('c8'), -1, './imgs/bishop_b.png')
        self.state[0][5] = Bishop(Position('f8'), -1, './imgs/bishop_b.png')
        self.state[0][1] = Knight(Position('b8'), -1, './imgs/knight_b.png')
        self.state[0][6] = Knight(Position('g8'), -1, './imgs/knight_b.png')
        self.state[0][0] = Rook(Position('a8'), -1, './imgs/rook_b.png')
        self.state[0][7] = Rook(Position('h8'), -1, './imgs/rook_b.png')
        for i in range(8):
            self.state[6][i] = Pawn(Position(Position.LETTERS_AN[i]+'2'), 1, './imgs/pawn_w.png')
            self.state[1][i] = Pawn(Position(Position.LETTERS_AN[i]+'7'), -1, './imgs/pawn_b.png')

    def get_obj_at_pos(self, an):
        """
        Get object from board using algebraic notation
        """
        x, y = Position.MAPPING.get(an)
        return self.state[y][x]

    def get_obj_from_mouse(self, x, y):
        """
        Get object from board using pygame positioning coords
        """
        x, y = x // 100, y// 100
        return self.state[y][x]

    def get_an_from_mouse(self, x, y):
        """
        Get position in algebraic notation from pygame positioning system
        """
        x, y = x // 100, y// 100
        return Position.to_an((x, y))

    def update_obj_at_pos(self, obj, an):
        """
        Update board state setting an object at position using
        algebraic notation
        """
        x, y = Position.MAPPING.get(an)
        self.state[y][x] = obj

    def search_unique_obj(self, type_, color):
        """
        Search unique objects (type_ must be King or Queen) in the board

        """
        for row in self.state:
            for obj in row:
                if isinstance(obj, Piece):
                    if obj.type_ == type_ and obj.color == color:
                        return obj

    def draw_layout(self, screen):
        for y in range(0, HEIGHT, TILE_SIZE):
            for x in range(0, WIDTH, TILE_SIZE):
                rect = (x, y, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(BACKGROUND, next(colors), rect)
            next(colors)

        numbers = []
        for n,y in enumerate(range(790, 0 , -TILE_SIZE), 1):
            text = text_font.render(str(n), True, (0, 0, 0)) # type -> 'pygame.Surface'
            text_area = text.get_rect() # type -> 'pygame.Rect'
            text_area.center = (5, y)
            numbers.append((text, text_area))
        letters = []
        for l,x in enumerate(range(15, 800 , TILE_SIZE)):
            text = text_font.render(Position.LETTERS_AN[l], True, (0, 0, 0)) # type -> 'pygame.Surface'
            text_area = text.get_rect() # type -> 'pygame.Rect'
            text_area.center = (x, 790)
            numbers.append((text, text_area))

        for t, t_a in numbers:
            BACKGROUND.blit(t, t_a)
        for t1, t_a1 in letters:
            BACKGROUND.blit(t1, t_a1)

    def draw_pieces(self):
        for key, val in Position.MAPPING.items():
            if isinstance(key, str):
                obj = self.state[val[0]][val[1]]
                if isinstance(obj, Piece):
                    p_img = pygame.image.load(obj.image).convert_alpha()
                    p_img = pygame.transform.scale(p_img, (75, 75))
                    BACKGROUND.blit(p_img, (100*val[1]+15, 100*val[0]+20))

    def draw_avail_pos(self, ans):
        ans = [Position.to_coord(an) for an in ans]
        rects = []
        for x, y in ans:
            pygame.draw.circle(BACKGROUND, COLOR_GRAY, (100*x+52,100*y+52), 10)

    def draw_edibl_pos(self, ans):
        ans = [Position.to_coord(an) for an in ans]
        rects = []
        for x, y in ans:
            pygame.draw.rect(BACKGROUND, COLOR_YELLOW, pygame.Rect(100*x, 100*y, 100, 100), 4)

    def draw_board(self, screen, avail=None, edibl=None):
        self.draw_layout(screen)
        if avail:
            self.draw_avail_pos(avail)
        if edibl:
            self.draw_edibl_pos(edibl)
        self.draw_pieces()
        screen.blit(BACKGROUND, (0, 0))
    
    def _extract(self, obj):
        
        if isinstance(obj, int):
            return '--'
        
        if obj.color == 1:
            color = 'w'
        elif obj.color == -1:
            color = 'b'
        
        if obj.type_ == "king":
            return color+"K"
        elif obj.type_ == "queen":
            return color+"Q"
        elif obj.type_ == "knight":
            return color+"T"
        elif obj.type_ == "rook":
            return color+"R"
        elif obj.type_ == "bishop":
            return color+"B"
        elif obj.type_ == "pawn":
            return color+"P"

    def draw_board_state(self):
        print(f"""
        8 {[self._extract(p) for p in self.state[0]]}
        7 {[self._extract(p) for p in self.state[1]]}
        6 {[self._extract(p) for p in self.state[2]]}
        5 {[self._extract(p) for p in self.state[3]]}
        4 {[self._extract(p) for p in self.state[4]]}
        3 {[self._extract(p) for p in self.state[5]]}
        2 {[self._extract(p) for p in self.state[6]]}
        1 {[self._extract(p) for p in self.state[7]]}
             a     b     c     d     e     f     g     h  
        """)


if __name__ == '__main__':
    board= Board()
    board.draw_board_state() 
    #qw = board.search_unique_obj('queen','white')

    #qw = board.get_obj_at_pos('d1')
    #print(qw.get_moves())
    #qw.move('e2')
    #print(qw.get_moves())
    #rw = board.get_obj_at_pos('a1')
    #print(rw.get_moves())
