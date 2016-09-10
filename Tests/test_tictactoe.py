# import pyytest
from TicTacToe import tictactoe

def test_winners():
    testwinners = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
    assert tictactoe.winners() == testwinners

def test_check_win_empty():
    p1 = set()
    assert tictactoe.check_win(p1) == False

def test_check_win_loser():
    p1 = {0,1,3,5,7,8}
    assert tictactoe.check_win(p1) == False


def test_check_win_winner():
    p1 = {0,1,3,5,6,8}
    assert tictactoe.check_win(p1) == True
