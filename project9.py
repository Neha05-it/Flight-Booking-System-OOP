from abc import ABC, abstractmethod


class Flight(ABC):

    total_flights = 0

    def __init__(self, flight_number, source, destination, price, seats):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self._price = price
        self._seats = seats
        Flight.total_flights += 1

    @property
    def price(self):
        return self._price

    @property
    def seats(self):
        return self._seats

    @classmethod
    def show_total_flights(cls):
        print("Total Flights:", cls.total_flights)

    @staticmethod
    def validate_seats(seats):
        return seats > 0

    @abstractmethod
    def calculate_fare(self):
        pass

    def display(self):
        print("----------------------------")
        print("Flight Number:", self.flight_number)
        print("From:", self.source)
        print("To:", self.destination)
        print("Price:", self.calculate_fare())
        print("Available Seats:", self.seats)


class DomesticFlight(Flight):

    def calculate_fare(self):
        return self._price


class InternationalFlight(Flight):

    def calculate_fare(self):
        return self._price + 3000


class Passenger:

    def __init__(self, name, age, passport):
        self.name = name
        self.age = age
        self.__passport = passport

    def display(self):
        print("Passenger Name:", self.name)
        print("Age:", self.age)
        print("Passport:", self.__passport)


class Booking:

    total_bookings = 0

    def __init__(self, passenger, flight):
        self.passenger = passenger
        self.flight = flight
        self.booking_id = Booking.total_bookings + 1
        Booking.total_bookings += 1

    def book(self):
        if self.flight._seats <= 0:
            print("No seats available!")
            return False

        self.flight._seats -= 1
        print("\nBooking Successful!")
        print("Booking ID:", self.booking_id)
        print("Flight:", self.flight.flight_number)
        print("Passenger:", self.passenger.name)
        print("Ticket Price:", self.flight.calculate_fare())
        return True

    def cancel(self):
        self.flight._seats += 1
        print("Booking Cancelled Successfully!")

    @staticmethod
    def show_total_bookings():
        print("Total Bookings:", Booking.total_bookings)


flights = [
    DomesticFlight("AI101", "Delhi", "Mumbai", 5000, 5),
    DomesticFlight("AI102", "Delhi", "Bangalore", 6000, 4),
    InternationalFlight("AI201", "Delhi", "Dubai", 12000, 3),
    InternationalFlight("AI202", "Delhi", "London", 25000, 2)
]

bookings = []


def show_flights():
    print("\n========== AVAILABLE FLIGHTS ==========")

    for flight in flights:
        flight.display()


def search_flight():
    number = input("Enter Flight Number: ").upper()

    for flight in flights:
        if flight.flight_number == number:
            print("\nFlight Found!")
            flight.display()
            return flight

    print("Flight Not Found!")
    return None


def book_flight():
    flight = search_flight()

    if flight is None:
        return

    name = input("Enter Passenger Name: ")
    age = int(input("Enter Passenger Age: "))
    passport = input("Enter Passport Number: ")

    passenger = Passenger(name, age, passport)
    booking = Booking(passenger, flight)

    if booking.book():
        bookings.append(booking)


def view_bookings():
    if len(bookings) == 0:
        print("No Bookings Found!")
        return

    print("\n========== ALL BOOKINGS ==========")

    for booking in bookings:
        print("----------------------------")
        print("Booking ID:", booking.booking_id)
        print("Passenger:", booking.passenger.name)
        print("Flight:", booking.flight.flight_number)
        print("From:", booking.flight.source)
        print("To:", booking.flight.destination)
        print("Fare:", booking.flight.calculate_fare())


def cancel_booking():
    try:
        booking_id = int(input("Enter Booking ID: "))

        for booking in bookings:
            if booking.booking_id == booking_id:
                booking.cancel()
                bookings.remove(booking)
                return

        print("Booking Not Found!")

    except ValueError:
        print("Please enter a valid Booking ID.")


def main_menu():

    while True:

        print("\n========== FLIGHT BOOKING SYSTEM ==========")
        print("1. Show Flights")
        print("2. Search Flight")
        print("3. Book Flight")
        print("4. View Bookings")
        print("5. Cancel Booking")
        print("6. Show Total Flights")
        print("7. Show Total Bookings")
        print("8. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            show_flights()

        elif choice == "2":
            search_flight()

        elif choice == "3":
            book_flight()

        elif choice == "4":
            view_bookings()

        elif choice == "5":
            cancel_booking()

        elif choice == "6":
            Flight.show_total_flights()

        elif choice == "7":
            Booking.show_total_bookings()

        elif choice == "8":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


main_menu()