def print_board(my_board):
    for p in range(5):
        for q in range(5):
            print(my_board[p][q], end="   ")
        print("")
    return


board = [["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-"]]
print("Empty Board")
print_board(board)

player_1 = input("\nEnter Player 1 Name: ")
pos_a = {}
player_1_input = True
while player_1_input:
    player_1_char = list(input("Enter 5 characters of player 1 seperated by , : ").split(","))
    if len(player_1_char) == 5:
        player_1_input = False
        for i in range(5):
            char_name = "A-" + player_1_char[i]
            board[4][i] = char_name
            pos_a[char_name] = [4, i]
    else:
        print("Wrong Input please re-enter")

print_board(board)

player_2 = input("Enter Player 2 Name: ")
pos_b = {}
player_2_input = True
while player_2_input:
    player_2_char = list(input("Enter 5 characters of player 2 seperated by , : ").split(","))
    if len(player_2_char) == 5:
        player_2_input = False
        for i in range(5):
            char_name = "B-" + player_2_char[i]
            board[0][i] = char_name
            pos_b[char_name] = [0, i]
    else:
        print("Wrong Input please re-enter")

print_board(board)

print("Moves are L for left move ")
print("Moves are R for right move ")
print("Moves are F for forward move ")
print("Moves are B for backward move ")
game_playing = 0
while game_playing < 1:
    a_move = input(player_1 + "'s Move (character:Move)").split(":")
    a_char = "A-" + a_move[0]
    position_a = pos_a[a_char]
    i = position_a[0]
    j = position_a[1]
    if a_move[1] == "L":
        if j - 1 <= 0:
            print("Wrong Input")
        else:
            if board[i][j - 1] != "-":
                prev = board[i][j - 1]
                del pos_b[prev]
            board[i][j - 1] = a_char
            board[i][j] = "-"
            pos_a[a_char] = [i, j - 1]
    elif a_move[1] == "R":
        if j + 1 > 5 and i > 5:
            print("Wrong Input")
        else:
            if board[i][j + 1] != "-":
                prev = board[i][j + 1]
                del pos_b[prev]
            board[i][j + 1] = a_char
            board[i][j] = "-"
            pos_a[a_char] = [i, j + 1]

    elif a_move[1] == "F":
        if i - 1 <= 0 and j > 5:
            print("Wrong Input")
        else:
            if board[i - 1][j] != "-":
                prev = board[i - 1][j]
                del pos_b[prev]
            board[i - 1][j] = a_char
            board[i][j] = "-"
            pos_a[a_char] = [i - 1, j]

    elif a_move[1] == "B":
        if i + 1 > 5 and j > 5:
            print("Wrong Input")
        else:
            if board[i + 1][j] != "-":
                prev = board[i + 1][j]
                del pos_b[prev]
            board[i + 1][j] = a_char
            board[i][j] = "-"
            pos_a[a_char] = [i + 1, j]
    print_board(board)
    b_move = input(player_2 + "'s Move (character:Move)").split(":")
    b_char = "B-" + b_move[0]
    position_b = pos_b[b_char]
    i = position_b[0]
    j = position_b[1]
    if b_move[1] == "L":
        if j + 1 > 5 and i > 5:
            print("Wrong Input")
        else:
            if board[i][j + 1] != "-":
                prev = board[i][j + 1]
                del pos_a[prev]
            board[i][j + 1] = b_char
            board[i][j] = "-"
            pos_b[b_char] = [i, j + 1]
    elif b_move[1] == "R":
        if j - 1 <= 0 and i > 5:
            print("Wrong Input")
        else:
            if board[i][j - 1] != "-":
                prev = board[i][j - 1]
                del pos_a[prev]
            board[i][j - 1] = b_char
            board[i][j] = "-"
            pos_b[b_char] = [i, j - 1]
    elif b_move[1] == "F":
        if i + 1 > 5 and j > 5:
            print("Wrong Input")
        else:
            if board[i + 1][j] != "-":
                prev = board[i + 1][j]
                del pos_a[prev]
            board[i + 1][j] = b_char
            board[i][j] = "-"
            pos_b[b_char] = [i + 1, j]

    elif b_move[1] == "B":
        if i - 1 <= 0 and i > 5:
            print("Wrong Input")
        else:
            if board[i - 1][j] != "-":
                prev = board[i - 1][j]
                del pos_a[prev]
            board[i - 1][j] = b_char
            board[i][j] = "-"
            pos_b[b_char] = [i - 1, j]

    print_board(board)
