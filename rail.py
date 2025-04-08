# Railway Ticket Booking System

class RailwaySystem:
    def __init__(self):
        self.trains = {
            101: {'name': 'Express A', 'seats': 5},
            102: {'name': 'Express B', 'seats': 3},
            103: {'name': 'Express C', 'seats': 4}
        }
        self.bookings = {}  # Format: {booking_id: {'train_id': int, 'passenger': str}}

        self.booking_id_counter = 1

    def view_trains(self):
        print("\nAvailable Trains:")
        for train_id, info in self.trains.items():
            print(f"Train {train_id}: {info['name']} - Seats Available: {info['seats']}")

    def book_ticket(self, train_id, passenger_name):
        if train_id not in self.trains:
            print("Invalid train ID.")
            return

        if self.trains[train_id]['seats'] > 0:
            booking_id = self.booking_id_counter
            self.bookings[booking_id] = {'train_id': train_id, 'passenger': passenger_name}
            self.trains[train_id]['seats'] -= 1
            self.booking_id_counter += 1
            print(f"Booking successful! Booking ID: {booking_id}")
        else:
            print("No seats available on this train.")

    def cancel_ticket(self, booking_id):
        if booking_id in self.bookings:
            train_id = self.bookings[booking_id]['train_id']
            self.trains[train_id]['seats'] += 1
            del self.bookings[booking_id]
            print("Booking canceled successfully.")
        else:
            print("Invalid booking ID.")

    def view_bookings(self):
        if not self.bookings:
            print("No bookings found.")
            return
        print("\nBooked Tickets:")
        for bid, info in self.bookings.items():
            train = self.trains[info['train_id']]['name']
            print(f"Booking ID: {bid} | Train: {train} | Passenger: {info['passenger']}")

def main():
    system = RailwaySystem()
    
    while True:
        print("\n--- Railway Ticket Booking System ---")
        print("1. View Trains")
        print("2. Book Ticket")
        print("3. Cancel Ticket")
        print("4. View Bookings")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            system.view_trains()
        elif choice == '2':
            name = input("Enter passenger name: ")
            train_id = int(input("Enter train ID: "))
            system.book_ticket(train_id, name)
        elif choice == '3':
            booking_id = int(input("Enter booking ID to cancel: "))
            system.cancel_ticket(booking_id)
        elif choice == '4':
            system.view_bookings()
        elif choice == '5':
            print("Thank you for using the Railway Ticket Booking System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

