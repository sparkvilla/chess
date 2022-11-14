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
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()

chess = Chess("./test_game_005.json5")
positions = None
avail = None
edibl = None

game_exit = False
while not game_exit:
    chess.is_check()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x_start, y_start = event.pos
            if y_start >= 800:
                pass
            else:
                chess.set_piece_from_coords(x_start, y_start)
                print(f"object: {chess.piece}")
                print(f"player: {chess.player}")

                if chess.piece == 0 or chess.piece.color != chess.player:
                    print("not allowed")
                    continue

                positions = chess.get_positions()

                if chess.is_restricted():
                    print("restricted")
                    positions = chess.restricted

                if chess.check and chess.piece.type_ != "king":
                    print("check")
                    chess.get_uncheck()
                    positions = chess.restricted

                avail, edibl = chess.get_avail_and_edibl(positions)

                print(f"avail: {avail}")
                print(f"edibl: {edibl}")
        if event.type == pygame.MOUSEBUTTONUP:
            x_end, y_end = event.pos
            if y_end >= 800:
                pass
            else:
                if chess.piece == 0 or chess.piece.color != chess.player:
                    print("not allowed")
                    continue
                an_end = chess.board.get_an_from_mouse(x_end, y_end)
                chess.move_piece(positions, an_end)

                avail = None
                edibl = None

    screen.fill(COLOR_SCREEN)
    chess.board.draw_board(screen, avail, edibl)
    pygame.display.flip()
    clock.tick(30)
