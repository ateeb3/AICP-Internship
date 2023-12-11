import random

print("Welcome to Tic Tac Toe")

print("------------------------")

posiibleNumbers = [1,2,3,4,5,6,7,8,9]
gameboard = [[1,2,3] , [4,5,6], [7,8,9]]

rows= 3
cols = 3
def printGameboard():
    for x in range(rows):
        print("\n+-----+-----+-----+")
        print("|", end="")
        for y in range(cols):
            print("", gameboard[x][y], end=" |")
        print("\n+-------+-------+")

def modifying(num,turn):
    num-=1
    if(num==0):
        gameboard[0][0] = turn
    elif(num == 1):
        gameboard[0][1] = turn
    elif (num == 2):
        gameboard[0][2] = turn
    elif (num == 3):
        gameboard[1][0] = turn
    elif (num == 4):
        gameboard[1][1] = turn
    elif (num == 5):
        gameboard[1][2] = turn
    elif (num == 6):
        gameboard[2][0] = turn
    elif (num == 7):
        gameboard[2][1] = turn
    elif (num == 8):
        gameboard[2][2] = turn

leaveLoop = False

turn = 'x'
turnCounter = 0

while(leaveLoop == False):
    if(turnCounter %2 == 1):
        printGameboard()
        numberPicked = int(input("\nChoose a number [1-9]"))
        if(numberPicked >=1 or numberPicked <= 9):
            modifying(numberPicked, "X")
            posiibleNumbers.remove(numberPicked)
        else:
            print("Invalid Input, Please try again!")
        turnCounter +=1

    else:
        while(True):
            cpuChoice = random.choice(posiibleNumbers)
            print("\nCPU choice: ", cpuChoice)
            if(cpuChoice in posiibleNumbers):
                modifying(cpuChoice, "O")
                posiibleNumbers.remove(cpuChoice)
                turnCounter +=1
                break

def winner():
    #X-axis
    if(gameboard[0][0] == "X" and gameboard[0][1] == "X" and gameboard[0][2] == "X"):
        print("X has won")
        return "X"
    elif(gameboard[0][0] == "O" and gameboard[0][1] == "O" and gameboard[0][2] == "O"):
        print("O has won")
        return "O"
    elif(gameboard[1][0] == "X" and gameboard[1][1] == "X" and gameboard[1][2] == "X"):
        print("X has won")
        return "X"
    elif (gameboard[1][0] == "O" and gameboard[1][1] == "O" and gameboard[1][2] == "O"):
        print("O has won")
        return "O"
    elif (gameboard[2][0] == "X" and gameboard[2][1] == "X" and gameboard[2][2] == "X"):
        print("X has won")
        return "X"
    elif (gameboard[2][0] == "O" and gameboard[2][1] == "O" and gameboard[2][2] == "O"):
        print("O has won")
        return "O"

    #Y-axis
    if (gameboard[1][0] == "X" and gameboard[2][1] == "X" and gameboard[3][2] == "X"):
        print("X has won")
        return "X"
    elif (gameboard[1][0] == "O" and gameboard[2][1] == "O" and gameboard[3][2] == "O"):
        print("O has won")
        return "O"

