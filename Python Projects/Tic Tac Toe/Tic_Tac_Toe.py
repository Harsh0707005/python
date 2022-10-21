def printBoard(arr):
    print(f'{arr[0]} | {arr[1]} | {arr[2]}')
    print(f'--|---|---')
    print(f'{arr[3]} | {arr[4]} | {arr[5]}')
    print(f'--|---|---')
    print(f'{arr[6]} | {arr[7]} | {arr[8]}')


def checkWin(arr):
    win_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in win_positions:
        win = {arr[win[0]], arr[win[1]], arr[win[2]]}
        if len(win) == 1:
            return True


if __name__ == "__main__":

    print("---------------- Welcome to Tic Tac Toe ----------------")

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    turn = 1

    while True:

        printBoard(arr)

        if turn == 1:
            print("X's Chance")
            value = int(input("Enter a position: "))
        else:
            print("O's Chance")
            value = int(input("Enter a position: "))

        if value < 0 or value > 9:
            print("\nEnter a valid position\n")
            continue

        if arr[value] == "X" or arr[value] == "O":
            print("\nPosition already occupied!!!")
            print()
            continue

        if turn == 1:
            arr[value] = "X"
        else:
            arr[value] = "O"

        if checkWin(arr):
            print()
            printBoard(arr)
            print(arr[value], "won")
            break
        turn = 1-turn
