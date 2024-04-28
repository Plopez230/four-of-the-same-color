import random
import sys
import pygame
from pygame.locals import *

def play_game(game, strategies: dict, verbose=False):
    state = game.initial_state()
    while not game.is_terminal(state):
        player = state.to_move
        move = strategies[player](game, state)
        state = game.result(state, move)
        if verbose: 
            print('Player', player, 'move:', move)
            print(state)
    return state

def random_strategy(game, state):
    return random.choice(game.actions(state))


class GameGUI:

    def __init__(self):
        pass

    def draw_state(self, state):
        pass

    def gui_strategy(self, strategy):
        def inner(game, state):
            self.draw_state(state)
            action = strategy(game, state)
            self.draw_state(state)
            return action
        return inner

    def main(self, strategies):
        for s in strategies:
            strategies[s] = self.gui_strategy(strategies[s])
        init = self.game.initial_state()
        self.draw_state(init)
        end = play_game(self.game, strategies)
        self.draw_state(end)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
