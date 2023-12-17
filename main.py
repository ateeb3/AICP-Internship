def main():
    c_sack = int(input("Enter the number of cement sacks: "))
    g_sack = int(input("Enter the number of gravel sacks: "))
    s_sack = int(input("Enter the number of sand sacks: "))

    actual_price = (c_sack * 3) + (g_sack * 2) + (s_sack * 2)
    total_order = c_sack + g_sack + s_sack

    rej = 0
    total_weight = 0

    for count in range(1, total_order + 1):
        print()
        content = input("Enter the content of a sack, C for cement, G for gravel, and S for sand: ")

        if content == 'C':
            while True:
                weight = float(input("Enter weight of cement sack between 24.9KG and 25.1KG: "))
                if 24.9 <= weight <= 25.1:
                    break
                else:
                    print("Sack is underweight or overweight")

        elif content in ('G', 'S'):
            while True:
                weight = float(input(f"Enter weight of {content} sack between 49.0KG and 50.1KG: "))
                if 49.0 <= weight <= 50.1:
                    break
                else:
                    print(f"{content} sack is underweight or overweight")

        else:
            print("The entered content is incorrect")

        total_weight += weight

    print()
    print(f"The total weight of order is: {total_weight}")
    print(f"The number of sacks rejected are: {rej}")

    sp = 0
    sp_price = 0

    while c_sack >= 1 and g_sack >= 2 and s_sack >= 2:
        sp += 1
        c_sack -= 1
        g_sack -= 2
        s_sack -= 2

    if sp >= 1:
        sp_price = sp * 10
        print(f"Total special packs are: {sp}")
        print(f"Price of special packs in dollars is: ${sp_price}")

        discount_price = (c_sack * 3) + (g_sack * 2) + (s_sack * 2) + sp_price
        print(f"The actual price of order is: ${actual_price}")
        print(f"The discounted price of order is: ${discount_price}")

        total_discount = actual_price - discount_price
        print(f"Total discount in order is: ${total_discount}")

    else:
        print(f"Price of regular order in dollars is: ${actual_price}")


if __name__ == "__main__":
    main()
