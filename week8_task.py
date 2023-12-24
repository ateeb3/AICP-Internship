BOAT_COUNT = 10
HOURLY_RATE = 20
HALF_HOUR_RATE = 12
OPENING_TIME = 10
CLOSING_TIME = 17


boats = [{'hired': False, 'hours_hired': 0, 'return_time': None, 'money_taken': 0} for _ in range(BOAT_COUNT)]


def get_hire_duration():
    while True:
        try:
            hire_duration = float(input("Enter the hire duration (1 for one hour, 0.5 for half an hour): "))
            if hire_duration in [1, 0.5]:
                return hire_duration
            else:
                print("Invalid hire duration. Please enter 1 or 0.5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def simulate_time_passage(current_time, hours):
    new_time = current_time + hours
    return new_time if OPENING_TIME <= new_time <= CLOSING_TIME else current_time

# Task 1 - Calculate the money taken in a day for all boats
def calculate_daily_profit_for_all_boats(current_time):
    available_boats = [boat_number for boat_number, boat in enumerate(boats, start=1) if not boat['hired'] and OPENING_TIME <= current_time <= CLOSING_TIME]
    return available_boats


def find_next_available_boat(current_time):
    available_boats = calculate_daily_profit_for_all_boats(current_time)

    if available_boats:
        print(f"\nAvailable boats: {available_boats}")
        user_choice = int(input("Choose a boat to hire (or enter 0 to exit): "))
        if user_choice == 0:
            return None
        elif user_choice in available_boats:
            return user_choice
        else:
            print("Invalid choice. Please choose from the available boats.")
            return find_next_available_boat(current_time)
    else:
        return None


def calculate_total_money_and_hours():
    total_money = sum(boat['money_taken'] for boat in boats)
    total_hours = sum(boat['hours_hired'] for boat in boats)
    unused_boats = [i + 1 for i, boat in enumerate(boats) if not boat['hired']]
    most_used_boat = max(enumerate(boats, start=1), key=lambda x: x[1]['hours_hired'])[0]

    print("\nEnd of day report:")
    print(f"Total money taken: ${total_money:.2f}")
    print(f"Total hours hired: {total_hours:.2f} hours")
    print(f"Boats not used today: {unused_boats}")
    print(f"Boat {most_used_boat} was used the most today.")


current_time = 10

# Simulate hiring more boats
while current_time <= CLOSING_TIME:
    boat_choice = find_next_available_boat(current_time)
    if boat_choice is None:
        break

    boat = boats[boat_choice - 1]
    hire_duration = get_hire_duration()

    if hire_duration == 1:
        rate = HOURLY_RATE
    elif hire_duration == 0.5:
        rate = HALF_HOUR_RATE

    boat['hired'] = True
    boat['hours_hired'] += hire_duration
    boat['return_time'] = simulate_time_passage(current_time, hire_duration)
    boat['money_taken'] += rate * hire_duration
    current_time = simulate_time_passage(current_time, 1)

    if current_time >= CLOSING_TIME:
        print("Closing time reached. The program will now terminate.")
        break


calculate_total_money_and_hours()
