import random
import math


class MCTSNode:

    def __init__(self, exploration, game, state, parent=None, action=None):
        self.exploration = exploration
        self.game = game
        self.state = state
        self.parent = parent
        self.action = action
        self.children = []
        self.actions = game.actions(state)
        self.visit = 0
        self.utility = 0

    def criterion(self, child):
        Q = 1 - ((child.utility / child.visit) + 1) / 2
        return Q + self.exploration * math.sqrt(
            math.log(self.visit) / child.visit
            )

    def is_expanded(self):
        return len(self.actions) == 0 and len(self.children) > 0
    
    def select(self):
        best_child = None
        best_criterion = - math.inf
        for child in self.children:
            criterion = self.criterion(child)
            if criterion > best_criterion:
                best_child = child
                best_criterion = criterion
        return best_child

    def expand(self):
        action = random.choice(self.actions)
        self.actions.remove(action)
        child_state = self.game.result(self.state, action)
        child = MCTSNode(
            self.exploration, self.game, child_state, self, action
            )
        self.children.append(child)
        return child
    
    def simulate(self):
        utility = self.game.utility(self.state, self.state.to_move)
        is_terminal = self.game.is_terminal(self.state)
        if is_terminal:
            return utility
        state = self.state
        while True:
            action = random.choice(self.game.actions(state))
            state = self.game.result(state, action)
            utility = self.game.utility(state, state.to_move)
            is_terminal = self.game.is_terminal(state)
            if is_terminal:
                return utility
            
    def backpropagate(self, utility):
        self.utility += utility
        self.visit += 1
        if self.parent is not None:
            self.parent.backpropagate(-utility)  


def search(exploration, game, state, iterations):
    root = MCTSNode(exploration, game, state, None, None)
    for _ in range(iterations):
        node = root
        while node.is_expanded():
            node = node.select()
        utility = game.utility(node.state, node.state.to_move)
        is_terminal = game.is_terminal(node.state)
        if not is_terminal:
            node = node.expand()
            utility = node.simulate()
        node.backpropagate(utility)
    return [
        (child.action, child.visit / root.visit) 
        for child in root.children
    ]

def mcts_strategy(exploration, iterations):
    def mcts(game, state):
        probabilities = search(exploration, game, state, iterations)
        most_probable = max(probabilities, key = lambda x: x[1])
        return most_probable[0]
    return mcts
