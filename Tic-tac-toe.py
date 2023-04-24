def tic_tac_toe_board(positions):
    print(f"{positions['7']} {positions['8']} {positions['9']}     '7 8 9'")
    print(f"{positions['4']} {positions['5']} {positions['6']}     '4 5 6'")
    print(f"{positions['1']} {positions['2']} {positions['3']}     '1 2 3'")

def tic_tac_toe_check(player, positions, score):
    if (positions["1"] == player and positions["2"] == player and positions["3"] == player) or \
        (positions["4"] == player and positions["5"] == player and positions["6"] == player) or \
        (positions["7"] == player and positions["8"] == player and positions["9"] == player) or \
        (positions["1"] == player and positions["4"] == player and positions["7"] == player) or \
        (positions["2"] == player and positions["5"] == player and positions["8"] == player) or \
        (positions["3"] == player and positions["6"] == player and positions["9"] == player) or \
        (positions["1"] == player and positions["5"] == player and positions["9"] == player) or \
        (positions["3"] == player and positions["5"] == player and positions["7"] == player):
        score[player] += 1
        print(f"{player} WIN!!!")
        return True
    elif positions["1"] != "-" and positions["2"] != "-" and positions["3"] != "-" and \
            positions["4"] != "-" and positions["5"] != "-" and positions["6"] != "-" and \
            positions["7"] != "-" and positions["8"] != "-" and positions["9"] != "-":
        print("DRAW")
        return True


score = {"X": 0, "O": 0}
positions = {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-"}
player = "O"
while True:
    if player == "O":
        player = "X"
    elif player == "X":
        player = "O"

    while True:
        print(f"{player} turn.")
        tic_tac_toe_board(positions)
        position = input("Enter position: ")
        if position in positions and positions[position] == "-":
            positions[position] = player
            break
        else:
            print("Invalid position, please try again.")
            continue

    if tic_tac_toe_check(player, positions, score):
        tic_tac_toe_board(positions)
        while True:
            again = input("Wanna play again? [YES/NO]: ")
            again = again.lower()
            if again == "yes":
                positions = {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-"}
                print(f"X {score['X']} - {score['O']} O")
                break
            elif again == "no":
                break
            else:
                print("Invalid command")
        if again == "no":
            break
input("Press ENTER to terminate the program.")


