from gui import FourGUI
from mcts import mcts_strategy

if __name__ == '__main__':
    game = FourGUI()
    game.main({
        1: game.human,
        -1: mcts_strategy(1.4, 2000)
        })
