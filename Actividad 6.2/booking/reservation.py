### 6.2 Ejercicio de programacion 3
### Sofia Mancias Carrillo - A01196563

class Reservation:
    def __init__(self, customer, hotel, num_rooms, check_in_date, check_out_date):
        self.customer = customer
        self.hotel = hotel
        self.num_rooms = num_rooms
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date

    def create_reservation(self):
        with open("reservations.txt", "a") as file:
            file.write(f"{self.hotel.name},{self.customer.name},{self.num_rooms},{self.check_in_date},{self.check_out_date}\n")
        print(f"Reservation made at {self.hotel.name} for {self.num_rooms} room(s).")

        # Agregar la reserva a la lista de reservas del hotel
        self.hotel.add_reservation(self)

    def cancel_reservation(self):
        with open("reservations.txt", "r") as file:
            lines = file.readlines()
        with open("reservations.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == self.hotel.name and data[1] == self.customer.name:
                    continue
                file.write(line)
        print("Reservation canceled.")
