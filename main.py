charity_names = [input("Enter name for Charity 1: "), input("Enter name for Charity 2: "), input("Enter name for Charity 3: ")]
charity_totals = [0, 0, 0]

def display_charities():
    for i, name in enumerate(charity_names, start=1):
        print(f"{i}. {name}")

def get_charity_choice():
    while True:
        try:
            choice = int(input("Enter the number of the charity (1, 2, or 3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

shopping_bill = float(input("Enter the customer's shopping bill: "))
charity_choice = get_charity_choice()
donation = shopping_bill * 0.01
charity_totals[charity_choice - 1] += donation


def process_customer():
    print("Processing a customer...")
    display_charities()
    shopping_bill = float(input("Enter the customer's shopping bill: "))
    charity_choice = get_charity_choice()
    donation = shopping_bill * 0.01
    charity_totals[charity_choice - 1] += donation
    print(f"Donation of ${donation:.2f} recorded for {charity_names[charity_choice - 1]}.")

# Task 3 - Show the totals so far
def show_totals():
    print("\nCharity Totals:")
    sorted_charities = sorted(zip(charity_names, charity_totals), key=lambda x: x[1], reverse=True)
    grand_total = 0
    for name, total in sorted_charities:
        print(f"{name}: ${total:.2f}")
        grand_total += total
    print("\nGRAND TOTAL DONATED TO CHARITY:", grand_total)


process_customer()
process_customer()
show_totals()
