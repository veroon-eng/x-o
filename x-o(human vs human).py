board={"0":" ","1":" ","2":" ",
       "3":" ","4":" ","5":" ",
       "6":" ","7":" ","8":" "}

player=1
total_moves=0
end_check=0


def check():
            #####checking for player one(X)#####
    
    #check for rows
    if board["0"]=="X" and board["1"]=="X" and board["2"]=="X":
        print("player one won!!!!!!!!!")
        return 1
    if board["3"]=="X" and board["4"]=="X" and board["5"]=="X":
        print("player one won!!!!!!!!!")
        return 1
    if board["6"]=="X" and board["7"]=="X" and board["8"]=="X":
        print("player one won!!!!!!!!!")
        return 1


    #check for diagonal
    if board["0"]=="X" and board["4"]=="X" and board["8"]=="X":
        print("player one won!!!!!!!!!")
        return 1
    if board["2"]=="X" and board["4"]=="X" and board["6"]=="X":
        print("player one won!!!!!!!!!")
        return 1


    #check for columns
    if board["0"]=="X" and board["3"]=="X" and board["6"]=="X":
        print("player one won!!!!!!!!!")
        return 1
    if board["1"]=="X" and board["4"]=="X" and board["7"]=="X":
        print("player one won!!!!!!!!!")
        return 1
    if board["2"]=="X" and board["5"]=="X" and board["8"]=="X":
        print("player one won!!!!!!!!!")
        return 1

            #####checking for player two(O)#####

    #check for rows
    if board["0"]=="O" and board["1"]=="O" and board["2"]=="O":
        print("player one won!!!!!!!!!")
        return 1
    if board["3"]=="O" and board["4"]=="O" and board["5"]=="O":
        print("player one won!!!!!!!!!")
        return 1
    if board["6"]=="O" and board["7"]=="O" and board["O"]=="X":
        print("player one won!!!!!!!!!")
        return 1


    #check for diagonal
    if board["0"]=="O" and board["4"]=="O" and board["O"]=="X":
        print("player one won!!!!!!!!!")
        return 1
    if board["2"]=="O" and board["4"]=="O" and board["6"]=="O":
        print("player one won!!!!!!!!!")
        return 1


    #check for columns
    if board["0"]=="O" and board["3"]=="O" and board["6"]=="O":
        print("player one won!!!!!!!!!")
        return 1
    if board["1"]=="O" and board["4"]=="O" and board["7"]=="O":
        print("player one won!!!!!!!!!")
        return 1
    if board["2"]=="O" and board["5"]=="O" and board["8"]=="O":
        print("player one won!!!!!!!!!")
        return 1

    




print("    0 | 1 | 2 ")
print("   ----------")
print("    3 | 4 | 5 ")
print("   ----------")
print("    6 | 7 | 8 ")
print("#######let's start#######")


while True:
    print(board["0"], "|", board["1"], "|",board["2"])
    print("----------")
    print(board["3"], "|", board["4"], "|",board["5"])
    print("----------")
    print(board["6"], "|", board["7"], "|",board["8"])
    print("----------")
    end_check=check()
    if total_moves==9 or end_check==1:
        break
    while True:
        if player==1:
            player1_input=input("player one: ")
            
            if player1_input.upper() in board and board[player1_input.upper()]==" ":
                board[player1_input.upper()]="X"
                player=2
                break
            else:
                print("try again")
                continue
        else:
            player2_input=input("player 2: ")
            
            if player2_input.upper() in board and board[player2_input.upper()]==" ":
                board[player2_input.upper()]="O"
                player=1
                break
            else:
                print("try again")
                continue
    total_moves +=1
    
                






























