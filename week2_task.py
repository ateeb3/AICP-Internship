
departure_times = ["09:00", "11:00", "13:00", "15:00"]
departure_seats = [480, 480, 480, 480]
departure_passengers = [0, 0, 0, 0]
departure_money_total = [0.0, 0.0, 0.0, 0.0]

return_times = ["10:00", "12:00", "14:00", "16:00"]
return_seats = [480, 480, 480, 640]
return_passengers = [0, 0, 0, 0]
return_money_total = [0.0, 0.0, 0.0, 0.0]


def display_schedule():
    print("\n\t\t\t\tTRAIN JOURNEY DISPLAY\n")
    for index in range(0, 4):
        if departure_seats[index] != 0:
            print(
                "Journey No:",index + 1,
                "| Departure Hour:",departure_times[index],
                "\t| Tickets available:",departure_seats[index],
            )
        else:
            print(
                "Journey No:", index + 1,
                "| Departure Hour:",departure_times[index],
                "\t| Closed!",
            )

        if return_seats[index] != 0:
            print(
                "Journey No:",index + 1,
                "| Return Hour:", return_times[index],
                "\t| Tickets available:",return_seats[index],
            )
        else:
            print(
                "Journey No:", index + 1,
                "| Return Hour:",return_times[index],
                "\t| Closed!",
            )
        print()




display_schedule()

num_of_passengers = up_trip = down_trip = free_tickets = 0
one_way_ticket = 25.0
one_way_cost = 0.0


choice = input("Do you want to buy ticket(s)? Enter Yes or No: ")
while choice.lower() != "yes" and choice.lower() != "no":
    choice = input("Invalid Input! Enter Yes or No: ")

while choice.lower() != "no":


    up_trip = int(input("Enter Journey number for your chosen departure hour: ")) - 1
    while up_trip not in range(0, 4):
        up_trip = int(input("Error! Enter Journey number from (1 to 4): "))-1

    print("\n\t\t Return Hours Available\n")
    for num in range(up_trip, 4):
        print(
            "Journey No:",num + 1,
            " | Return Hour:",return_times[num],
            " | Remaining Tickets:",return_seats[num],
        )
    print()
    down_trip = int(input("Enter Journey number for your chosen Return hour: ")) - 1
    while down_trip < up_trip or down_trip > 3:
        down_trip = int(
            input("Error! Enter Journey number from the given list above: ") - 1
        )
    #
    print()
    num_of_passengers = int(input("Enter number of passengers for the trip: "))
    while num_of_passengers <= 0:
        num_of_passengers = int(input("Error! Enter a number greater than 0: "))

    if (
        num_of_passengers > departure_seats[up_trip]
        or num_of_passengers > return_seats[down_trip]
    ):

        print("Seats not available for chosen hours")
        print("Please check the display below for available Seats =>")
    else:
        print("\n!!! Seats Booked !!!")
        if 10 <= num_of_passengers <= 80:
            free_tickets = num_of_passengers // 10
        else:
            free_tickets = 0
        one_way_cost = (num_of_passengers - free_tickets) * one_way_ticket
        print("Total price for a two-way journey: $", one_way_cost * 2, sep="")
        #
        departure_passengers[up_trip] += num_of_passengers
        departure_seats[up_trip] -= num_of_passengers
        departure_money_total[up_trip] += one_way_cost
        #
        return_passengers[down_trip] += num_of_passengers
        return_seats[down_trip] -= num_of_passengers
        return_money_total[down_trip] += one_way_cost

    display_schedule()

    choice = input("Do you want to buy ticket(s)? Enter Yes or No: ")
    while choice.lower() != "yes" and choice.lower() != "no":
        choice = input("Invalid Input! Enter Yes or No: ")


total_amount = 0.0
total_passengers = 0
max_train = ""
most_passengers = 0


print("\n")
print("END OF THE DAY")
print("\n")
for count in range(0, 4):
    print(
        "Journey No:",count + 1,
        "\t| Departure Hour:",departure_times[count],
        "\t| Number of passengers:",departure_passengers[count],
        "\t| Total money: $",departure_money_total[count],sep="",
    )
    print(
        "Journey No:",count + 1,
        "\t| Return Hour:",return_times[count],
        "\t| Number of passengers:",return_passengers[count],
        "\t| Total money: $",return_money_total[count],sep="",
    )


for index in range(0, 4):
    total_passengers += departure_passengers[index]
    total_amount += departure_money_total[index] * 2
for count in range(0, 4):
    if departure_passengers[count] > most_passengers:
        most_passengers = departure_passengers[count]
        max_train = departure_times[count]
    if return_passengers[count] > most_passengers:
        most_passengers = return_passengers[count]
        max_train = return_times[count]

print("Total money earned today: $", total_amount, sep="")
print("Total passengers traveled today:", total_passengers)
print("The train journey with the highest number of passengers today:", max_train)
input("Press Enter to Exit!")
