import random

def reset():
    global used
    global last_play
    global board
    board = {}
#    board = board.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9], " ")
    board = [' '] * 10
    used = []
    last_play = 0
    return
    

def printBoard():
    print(" _________________")
    print("|     |     |     |")
    print("|  "+board[1]+"  |  "+board[2]+"  |  "+board[3]+"  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  "+board[4]+"  |  "+board[5]+"  |  "+board[6]+"  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  "+board[7]+"  |  "+board[8]+"  |  "+board[9]+"  |")
    print("|_____|_____|_____|")
    return
    
def set_player():
    if last_play <= 1:
        return 'p1'
    elif last_play == 2:
        return 'p2'
    return
    
    
def player(num):
    global last_play
    global board
    if board[num] != " ":
        print("This spot is already taken! Run 'play()' for help")
        num = eval(input("Try again:"))
        player(num)
        printBoard()  
    else:    
        x = str(playerNum[set_player()])
        board[int(num)] = x
        printBoard()
# Sets the appropriate spot in the matrix with the player's playerpiece, based on the number they entered.
        winning = [board[1] == board[2] == board[3] == x,
                    board[1] == board[4] == board[7] == x,    
                    board[3] == board[6] == board[9] == x,          
                    board[7] == board[8] == board[9] == x,
                    board[1] == board[5] == board[9] == x,
                    board[4] == board[5] == board[6] == x,
                    board[2] == board[5] == board[8] == x,
                    board[7] == board[5] == board[3] == x]
        if any(winning):
            if last_play == 1:
                print("YOU WIN!")
            if last_play == 2:
                print("YOU LOSE!")
            reset()
            play_again()
# Checks to see if the player won, asks them if they want to play again
        elif full_board_check(board):
            print("TIE!")
            reset()
            play_again()
# Checks for a tie, resets the game, asks them if they want to play again
        else:
            if last_play == 2:
                last_play = 1
                move()
            elif last_play <= 1:
                last_play = 2
                com_play()
    return
 
def full_board_check(board):
    ''' Function to check if any remaining blanks are in the board '''
    if " " in board[1:]:
        return False
    else:
        return True
    return

# Changes the playerNum to the next player, requests an input.            
def play():
    reset()
    global playerNum
    playerNum = {'p1':"",'p2':""}
    print("The board is divided up into a grid, using the numbers 1 through 9.")
    print("")
    print(" _________________")
    print("|     |     |     |")
    print("|  1  |  2  |  3  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  4  |  5  |  6  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  7  |  8  |  9  |")
    print("|_____|_____|_____|")
    print("")   
    print("You can insert a piece by entering a number between 1 and 9")
    print("You can reset the game using the 'reset()' command.")
    while playerNum == {'p1':"",'p2':""}:    
        piece = input("Welcome to Tic Tac Toe! Would you like to be an X or an O? ")
        if str(piece.upper()) == "X":
            playerNum['p1'] = "X"
            playerNum['p2'] = "O"
        elif str(piece.upper()) == "O": 
            playerNum['p1'] = "O"
            playerNum['p2'] = "X"
    move()
    return
    
def move():
    num = input("It's your turn Player! Place your piece: ")
    print("")
    while not num.isdigit() or int(num) not in range(1,10):
        num = input("Fuck off Andrew, try again: ")
    player(int(num))
    return

def play_again():
    answer = " "
    answer = input("The game has been reset. Do you want to play again? Yes/No. ")
    if answer.lower() == "yes":
        play()
    elif answer.lower() == "no":
        answer = "no"
    else:
        answer = " "
    while answer == " ":
        play_again()
    return

def com_play():
# Decicion logic
    print("Computer playing...")
    opp = str(playerNum['p1'])
    comp = str(playerNum['p2'])
    com_win(comp,opp)
    return

def com_win(comp, opp):
    print("Ran com_win")
    char = comp
    char_logic(char,opp)
    return

def com_block(opp):
# Decicion logic
    print("Ran com_block")
    char = opp
    char_logic(char,opp)	
    return
    
def char_logic(char,opp):
    # Left and right, in the middle
    if board[1] == board[3] == char and board[2] == " ":            
        num = 2
        player(num)
    elif board[4] == board[6] == char and board[5] == " ":            
        num = 5
        player(num)
    elif board[7] == board[9] == char and board[8] == " ":       
        num = 8
        player(num)    
    # left to right
    elif board[1] == board[2] == char and board[3] == " ":            
        num = 3
        player(num)
    elif board[4] == board[5] == char and board[6] == " ":        
        num = 6
        player(num)
    elif board[7] == board[8] == char and board[9] == " ":       
        num = 9
        player(num)
    # right to left    
    elif board[2] == board[3] == char and board[1] == " ":        
        num = 1
        player(num)
    elif board[5] == board[6] == char and board[4] == " ":        
        num = 4
        player(num)
    elif board[8] == board[9] == char and board[7] == " ":        
        num = 7
        player(num)
    # up/down, blocking the middle
    elif board[1] == board[7] == char and board[4] == " ":        
        num = 4
        player(num)
    elif board[2] == board[8] == char and board[5] == " ":        
        num = 5
        player(num)
    elif board[3] == board[9] == char and board[6] == " ":     
        num = 6
        player(num)    
    # up to down  
    elif board[1] == board[4] == char and board[7] == " ":           
        num = 7
        player(num)
    elif board[2] == board[5] == char and board[8] == " ":           
        num = 8
        player(num)
    elif board[3] == board[6] == char and board[9] == " ":           
        num = 9
        player(num)
    # down to up
    elif board[4] == board[7] == char and board[1] == " ":           
        num = 1
        player(num)
    elif board[5] == board[8] == char and board[2] == " ":           
        num = 2
        player(num)
    elif board[6] == board[9] == char and board[3] == " ":           
        num = 3
        player(num)   
    # diaganols - blocking the middle
    elif board[1] == board[9] == char and board[5] == " ":   
        num = 5
        player(num)
    elif board[7] == board[3] == char and board[5] == " ":           
        num = 5
        player(num)    
    # diaganols
    elif board[1] == board[5] == char and board[9] == " ":   
        num = 9
        player(num)
    elif board[3] == board[5] == char and board[7] == " ":           
        num = 7
        player(num)
    elif board[7] == board[5] == char and board[3] == " ":           
        num = 3
        player(num)
    elif board[9] == board[5] == char and board[1] == " ":           
        num = 1
        player(num)
    else:
        if char == opp:
            print("Pulling other int.")            
            if board[5] == " ":
                num = 5
                player(num)
            elif board[5] != " ":
                starting_moves = [1,3,7,9]
                rand_start = random.sample(starting_moves,1)
                while board[rand_start[0]] != " ":
                    rand_start = random.sample(starting_moves,1)
                player(rand_start)
                    elif board[1] and board[3] and board[7] and board[9] != " ":
                        print("Pulling random int.")
                        rand = random.randint(1,9)
                        while board[rand] != " ":
                            rand = random.randint(1,9)
                        player(rand)
                    else: 
                        start = " "
        else:
            com_block(opp)
        return

play()
            