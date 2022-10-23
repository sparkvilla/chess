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
current_player = 1 # white
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
                if chess.piece == 0 or chess.piece.color != current_player:
                    continue

                avail_pos = chess.get_piece_avail_pos()
                edibl_pos = chess.get_piece_edible_pos()
                print(f'avail0: {avail_pos}')
                print(f'edibl0: {edibl_pos}')
                auto_check_paths = chess.look_for_auto_check(chess.piece)
                print(f'auto_check: {auto_check_paths}')

                if chess.piece.type_ == 'king':
                    avail_pos_check = []
                    edibl_pos_check = []
                    check_paths = chess.look_for_check(avail_pos)
                    if check_paths:
                        print(check_paths)
                        for ck_path in check_paths:
                            avail_pos_check.extend(list(set(avail_pos) - set(ck_path)))
                            edibl_pos_check.extend(list(set(edibl_pos).intersection(ck_path)))

                        avail_pos = avail_pos_check
                        edibl_pos = edibl_pos_check

                else:
                    if auto_check_paths:
                        avail_pos_autocheck = []
                        edibl_pos_autocheck = []
                        if chess.piece.type_ != 'king':
                            for ck_path in auto_check_paths:
                                avail_pos_autocheck.extend(list(set(avail_pos).intersection(ck_path)))
                                edibl_pos_autocheck.extend(list(set(edibl_pos).intersection(ck_path)))
                        else:
                            for ck_path in auto_check_paths:
                                print(ck_path)
                                avail_pos_autocheck.extend(list(set(avail_pos) - set(ck_path)))
                                edibl_pos_autocheck.extend(list(set(edibl_pos).intersection(ck_path)))

                        avail_pos = avail_pos_autocheck
                        edibl_pos = edibl_pos_autocheck

                    #avail_pos = [i in avail_pos if i not in check_path]
                    #print(edibl_pos)
                    # look for potential aouto-check when moving the current piece
                print(f'avail1: {avail_pos}')
                print(f'edibl1: {edibl_pos}')

        if event.type == pygame.MOUSEBUTTONUP:
            x_end, y_end = event.pos
            if y_end >= 800:
                pass
            else:
                an_end = board.get_an_from_mouse(x_end, y_end)
                # end position is non-empty
                if chess.get_piece_from_an(an_end) and edibl_pos:
                    current_player = chess.move_piece(edibl_pos, an_end)
                # end position is empty
                elif avail_pos:
                    current_player = chess.move_piece(avail_pos, an_end)

                avail_pos = None
                edibl_pos = None

                print(current_player)

    screen.fill(COLOR_SCREEN)
    board.draw_board(screen, avail_pos, edibl_pos)
    pygame.display.flip()
    clock.tick(30)
