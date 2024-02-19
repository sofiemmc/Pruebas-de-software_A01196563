### 6.2 Ejercicio de programacion 3
### Sofia Mancias Carrillo - A01196563

class Hotel:
    def __init__(self, name, location, rooms_available):
        self.name = name
        self.location = location
        self.rooms_available = rooms_available
        self.reservations = []

    def create_hotel(self):
        with open("hotels.txt", "a") as file:
            file.write(f"{self.name},{self.location},{self.rooms_available}\n")

    @staticmethod
    def delete_hotel(name):
        with open("hotels.txt", "r") as file:
            lines = file.readlines()
        with open("hotels.txt", "w") as file:
            for line in lines:
                if not line.startswith(name):
                    file.write(line)

    @staticmethod
    def display_hotel_info(name):
        with open("hotels.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == name:
                    print("Hotel Name:", data[0])
                    print("Location:", data[1])
                    print("Available Rooms:", data[2])
                    break
            else:
                print("Hotel not found.")

    @staticmethod
    def modify_hotel_info(name, new_name=None, new_location=None, new_rooms_available=None):
        with open("hotels.txt", "r") as file:
            lines = file.readlines()
        with open("hotels.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == name:
                    if new_name:
                        data[0] = new_name
                    if new_location:
                        data[1] = new_location
                    if new_rooms_available is not None:
                        data[2] = str(new_rooms_available)
                    file.write(",".join(data) + "\n")
                else:
                    file.write(line)

    def reserve_room(self, customer_name, num_rooms):
        if num_rooms <= self.rooms_available:
            self.rooms_available -= num_rooms
            self.reservations.append((customer_name, num_rooms))
            with open("reservations.txt", "a") as file:
                file.write(f"{self.name},{customer_name},{num_rooms}\n")
            print(f"{num_rooms} room(s) reserved for {customer_name}")
        else:
            print("Insufficient rooms available.")

    def cancel_reservation(self, customer_name, num_rooms):
        for reservation in self.reservations:
            if reservation[0] == customer_name:
                self.rooms_available += reservation[1]
                self.reservations.remove(reservation)
                with open("reservations.txt", "r") as file:
                    lines = file.readlines()
                with open("reservations.txt", "w") as file:
                    for line in lines:
                        if not line.startswith(f"{self.name},{customer_name}"):
                            file.write(line)
                print(f"{num_rooms} room(s) reservation canceled for {customer_name}")
                break
        else:
            print("No reservation found for this customer.")

    def add_reservation(self, reservation):
        self.reservations.append(reservation)
