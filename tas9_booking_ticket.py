#  Booking ticket with if control flow command
print("Welcome to the Olu.Oludayo Railway Ticket Booking System!")
print("Kindly note the Seats available: 1 to 50")

# Ask user if they want to continue
confirm = input("Do you wish to continue booking? (yes/no): ")

if confirm.lower() == "yes":
    print("Continue your Booking please !!!")

    # Create seats
    seat_number = set(range(1, 51))
    print("All available seats:", sorted(seat_number))

    # Ask user to pick a seat
    ticket = int(input("Select your seat from 1 to 50 to book your preferred seat: "))

    # Check if seat is available
    if ticket in seat_number:
        seat_number.remove(ticket)  # book the seat
        print(f"You have successfully booked seat {ticket}.")
    else:
        print("Sorry, that seat is already taken  Thank you.")
print(" Thank you for your booking ,see next time.!..!...!")