
restart = "N"
board=[' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ']
win = 0
step_count = 1
def display_board(board):
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9]+'  ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[4]+' | '+board[5]+' | '+board[6]+'  ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+'  ')
    print('   |   |   ')
    pass
def player_input():
    
    global Player1
    global Player2
    Player1 = ''
    Player2 = ''
    while not (Player1=='X' or Player1=='O'):
        Player1 = input(print('Do you wan to be either X or O?')).upper()
        if Player1 == 'X':
            Player2 = 'O'
            print('Player 1 will be using {}'.format(Player1))
            print('Player 2 will be using {}'.format(Player2))

        elif Player1 =='O':
            Player1 ='O'
            Player2 ='X'
            print('Player 1 will be using {}'.format(Player1))
            print('Player 2 will be using {}'.format(Player2)) 
def position_update(board,maker,position):
    board[position]=maker
def check_win(board,palyer_name):
    global win
    if board[1] == board[2] == board[3]!=' ' :
        win = 1
    elif board[4] == board[5] == board[6]!=' ':
        win = 1
    elif board[7] == board[8] == board[9]!=' ':
        win =1
    elif board[1] == board[4] == board[7]!=' ':
        win = 1
    elif board[2]==board[5] == board[8]!=' ':
        win = 1
    elif board[9] == board[6] == board[3]!=' ': 
        win = 1
    elif board[1] == board[5] == board[9]!=' ':
        win = 1
    elif board[3] == board[5] == board[7]!=' ':
        win = 1
    else:
        win = 0
    if win == 1:
        print('{} win!'.format(input_player))
def user_input():
    global position
    global maker
    global step_count
    global input_player
    if step_count%2 == 1:
        maker = Player1
        input_player = 'Player1'
    elif step_count%2==0:
        maker = Player2
        input_player = 'Player2'
    while True:
        try:
            position = int(input('{}: Please input your location:'.format(input_player)))
        except ValueError:
            print("Please input a integer")
            continue
        if position < 0 or position > 10 or board[position]!= ' ':
            print('Input error, please try again')
            continue
        else:  
            position_update(board,maker,position)
            display_board(board)
            step_count += 1
            break
def game_restart():
    global win
    global step_count
    global restart
    global board
    win = 0
    step_count = 1
    restart="N"
    player_input()
    board = [ ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ' , ' ']
win = 0
player_input()
while win == 0 and step_count <10 and restart == "N":
    user_input()
    position_update(board,maker,position)
    check_win(board, input_player)
    if win ==1:
        print("{}  win!".format(input_player))
        restart = input(print("Do you want to restar the game? Y/N")).upper()
        if restart == "Y":
            game_restart()
        elif restart == "N":
            print("Bye")
            break     
    elif win ==0 and step_count ==10:
        restart = input(print("No one win. Do you want to restart the game? Y/N")).upper()
        game_restart(restart)
        if restart == "Y":
            game_restart()
        elif restart == "N":
            print("Bye")
            break     
    

