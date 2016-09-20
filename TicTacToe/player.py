"""
    player.py - the Player class
    ------------------------
"""
import TicTacToe.tictactoe as tictactoe

class Player:
    """"
        Defines a TicTacToe game with an AI opponent.
    """

    def __init__(self):
        self._winners = tictactoe.winners()
        self._state = set()

    def play_field(self, field_number):
        self._state.add(field_number)

    def reduce_winners(self, opponent_state):
        self._winners = tictactoe.reduce_winners(self._winners, opponent_state)

    @property
    def winners(self):
        return self._winners

    @property
    def state(self):
        return self._state

    @property
    def is_winner(self):
        return tictactoe.check_win(self._state)
