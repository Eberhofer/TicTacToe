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
        """
            Alters the state for the player to add the played field_number.
        """
        self._state.add(field_number)

    def reduce_winners(self, opponent_state):
        """
            Recalculates the remaining set of winners based on the opponent_state.
        """
        self._winners = tictactoe.reduce_winners(self._winners, opponent_state)

    @property
    def winners(self):
        """
            Returns the set of winners for the player.
        """
        return self._winners

    @property
    def state(self):
        """
            Returns the state, i.e. the set of field_numbers played,
            for the player.
        """
        return self._state

    @property
    def is_winner(self):
        """
            Returns True, if the player has a winning combination and False
            otherwise.
        """
        return tictactoe.check_win(self._state)
