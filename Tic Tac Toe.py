def askInput(grid, playerChar):
    while True:
        pos = input('Where do you want to place?')
        if pos == "0":
            row, col = 0, 0
        elif pos == "1":
            row, col = 0, 1
        elif pos == "2":
            row, col = 0, 2
        elif pos == "3":
            row, col = 1, 0
        elif pos == "4":
            row, col = 1, 1
        elif pos == "5":
            row, col = 1, 2
        elif pos == "6":
            row, col = 2, 0
        elif pos == "7":
            row, col = 2, 1
        elif pos == "8":
            row, col = 2, 2
        if grid[row][col] != "x" and grid[row][col] != "o":
            grid[row][col] = playerChar
            break
        else:
            print('''That place is already filled.
Please pick another place.''')


def printBoard(grid):
    print(f"""
  {grid[0][0]}  |  {grid[0][1]}  |  {grid[0][2]}
-----+-----+-----
  {grid[1][0]}  |  {grid[1][1]}  |  {grid[1][2]}
-----+-----+-----
  {grid[2][0]}  |  {grid[2][1]}  |  {grid[2][2]}
""")


def checkWinner(grid, player):
    if (grid[0][0] == grid[0][1] == grid[0][2]) or \
            (grid[1][0] == grid[1][1] == grid[1][2]) or \
            (grid[2][0] == grid[2][1] == grid[2][2]) or \
            (grid[0][0] == grid[1][0] == grid[2][0]) or \
            (grid[0][1] == grid[1][1] == grid[2][1]) or \
            (grid[0][2] == grid[1][2] == grid[2][2]) or \
            (grid[0][0] == grid[1][1] == grid[2][2]) or \
            (grid[0][2] == grid[1][1] == grid[2][0]):
        print("Player ", player, "wins.")
        print("Thank you for playing this game.")
        return True
    return False


gridMain = [["0", "1", "2"],
            ["3", "4", "5"],
            ["6", "7", "8"]]
print("Hello! Welcome to Tic Tac Toe game!")
print('''
Rules: Player 1 and player 2, take turns 
       marking the spaces in a 3*3 grid. The player who succeeds in placing 
       three of their marks horizontally, vertically, or diagonally wins.
''')
print("\n")
print('Select a mark which Player 1 wants to use:')
print("       x           o")
mark1 = input()
mark2 = "x"
if mark1 == "x":
    mark2 = "o"
print("\n")
printBoard(gridMain)
while True:
    print("Player 1's turn:-")
    askInput(gridMain, mark1)
    printBoard(gridMain)
    flag = checkWinner(gridMain, 1)
    if flag:
        break
    print("Player 2's turn:-")
    askInput(gridMain, mark2)
    printBoard(gridMain)
    flag = checkWinner(gridMain, 2)
    if flag:
        break
