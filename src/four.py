import copy


class FourState:

    def __init__(self):
        self.board = [
            [0 for row in range(6)]
            for col in range(7)
        ]
        self.to_move = 1
    
    def __str__(self):
        return str(self.board)


class FourGame:

    def initial_state(self):
        return FourState()

    def actions(self, state):
        actions = []
        for col in range(7):
            if state.board[col][0] == 0:
                actions.append((state.to_move, col))
        return actions

    def result(self, state, move):
        new_state = copy.deepcopy(state)
        first_empty_position = 0
        for row in range(6):
            if new_state.board[move[1]][row] == 0:
                first_empty_position = row
        new_state.board[move[1]][first_empty_position] = new_state.to_move
        new_state.to_move *= -1
        return new_state

    def is_terminal(self, state):
        return self.utility(state, self.get_player(state)) != 0 \
            or not self.actions(state)
    
    def utility(self, state, player):
        for col in range(7):
            for rd in range(3):
                v = sum(state.board[col][rd: rd + 4])
                if abs(v) == 4:
                    return player * v / 4
        for row in range(6):
            for cd in range(4):
                v = sum([state.board[col][row] for col in range(cd, cd+4)])
                if abs(v) == 4:
                    return player * v / 4
        for rd in range(3):
            for cd in range(4):
                v = sum(state.board[cd+p][rd+p] for p in range(4))
                if abs(v) == 4:
                    return player * v / 4
                v = sum(state.board[cd+p][rd+3-p] for p in range(4))
                if abs(v) == 4:
                    return player * v / 4
        return 0

    def get_player(self, state):
        return state.to_move
