"""
    game.py - the Game class
    ------------------------
"""
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
        """
            Returns the board state as a list of ' ', 'X' and 'O'.
        """
        def set_field(p1state, p2state, field_number):
            """
                Returns the character for field with field_number based on the
                states players 1 and 2 (p1state and p2state).
            """
            return 'X' if field_number in p1state else \
                'O' if field_number in p2state else ' '
        return [set_field(self.player1.state, self.player2.state, _)
                for _ in range(1, 10)]

    def move(self, player, field_number):
        """
            Defines the move for a player to play field with field_number.
            There are a few intentional side effects: move updates the opponent's
            winner. (??? IS THIS A GOOD IDEA? ???)
        """
        opponent = self.player2 if self.player1 == player else self.player1
        if field_number in opponent.state:
            raise ValueError("Field already occupied by opponent.")
        if field_number in player.state:
            raise ValueError("Field already occupied by player.")
        self._board.remove(field_number)
        self._game_sequence.append(field_number)
        player.play_field(field_number)
        opponent.reduce_winners(player.state)
