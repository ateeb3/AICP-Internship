electricity_matrix = [
    [50, 150, 250],
    [80, 120, 180],
]


def costSlab1():
    slab1_units = min(electricity_matrix[0][0], 100)
    slab1_cost = slab1_units * 10
    print(f"Bill for Slab 1 is : \n{slab1_cost}\t\t{electricity_matrix[0][1]}\t\t{electricity_matrix[0][2]}")


def costSlab2():
    slab2_units = max(min(electricity_matrix[0][1], 200) - 100, 0)
    slab2_cost = slab2_units * 15
    print(f"Bill for Slab 2 is : \n{electricity_matrix[0][1]}\t\t{slab2_cost}\t\t{electricity_matrix[0][2]}")


def costSlab3():
    slab3_units = max(electricity_matrix[0][2] - 200, 0)
    slab3_cost = slab3_units * 20
    print(f"Bill for Slab 3 is : \n{electricity_matrix[0][2]}\t\t{electricity_matrix[0][2]}\t\t{slab3_cost}")


def main_menu(student_id):
    while True:
        print(f"\n\nMy Student ID is {student_id}")
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
