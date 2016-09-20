from TicTacToe.game import Game

def get_field_number_stdin():
    def get_from_stdin():
        userresponse = input()
        try:
            userresponse = int(userresponse)
        except ValueError:
            userresponse = 100
        return userresponse
    field_number = get_from_stdin()
    while not field_number in range(1, 10):
        print('Invalid input. Please enter a number between 1 and 9.')
        field_number = get_from_stdin()
    return field_number

def playtictactoe():

    def game_ended(g):
        if g.player1.is_winner:
            return True
        if g.player2.is_winner:
            return True
        if g.player1.state | g.player2.state == set(range(1, 10)):
            return True

    g=Game()
    game_round=1
    print(g.board_state)
    while True:
        field_number = get_field_number_stdin()
        if game_round%2 == 1:
            g.move(g.player1, field_number)
        else:
            g.move(g.player2, field_number)
        print(g.board_state)
        if game_ended(g):
            break
        game_round += 1
    if g.player1.is_winner:
        print("player 1 wins!")
    elif g.player2.is_winner:
        print("player 2 wins")
    else:
        print("The game is a tie")


if __name__ == '__main__':
    playtictactoe()
