import random
from bke import *

class MySmartAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        getal = 1
        if can_win(board, my_symbol):
            getal += 3
        if board[4] == my_symbol:
            getal += 2 
        if is_winner(board, my_symbol):
            getal = 10
        elif can_win(board, opponent_symbol):
            getal = -10
        return getal

class MyRandomAgent(EvaluationAgent):
    def evaluate(self, board, my_symbol, opponent_symbol):
        return random.randint(1, 500)

my_random_agent = MyRandomAgent()
my_smart_agent = MySmartAgent ()
start(player_o=my_smart_agent, player_x=my_random_agent)


