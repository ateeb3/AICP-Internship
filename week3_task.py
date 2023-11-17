electricity_matrix = [
    [550,  650,  750],
    [1800, 2250, 2250],
    [4200, 4600, 4800],
]


def costSlab1():
    print("Bill for Slab 1 is :")
    for value in electricity_matrix[0]:
        print(value, end="\t")
def costSlab2():
    print("\nBill for Slab 2 is :")
    for value in electricity_matrix[1]:
        print(value, end="\t")


def costSlab3():
    print("Bill for Slab 3 is :")
    for value in electricity_matrix[2]:
        print(value, end="\t")


def main_menu(student_id):
    while True:
        print(f"\n\n\nMy Student ID is {student_id}")
        print("Enter your choice:")
        print("Press 1 to display the bill of slab 1 and slab 2.")
        print("Press 2 to display the bill of slab 3.")
        print("Press any other key to exit.")

        choice = input("Enter your choice: ")

        if choice == '1':
            costSlab1()
            costSlab2()
        elif choice == '2':
            costSlab3()
        else:
            break


student_id = input("Enter your Student ID: ")


main_menu(student_id)
