cnic_last_digit = 3
one_side_of_hexagon = cnic_last_digit
one_side_of_square = cnic_last_digit + 1

def calcArea():
    return 1.5 * 1.732 * one_side_of_hexagon

def calcPeri():
    return 6 * one_side_of_hexagon
def calcAngleSum():
    return 6 * 120
def displayHexagon():
    print(f"Area of hexagon is: {calcArea()}")
    print(f"Perimeter of hexagon is: {calcPeri()}")
    print(f"Sum of angles of hexagon is: {calcAngleSum()}")


def calcAreaSquare():
    return one_side_of_square * 2
def calcPeriSquare():
    return one_side_of_square * 4

def displaySquare():
    print(f"Area of square is: {calcAreaSquare()}")
    print(f"Perimeter of square is: {calcPeriSquare()}")

def mainMenu():
    while True:
        user_choice = int(input("Enter 1 to calculate area, perimeter, and sum of angles of hexagon\nEnter 2 to calculate area and perimeter of square\n"))
        if user_choice == 1:
            displayHexagon()
        elif user_choice == 2:
            displaySquare()
        else:
            break

mainMenu()