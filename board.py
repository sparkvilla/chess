import itertools
import sys
import pygame
from pygame.locals import *
from piece import Piece, King, Queen, Rook, Bishop, Knight, Pawn
import pdb

pygame.init()
COLOR_SCREEN = (217, 217, 217)

TILE_SIZE = 100
WIDTH, HEIGHT = 8 * TILE_SIZE, 8 * TILE_SIZE

COLOR1 = (238,238,210)
COLOR2 = (118,150,86)
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

BACKGROUND = pygame.Surface((WIDTH, HEIGHT))
colors = itertools.cycle((COLOR1, COLOR2))
text_font = pygame.font.SysFont(None, 26) # type -> 'pygame.font.Font'

class Board:

    NUMBERS_AN = ('8', '7', '6', '5', '4', '3', '2', '1')
    LETTERS_AN = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    COORDS = {}

    @classmethod
    def _gen_coordinates(cls):
        for row in range(8):
            for col in range(8):
                yield row, col

    @classmethod
    def init_coords(cls):
        for row, col in Board._gen_coordinates():
            Board.COORDS[Board.LETTERS_AN[col] + Board.NUMBERS_AN[row]] = row, col
            Board.COORDS[row,col] = Board.LETTERS_AN[col]+Board.NUMBERS_AN[row]

    def __init__(self):
        self.init_game()

    def init_game(self):
        self.state = [[0 for y in range(8)] for x in range(8)]
        self.state[7][4] = King('e1', 'white', './imgs/king_w.png')
        self.state[7][3] = Queen('d1', 'white', './imgs/queen_w.png')
        self.state[7][2] = Bishop('c1', 'white', './imgs/bishop_w.png')
        self.state[7][5] = Bishop('f1', 'white', './imgs/bishop_w.png')
        self.state[7][1] = Knight('b1', 'white', './imgs/knight_w.png')
        self.state[7][6] = Knight('g1', 'white', './imgs/knight_w.png')
        self.state[7][0] = Rook('b1', 'white', './imgs/rook_w.png')
        self.state[7][7] = Rook('g1', 'white', './imgs/rook_w.png')

        self.state[0][4] = King('e8', 'black', './imgs/king_b.png')
        self.state[0][3] = Queen('d8', 'black', './imgs/queen_b.png')
        self.state[0][2] = Bishop('c8', 'black', './imgs/bishop_b.png')
        self.state[0][5] = Bishop('f8', 'black', './imgs/bishop_b.png')
        self.state[0][1] = Knight('b8', 'black', './imgs/knight_b.png')
        self.state[0][6] = Knight('g8', 'black', './imgs/knight_b.png')
        self.state[0][0] = Rook('b8', 'black', './imgs/rook_b.png')
        self.state[0][7] = Rook('g8', 'black', './imgs/rook_b.png')
        for i in range(8):
            self.state[6][i] = Pawn(self.LETTERS_AN[i]+'2', 'white', './imgs/pawn_w.png')
            self.state[1][i] = Pawn(self.LETTERS_AN[i]+'7', 'black', './imgs/pawn_b.png')

    def get_obj_at_pos(self, an):
        row, col = self.COORDS.get(an)
        return self.state[row][col]

    def get_obj_from_mouse(self, row, col):
        row, col = row // 100, col// 100
        return self.state[col][row]

    def update_obj_at_pos(self, an, obj):
        row, col = self.COORDS.get(an)
        self.state[row][col] = obj

    def search_for_obj(self, type_, color):
        for row in self.state:
            for obj in row:
                if isinstance(obj, Piece):
                    if obj.type_ == type_ and obj.color == color:
                        return obj

    def draw_board(self, screen):
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
            text = text_font.render(LETTERS[l], True, (0, 0, 0)) # type -> 'pygame.Surface'
            text_area = text.get_rect() # type -> 'pygame.Rect'
            text_area.center = (x, 790)
            numbers.append((text, text_area))

        screen.fill(COLOR_SCREEN)
        for t, t_a in numbers:
            BACKGROUND.blit(t, t_a)
        for t1, t_a1 in letters:
            BACKGROUND.blit(t1, t_a1)

        for key, val in self.COORDS.items():
            if isinstance(key, str):
                obj = self.state[val[0]][val[1]]
                if isinstance(obj, Piece):
                    p_img = pygame.image.load(obj.image).convert_alpha()
                    p_img = pygame.transform.scale(p_img, (75, 75))
                    BACKGROUND.blit(p_img, (100*val[1]+15, 100*val[0]+20))

        screen.blit(BACKGROUND, (0, 0))

Board.init_coords()
