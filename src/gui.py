import pygame
from pygame.locals import *
import sys
from four import FourGame
from game import GameGUI


class FourGUI(GameGUI):

    def __init__(self):
        pygame.display.set_mode((50 * 7, 50 * 6), 0, 32)
        pygame.display.set_caption("Four of the same color")
        self.game = FourGame()

    def human(self, game, state):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    action = (
                        game.get_player(state), 
                        int(pos[0] / 50)
                        )
                    if state.board[action[1]][0] == 0:
                        return action

    def draw_state(self, state):
        for row in range(6):
            for col in range(7):
                color = (200, 200, 200)
                value = state.board[col][row]
                if value == -1:
                    color = (255, 0, 0)
                if value == 1:
                    color = (0, 0, 255)
                size = 50
                pygame.draw.circle(
                    pygame.display.get_surface(),
                    color,
                    (col * size + size / 2, row * size + size / 2),
                    size / 2.1
                )
        pygame.display.update()
