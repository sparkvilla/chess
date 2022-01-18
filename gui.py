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
COLOR_SCREEN = (217, 217, 217)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

board = Board()
chess = Chess(board)
avail_pos = None
edibl_pos = None


game_exit = False
while not game_exit:
    #x, y = pygame.mouse.get_pos()
    #print(f'{x, y}')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_start, y_start = event.pos
            if y_start >= 800:
                pass
            else:
                chess.set_piece_from_coords(x_start, y_start)
                print(f'object: {chess.piece}')
                avail_pos = chess.get_piece_avail_pos()
                print(avail_pos)
                edibl_pos = chess.get_piece_edible_pos()
                #print(edibl_pos)
        if event.type == pygame.MOUSEBUTTONUP:
            x_end, y_end = event.pos
            if y_end >= 800:
                pass
            else:
                an_end = board.get_an_from_mouse(x_end, y_end)
                print(an_end)
                # end position is non-empty
                if chess.get_piece_from_an(an_end):
                    chess.move_piece(edibl_pos, an_end)
                # end position is empty
                else:
                    chess.move_piece(avail_pos, an_end)
                avail_pos = None
                edibl_pos = None

    screen.fill(COLOR_SCREEN)
    board.draw_board(screen, avail_pos, edibl_pos)
    pygame.display.flip()
    clock.tick(30)
