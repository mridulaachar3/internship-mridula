# Movie Ticket Booking System
num_customers = int(input("Enter number of customers: "))

total_collection = 0

for i in range(num_customers):

    print("\n-------------------------")
    print("Customer", i + 1)

    name = input("Enter customer name: ")
    age = int(input("Enter age: "))

    if age <= 0:
        print("Invalid age entered. Moving to next customer.")
        continue

    movie_type = input("Enter movie type (2D / 3D / IMAX): ").upper()

    while True:
        tickets = int(input("Enter number of tickets: "))

        if tickets <= 0:
            print("Please enter at least 1 ticket.")
            continue

        if tickets > 10:
            print("Maximum 10 tickets allowed per booking.")
            continue

        break

    if movie_type == "2D":
        price = 150
    elif movie_type == "3D":
        price = 220
    elif movie_type == "IMAX":
        price = 300
    else:
        print("Invalid movie type. Using 2D ticket price.")
        price = 150

    amount = price * tickets

    discount = 0

    if age < 12 or age >= 60:
        if tickets >= 4:
            discount = 20
        else:
            discount = 15
    else:
        if tickets >= 6:
            discount = 10
        elif tickets >= 4:
            discount = 5

    discount_amount = (amount * discount) / 100
    final_amount = amount - discount_amount

    total_collection += final_amount

    
    print("\nBooking Details")
    print("-------------------------")
    print("Customer Name :", name)
    print("Age           :", age)
    print("Movie Type    :", movie_type)
    print("Tickets       :", tickets)
    print("Amount        :", amount)
    print("Discount      :", discount, "%")
    print("Final Amount  :", final_amount)

    if final_amount > 0:
        print("Booking Status: CONFIRMED")
    else:
        print("Booking Status: FAILED")

print("\n=========================")
print("All bookings completed.")
print("Total Collection Today:", total_collection)