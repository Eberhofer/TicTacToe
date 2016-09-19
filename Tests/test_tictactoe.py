# import pyytest
from TicTacToe.tictactoe import winners, check_win, winning_combinations
from TicTacToe.tictactoe import reduce_winners

winning_set = winners()

def test_winners():
    testwinners = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8},
                   {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    assert winning_set == testwinners

def test_check_win_empty():
    p1 = set()
    assert check_win(p1) == False

def test_check_win_loser():
    p1 = {1, 3, 4, 5, 8}
    assert check_win(p1) == False

def test_check_win_winner():
    p1 = {1, 3, 5, 6, 7, 8}
    assert check_win(p1) == True

def test_winning_combinations_empty():
    assert winning_combinations(set(), winning_set) == set()

def test_winning_combinations_19():
    assert winning_combinations({1, 9}, winning_set) == {3, 7}

def test_winning_combinations_15():
    assert winning_combinations({1, 5}, winning_set) == {2, 3, 4, 7}

def test_winning_combinations_15_reduced():
    reducedwinners = [{4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {1, 5, 9}]
    assert winning_combinations({1, 5}, reducedwinners) == {4}

def test_reduce_winners_winners_23():
    p1 = {2, 3}
    reducedwinners = [{4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {1, 5, 9}]
    assert reduce_winners(winning_set, p1) == reducedwinners

def test_reduce_winners_winners_137():
    p1 = {1, 3, 7}
    assert reduce_winners(winning_set, p1) == [{4, 5, 6}, {2, 5, 8}]

def test_reduce_winners_no_winners():
    p1 = {1, 3, 5, 7}
    assert reduce_winners(winning_set, p1) == []

def test_reduce_winners_state_empty():
    p1 = set()
    assert reduce_winners(winning_set, p1) == winning_set
