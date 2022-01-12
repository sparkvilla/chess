import itertools
import sys
import pygame
from pygame.locals import *

from board import Board
from chess import Chess

import pdb

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

board = Board()
chess = Chess(board)

game_exit = False
while not game_exit:
    x, y = pygame.mouse.get_pos()
    print(f'{x, y}')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_start, y_start = event.pos
            if y_start >= 800:
                pass
            else:
                obj_s = chess.get_obj_from_coords(x_start, y_start)
                print(f'object: {obj_s}')
        if event.type == pygame.MOUSEBUTTONUP:
            x_end, y_end = event.pos
            if y_end >= 800:
                pass
            else:
                obj_e = chess.get_obj_from_coords(x_end, y_end)
                print(f'object: {obj_e}')
                pos_end = chess.get_an(x_end, y_end)
                chess.move(obj_s, obj_e, pos_end)

    chess.draw_board(screen)
    pygame.display.flip()
    clock.tick(30)
