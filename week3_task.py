electricity_matrix = [
    [55, 65, 75],
    [120, 150, 170],
    [210, 230, 240],
]

def costSlab1():
    slab1_units = electricity_matrix[0]
    slab1_cost = [i*10 for i in slab1_units]
    print(f"Bill for Slab 1 is :")
    print(*slab1_cost , sep="\t\t")

def costSlab2():
    slab2_units = electricity_matrix[1]
    slab2_cost = [i*15 for i in slab2_units]
    print("Bill for Slab 2 is :")
    print(*slab2_cost , sep="\t")


def costSlab3():
    slab3_units = electricity_matrix[2]
    slab3_cost = [i * 20 for i in slab3_units]
    print("Bill for Slab 3 is :")
    print(*slab3_cost , sep="\t")

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
