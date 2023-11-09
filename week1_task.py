
category = ["Case", "RAM", "Main Hard Disk Drive", "Solid State Drive", "Second Hard Disk Drive", "Optical Drive", "Operating System"]
item_codes = [["A1", "A2"], ["B1", "B2", "B3"], ["C1", "C2", "C3"], ["D1", "D2"], ["E1", "E2", "E3"], ["F1", "F2"], ["G1", "G2"]]
descriptions = [["Compact", "Tower"], ["8 GB", "16 GB", "32 GB"], ["1 TB HDD", "2 TB HDD", "4 TB HDD"], ["240 GB SSD", "480 GB SSD"], ["1 TB HDD", "2 TB HDD", "4 TB HDD"], ["DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer"], ["Standard Version", "Professional Version"]]
prices = [[75.00, 150.00], [79.99, 149.99, 299.99], [49.99, 89.99, 129.99], [59.99, 119.99], [49.99, 89.99, 129.99], [50.00, 100.00], [100.00, 175.00]]


chosen_items = {"Case": None, "RAM": None, "Main Hard Disk Drive": None}
additional_items = []
total_price = 0


print("Welcome to the AICP Online Computer Shop!")
print("Available Categories:\n1. Case\n2. RAM\n3. Main Hard Disk\nYou must select one item from each category:")

def display_items(category_name, item_list):
    print(f"{category_name}:")
    for i, item_code in enumerate(item_list):
        print(f"{i+1}. Item Code: {item_code}, Description: {descriptions[category.index(category_name)][i]}, Price: ${prices[category.index(category_name)][i]:.2f}")


def get_user_choice(category_name, item_list):
    while True:
        display_items(category_name, item_list)
        choice = input(f"Choose a {category_name} by entering the item number (1 to {len(item_list)}): ")
        if choice.isdigit() and 1 <= int(choice) <= len(item_list):
            return int(choice) - 1
        else:
            print("Invalid choice. Please enter a valid number.")


for category_name, item_list in zip(category[:3], item_codes[:3]):
    item_index = get_user_choice(category_name, item_list)
    chosen_items[category_name] = item_index
    total_price += prices[category.index(category_name)][item_index]


print("\nChosen items:")
for category_name, item_index in chosen_items.items():
    print(f"{category_name}: {descriptions[category.index(category_name)][item_index]} - ${prices[category.index(category_name)][item_index]:.2f}")

print(f"Total price: ${total_price:.2f}")


additional_choice = input("Would you like to purchase additional items? (yes/no): ").strip().lower()
if additional_choice == "yes":
    for category_name, item_list in zip(category[3:], item_codes[3:]):
        item_index = get_user_choice(category_name, item_list)
        additional_items.append((category_name, item_index))
        total_price += prices[category.index(category_name)][item_index]


    print("\nAdditional items:")
    for category_name, item_index in additional_items:
        print(f"{category_name}: {descriptions[category.index(category_name)][item_index]} - ${prices[category.index(category_name)][item_index]:.2f}")

    print(f"New total price: ${total_price:.2f}")


if len(additional_items) == 1:
    discount = total_price * 0.05
elif len(additional_items) >= 2:
    discount = total_price * 0.10
else:
    discount = 0

print(f"Discount: ${discount:.2f}")
final_price = total_price - discount
print(f"Final price after discount: ${final_price:.2f}")

print("Thank you for shopping with us!")
