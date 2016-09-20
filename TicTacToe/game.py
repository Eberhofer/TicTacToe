"""
    game.py - the Game class
    ------------------------
"""
import TicTacToe.tictactoe as tictactoe
from TicTacToe.player import Player

class Game:
    """"
        Defines a TicTacToe game with an AI opponent.
    """

    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self._board = [_ for _ in range(1, 10)]
        self._game_sequence = []

    @property
    def board_state(self):
        def set_field(p1, p2, i):
            return 'X' if i in p1 else 'O' if i in p2 else ' '
        return [set_field(self.player1.state, self.player2.state, _)
                for _ in range(1, 10)]

    def move(self, player, field_number):
        opponent = self.player2 if self.player1 == player else self.player1
        if field_number in opponent.state:
            raise ValueError("Field already occupied by opponent.")
        if field_number in player.state:
            raise ValueError("Field already occupied by player.")
        self._board.remove(field_number)
        self._game_sequence.append(field_number)
        player.play_field(field_number)
        opponent.reduce_winners(player.state)
