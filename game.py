def print_board(my_board):
    for i in range(5):
        for j in range(5):
            print(my_board[i][j], end="   ")
        print("")
    return


board = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]
print("Empty Board")
print_board(board)

player_1 = input("\nEnter Player 1 Name: ")
player_1_char = list(input("Enter 5 characters of player 1 seperated by , : ").split(","))
pos_a = {}
if len(player_1_char) == 5:
    for i in range(5):
        char_name = "A-"+player_1_char[i]
        board[4][i] = char_name
        pos_a[char_name] = [4,i]

print_board(board)

player_2 = input("Enter Player 2 Name: ")
player_2_char = list(input("Enter 5 characters of player 1 seperated by , : ").split(","))
pos_b = {}
if len(player_1_char) == 5:
    for i in range(5):
        char_name = "B-"+player_1_char[i]
        board[0][i] = char_name
        pos_b[char_name] = [0, i]

print_board(board)

print("Moves are L for left move ")
print("Moves are R for right move ")
print("Moves are F for forward move ")
print("Moves are B for backward move ")
game_playing = 0
while game_playing < 1:
    a_move = input(player_1+"'s Move (character:Move)").split(":")
    a_char = "A-"+a_move[0]
    position_a = pos_a[a_char]
    i = position_a[0]
    j = position_a[1]
    if a_move[1] == "L":
        if board[i][j-1] == "-":
            board[i][j-1] = a_char
            board[i][j] = "-"
            pos_a[a_char] = [i,j-1]
    elif a_move[1] == "R":
        if board[i][j + 1] == "-":
            board[i][j + 1] = a_char
            board[i][j] = "-"
            pos_a[a_char] = [i, j + 1]
    elif a_move[1] == "F":
        if board[i-1][j] == "-":
            board[i-1][j] = a_char
            board[i][j] = "-"
            pos_a[a_char] = [i-1, j]
    elif a_move[1] == "B":
        if board[i+1][j] == "-":
            board[i+1][j] = a_char
            board[i][j] = "-"
            pos_a[a_char] = [i+1, j]
    print_board(board)
    b_move = input(player_2+"'s Move (character:Move)").split(":")
    b_char = "B-"+b_move[0]
    position_b = pos_b[b_char]
    i = position_b[0]
    j = position_b[1]
    if b_move[1] == "L":
        if board[i][j + 1] == "-":
            board[i][j + 1] = b_char
            board[i][j] = "-"
            pos_b[b_char] = [i,j+1]
    elif b_move[1] == "R":
        if board[i][j - 1] == "-":
            board[i][j - 1] = b_char
            board[i][j] = "-"
            pos_b[b_char] = [i, j -1]
    elif b_move[1] == "F":
        if board[i+1][j] == "-":
            board[i+1][j] = b_char
            board[i][j] = "-"
            pos_b[b_char] = [i+1, j]
    elif b_move[1] == "B":
        if board[i-1][j] == "-":
            board[i-1][j] = b_char
            board[i][j] = "-"
            pos_b[b_char] = [i-1, j]
    print_board(board)