def tic_tac_toe_board(positions):
    print(f"{positions['7']} {positions['8']} {positions['9']}     '7 8 9'")
    print(f"{positions['4']} {positions['5']} {positions['6']}     '4 5 6'")
    print(f"{positions['1']} {positions['2']} {positions['3']}     '1 2 3'")

def tic_tac_toe_check(player, positions):
    for number in range(1,8,3):
        if positions[str(number)] == player and positions[str(number+1)] == player and positions[str(number+2)] == player:
            return True
    for number in range(1,4):
        if positions[str(number)] == player and positions[str(number+3)] == player and positions[str(number+6)] == player:
            return True
    if positions["1"] == player and positions["5"] == player and positions["9"] == player:
        return True
    elif positions["3"] == player and positions["5"] == player and positions["7"] == player:
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

    if tic_tac_toe_check(player, positions):
        tic_tac_toe_board(positions)
        print(f"{player} WIN!!!")
        score[player] += 1
        while True:
            again = input("Wanna play again? [YES/NO] ")
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


