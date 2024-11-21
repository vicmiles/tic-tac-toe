

def evaluate(board):
    i = 0
    gameIsNotFinished = False
    length = len(board)
    while i < length:
        if board[i] == '-':
            gameIsNotFinished = True
            i += 1
        elif board[i] == 'x':
            if i < length -2 and board[i + 1] == 'x' and board[i + 2] == 'x':
                return ('x')
            i += 1
        elif board[i] == 'o':
            if i < length -2 and board[i + 1] == 'o' and board[i + 2] == 'o':
                return ('o')
            i += 1

    if (gameIsNotFinished):
        return('-')
    else:
        return('!')

def move(board, mark, position):
    pos = int(position)
    if pos > 0:
        new_board = board[:pos] + mark + board[pos+1:]
    else:
        new_board = mark + board[pos+1:]
    print(new_board)
    return (new_board)

def isPositionOk(board, position):
    if str(position).isnumeric():
        pos = int(position)
        if pos < 0 or pos > len(board):
            return (False)
        if (board[pos] == '-'):
            return (True)
        else:
            return (False)
    elif str(position) == 'end' or str(position) == 'END':
        print('Thanks for playing. Goodbye!')
        exit()
    else:
        return (False)

def player_move(board):
    position = input("Write the position you put your mark on (0 - 19): ")

    while (not isPositionOk(board, position)):
        position = input("Wrong input, try again. Write the position you put your mark on (0 - 19): ")

    return(move(board, 'x', position))

def pc_move(board):
    from random import randrange
    position = randrange(19)
    while (not isPositionOk(board, position)):
        position = randrange(19)
    return(move(board, 'o', position))

def tictactoe_1d():
    print('welcome. to exit the game type end')
    board = '--------------------'
    print(board)

    isFinished = False
    while (not isFinished):
        board = player_move(board)
        if evaluate(board) != '-':
            isFinished = True
        else:
            board = pc_move(board)
            if evaluate(board) != '-':
                isFinished = True

    ev = evaluate(board)
    if (ev == 'x'):
        print("The Player wins!")
    elif (ev == 'o'):
        print("The Computer wins!")
    else:
        print("Draw!")

tictactoe_1d()