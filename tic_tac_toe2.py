import random

# To-do: allow choice of x or o DONE

# Try to come up with a recursive way to check win condition

# Determines if the attempted move is valid by seeing if the space on the grid is taken or not. If it is a valid move, the move will be accepted
# and the grid value of the move returned.
def validMove(gridList, turns):
    enteredMove = False

    while enteredMove == False:
        # Prompts for a move with a message depending on what turn it is.
        if turns < 3:
            move = int(input("Enter your {}{} move: ".format(str(turns + 1), ordinals[turns])))
        else:
            move = int(input("Enter your {}{} move: ".format(str(turns + 1), "th")))


        if grid[move-1] == "":
            # I don't really need the below line, as returning stops the function anyway...
            enteredMove = True
            return move
        else:
            print("Space already taken, try another move.")

# Determines if the win condition has been met
# turn defines which character (x or o) to look for
def endGame(gridList):
    # checks for horizontal 3-in-a-rows
    for x in range(0,7,3):
        if gridList[x] == gridList[x+1] == gridList[x+2] == gridList[x] and gridList[x] != "":
            return True

    # checks for vertical 3-in-a-rows
    for x in range(3):
        if gridList[x] == gridList[x+3] == gridList[x+6] == gridList[x] and gridList[x] != "":
            return True

    # checks for one diagonal 3-in-a-row (grids 1,5,9)
    if gridList[0] == gridList[4] == gridList[8] == gridList[0] and gridList[0] != "":
            return True

    # checks for the other diagonal 3-in-a-row (grids 3,5,7)
    if gridList[2] == gridList[4] == gridList[6] == gridList[2] and gridList[2] != "":
            return True

# returns a list of the grid spaces that are still empty
def emptySpace(gridList):
    output = []
    for x in range(9):
        if gridList[x] == "":
            output.append(x)
    return output


def opponentMove(gridList, turn):
    if turn < 5:
    
        # spaces = a list of empty spaces on the board
        spaces = emptySpace(gridList)
        maxIndex = len(spaces) - 1
        
        # chooses a random index to select an empty grid at random
        return spaces[random.randint(0, maxIndex)]
    


# a - i = grids 1-9 (counted from top to bottom, left to right)
# [1] [2] [3]
# [4] [5] [6]
# [7] [8] [9]

# turns = how many turns have been made so far
# The elements of the list correspond to grids squares 1-9 from left to right
grid = ["", "", "", "", "", "", "", "", ""]
ordinals = ["st", "nd", "rd"]
turns = 0
board = "[1] [2] [3]\n[4] [5] [6]\n[7] [8] [9]" 



# team selection
team = input("x or o? ")

while team != "x" and team != "o":
    print("Invalid entry: select x or o")
    team = input("x or o? ")

if team == "x":
    opTeam = "o"
else:
    opTeam = "x"



# "gameplay"
print(board)
while turns < 5:

    # player's move
    move = validMove(grid, turns)-1
    # subtract 1 so that the chosen grid square maps to the right variable in the list
    grid[move] = team

    board = "[{0:1}] [{1:1}] [{2:1}]\n[{3:1}] [{4:1}] [{5:1}]\n[{6:1}] [{7:1}] [{8:1}]".format(grid[0],grid[1],grid[2],grid[3],grid[4],grid[5],grid[6],grid[7],grid[8])
    print(board)

    if endGame(grid):
        # prints the board at the end of the game
        print("Game Over: You Win!\n" + "-----------\n" + board)
        break
    
    if turns == 4:
        print("Game Over: Stalemate")
        break

    # opponent's move
    opMove = opponentMove(grid, turns)
    grid[opMove] = opTeam

    print("Opponent turn {}".format(turns+1))
    board = "[{0:1}] [{1:1}] [{2:1}]\n[{3:1}] [{4:1}] [{5:1}]\n[{6:1}] [{7:1}] [{8:1}]".format(grid[0],grid[1],grid[2],grid[3],grid[4],grid[5],grid[6],grid[7],grid[8])


    print(board)
    turns += 1

    if endGame(grid):
        # prints the board at the end of the game
        print("Game Over: You Lose\n" + "-----------\n" + board)
        break



    