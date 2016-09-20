# import pyytest
from TicTacToe.player import Player, tictactoe

class TestPlayer:

    def test_instatiate_game(self):
        p = Player()
        assert p.winners == tictactoe.winners()
        assert p.state == set()

    def test_play_field_number_761(self):
        p = Player()
        assert p.state == set()
        p.play_field(7)
        assert p.state == {7}
        p.play_field(6)
        assert p.state == {6, 7}
        p.play_field(1)
        assert p.state == {1, 6, 7}

    def test_reduce_winners_5(self):
        p = Player()
        p.reduce_winners({5})
        assert p.winners == [{1, 2, 3}, {7, 8, 9}, {1, 4, 7}, {3, 6, 9}]
