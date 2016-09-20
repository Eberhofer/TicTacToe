"""
    TicTacToe supporting functions
    ------------------------------
"""

def winners():
    """
        Returns a list of sets with winning combinations for tic tac toe.
    """
    return [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8},
            {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]

def check_win(player_state):
    """
        Returns a boolean - True if player_state fields is a winner.
    """
    for i in winners():
        if i < player_state:
            win = True
            break
    else:
        win = False
    return win

def reduce_winners(current_winners, opponent_state):
    """
        Returns the recalculated set of possible winners by pruning the
        the winners that are blocked by the opponent_state.
    """
    return [_ for _ in current_winners if _.isdisjoint(opponent_state)]

def winning_combinations(player_state, current_winners):
    """
        Returns a list of numbers that can be played which will give the player
        with player_state a certain winning combination. A certain winning
        combination is a combination wich has an intersection with at least two
        sets from current_winners, where the third member differs.
    """
    candlist = []
    for candidate in current_winners:
        if candidate.isdisjoint(player_state):
            continue
        for field_number in candidate - player_state:
            candlist.append(field_number)
            print(candlist)
    return {_ for _ in candlist if candlist.count(_) > 1}
