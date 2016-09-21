from TicTacToe.game import Game

def playtictactoe():
    print_board_state(range(1, 10))
    print('Play by entering the field number of the next field you want to')
    print('occupy and confirm wiht <enter>. See above for the field numbers.')
    print("Type 'quit' or '1000' to quit the game at any time")
    game = Game()
    game_round = 1
    print_board_state(game.board_state)
    while True:
        field_number = get_field_number_stdin()
        if field_number == 1000:
            break
        if game_round%2 == 1:
            game.move(game.player1, field_number)
        else:
            game.move(game.player2, field_number)
        print_board_state(game.board_state)
        if game_ended(game):
            break
        game_round += 1
    if game.player1.is_winner:
        print("player 1 wins!")
    elif game.player2.is_winner:
        print("player 2 wins!")
    else:
        print("The game is a tie!")

def get_from_stdin():
    userresponse = input()
    if userresponse == 'quit' or userresponse == '1000':
        return 1000
    try:
        userresponse = int(userresponse)
    except ValueError:
        userresponse = 100
    return userresponse

def get_field_number_stdin():
    field_number = get_from_stdin()
    while not field_number in range(1, 10):
        if field_number == 1000:
            break
        print('Invalid input. Please enter a number between 1 and 9.')
        field_number = get_from_stdin()
    return field_number

def game_ended(game):
    if game.player1.is_winner:
        return True
    if game.player2.is_winner:
        return True
    if game.player1.state | game.player2.state == set(range(1, 10)):
        return True

def print_board_state(board_state):
    print()
    print("*******************")
#    print("1*****2*****3******")
    print("*     *     *     *")
    print("*  {0}  *  {1}  *  {2}  *".format(board_state[0],
                                             board_state[1], board_state[2]))
    print("*     *     *     *")
    print("*******************")
#    print("4*****5*****6******")
    print("*     *     *     *")
    print("*  {0}  *  {1}  *  {2}  *".format(board_state[3],
                                             board_state[4], board_state[5]))
    print("*     *     *     *")
    print("*******************")
#    print("7*****8*****9******")
    print("*     *     *     *")
    print("*  {0}  *  {1}  *  {2}  *".format(board_state[6],
                                             board_state[7], board_state[8]))
    print("*     *     *     *")
    print("*******************")
    print()

if __name__ == '__main__':
    playtictactoe()
