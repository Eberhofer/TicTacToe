# import pyytest
from TicTacToe.game import Game
import TicTacToe.tictactoe as tictactoe
import pytest


class TestGame:

    def test_instatiate_game(self):
        g = Game()
        assert g.player1.winners == tictactoe.winners()
        assert g.player2.winners == tictactoe.winners()
        assert g.player1.state == set()
        assert g.player2.state == set()
        assert g.board_state == [' '] * 9

    def test_board_state_3586(self):
        g = Game()
        g.move(g.player1, 3)
        g.move(g.player1, 8)
        g.move(g.player2, 5)
        g.move(g.player2, 6)
        assert g.board_state == [' ', ' ', 'X',
                                 ' ', 'O', 'O',
                                 ' ', 'X', ' ']

    def test_move_updates_player_state(self):
        g = Game()
        g.move(g.player1, 5)
        assert g.player1.state == {5}

    def test_move_updates_opponent_winners(self):
        g = Game()
        g.move(g.player1, 5)
        assert g.player2.winners == [{1, 2, 3}, {7, 8, 9}, {1, 4, 7}, {3, 6, 9}]

    def test_move_playersamefield(self):
        g = Game()
        g.move(g.player1, 5)
        with pytest.raises(ValueError):
            g.move(g.player1, 5)

    def test_move_oppomnentsamefield(self):
        g = Game()
        g.move(g.player1, 5)
        with pytest.raises(ValueError):
            g.move(g.player2, 5)
