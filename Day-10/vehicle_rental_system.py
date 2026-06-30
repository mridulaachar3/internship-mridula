# Vehicle Rental Management System

from abc import ABC, abstractmethod


# Vehicle is abstract, cant make an object of it directly
# every subclass HAS to write its own rental_price()
class Vehicle(ABC):

    def __init__(self, vehicle_id, name, is_available=True):
        self.vehicle_id = vehicle_id
        self.name = name
        self._is_available = is_available   # single underscore = protected
        self.__rental_count = 0              # double underscore = private

    @abstractmethod
    def rental_price(self):
        pass   # no logic here, child classes define their own

    def is_available(self):
        return self._is_available

    def mark_rented(self):
        self._is_available = False
        self.__rental_count += 1

    def mark_returned(self):
        self._is_available = True

    def get_rental_count(self):
        # cant access __rental_count directly from outside, need this getter
        return self.__rental_count

    def show_info(self):
        status = "Available" if self._is_available else "Rented out"
        print(f"  [{self.vehicle_id}] {self.name} - Rs.{self.rental_price()}/day - {status}")


# inheritance - Car, Bike, Scooter all inherit Vehicle

class Car(Vehicle):
    def __init__(self, vehicle_id, name, seats, is_available=True):
        super().__init__(vehicle_id, name, is_available)
        self.seats = seats

    def rental_price(self):
        # polymorphism - same method name as bike/scooter but diff calculation
        return 2000 + (self.seats * 100)


class Bike(Vehicle):
    def __init__(self, vehicle_id, name, cc, is_available=True):
        super().__init__(vehicle_id, name, is_available)
        self.cc = cc

    def rental_price(self):
        return 500 + (self.cc // 10)


class Scooter(Vehicle):
    def __init__(self, vehicle_id, name, is_available=True):
        super().__init__(vehicle_id, name, is_available)

    def rental_price(self):
        return 300   # flat rate, doesnt depend on anything


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.rented_vehicles = []

    def add_rental(self, vehicle_id):
        self.rented_vehicles.append(vehicle_id)


# this class handles everything - adding, booking, returns
class RentalManager:
    def __init__(self):
        self.vehicles = []
        self.customers = {}

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Added {vehicle.name} to fleet.")

    def show_available_vehicles(self):
        print("\n--- Available Vehicles ---")
        found = False
        for v in self.vehicles:
            if v.is_available():
                v.show_info()
                found = True
        if not found:
            print("  Nothing available right now.")

    def show_all_vehicles(self):
        print("\n--- All Vehicles ---")
        # this works the same for Car, Bike or Scooter objects - polymorphism
        for v in self.vehicles:
            v.show_info()

    def book_vehicle(self, vehicle_id, customer_name, customer_phone):
        vehicle = None
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                vehicle = v
                break

        if vehicle is None:
            print("Vehicle not found.")
            return

        if not vehicle.is_available():
            print(f"{vehicle.name} is already rented out.")
            return

        if customer_name not in self.customers:
            self.customers[customer_name] = Customer(customer_name, customer_phone)

        customer = self.customers[customer_name]
        customer.add_rental(vehicle_id)
        vehicle.mark_rented()

        print(f"\nBooking confirmed!")
        print(f"  Customer : {customer_name}")
        print(f"  Vehicle  : {vehicle.name}")
        print(f"  Price    : Rs.{vehicle.rental_price()}/day")

    def return_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                v.mark_returned()
                print(f"{v.name} returned. Rented {v.get_rental_count()} time(s) total.")
                return
        print("Vehicle not found.")


# main

manager = RentalManager()

manager.add_vehicle(Car("C001", "Honda City", seats=5))
manager.add_vehicle(Car("C002", "Swift Dzire", seats=4))
manager.add_vehicle(Bike("B001", "Royal Enfield", cc=350))
manager.add_vehicle(Bike("B002", "Pulsar", cc=150))
manager.add_vehicle(Scooter("S001", "Activa"))

manager.show_all_vehicles()

while True:
    print("\n=== Vehicle Rental System ===")
    print("1. Show available vehicles")
    print("2. Show all vehicles")
    print("3. Book a vehicle")
    print("4. Return a vehicle")
    print("5. Exit")

    choice = input("Choose: ").strip()

    if choice == "1":
        manager.show_available_vehicles()

    elif choice == "2":
        manager.show_all_vehicles()

    elif choice == "3":
        v_id = input("Vehicle ID (eg. C001): ").strip()
        cust_name = input("Customer name: ").strip()
        cust_phone = input("Customer phone: ").strip()
        manager.book_vehicle(v_id, cust_name, cust_phone)

    elif choice == "4":
        v_id = input("Vehicle ID to return: ").strip()
        manager.return_vehicle(v_id)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, pick 1-5.")