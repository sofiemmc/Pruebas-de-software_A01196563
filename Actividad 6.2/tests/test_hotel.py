### 6.2 Ejercicio de programacion 3
### Sofia Mancias Carrillo - A01196563

import unittest
from booking.hotel import Hotel
import io
import unittest.mock

class TestHotel(unittest.TestCase):
    def test_create_hotel(self):
        # Prueba para crear un hotel
        hotel1 = Hotel("Hilton", "San Antonio", 10)
        hotel1.create_hotel()
        hotel2 = Hotel("Holiday Inn", "Laredo", 3)
        hotel2.create_hotel()
        hotel3 = Hotel("Embassy Suits", "Austin", 7)
        hotel3.create_hotel()

        # Verificar que los hoteles se hayan agregado al archivo de hoteles
        with open("hotels.txt", "r") as file:
            hotels = file.readlines()
            self.assertTrue(any("Hilton,San Antonio" in line for line in hotels))
            self.assertTrue(any("Holiday Inn,Laredo" in line for line in hotels))
            self.assertTrue(any("Embassy Suits,Austin" in line for line in hotels))

    def test_delete_hotel(self):
        # Prueba para eliminar un hotel
        hotel2 = Hotel("Holiday Inn", "Laredo", 3)

        hotel2.delete_hotel("Holiday Inn")

        # Verificar que el Holiday Inn se haya eliminado del archivo de hoteles
        with open("hotels.txt", "r") as file:
            hotels = file.readlines()
            self.assertTrue(any("Hilton" in line for line in hotels))
            self.assertFalse(any("Holiday Inn" in line for line in hotels))
            self.assertTrue(any("Embassy Suits" in line for line in hotels))

    def test_display_hotel_info(self):
        # Prueba para mostrar la información de un hotel
        with open("hotels.txt", "w") as file:
            file.write("Hilton,San Antonio,10\n")
            file.write("Embassy Suits,Austin,7\n")
            file.write("Holiday Inn,Laredo,3\n")

        # Llamamos al método display_hotel_info para Embassy Suits y verificamos la salida
        expected_output = "Hotel Name: Hilton\nLocation: San Antonio\nAvailable Rooms: 10\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            Hotel.display_hotel_info("Hilton")
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_modify_hotel_info(self):

        # Llamamos al método modify_hotel_info para Embassy Suits y verificamos que se haya modificado correctamente
        Hotel.modify_hotel_info("Embassy Suits", new_name="Marriott", new_location="Austin", new_rooms_available=25)
        with open("hotels.txt", "r") as file:
            lines = file.readlines()
            self.assertTrue(any("Marriott,Austin,25" in line for line in lines))

    def test_reserve_room(self):
        # Prueba para reservar una habitación en un hotel
        hotel = Hotel("Hilton", "San Antonio", 10)

        hotel.reserve_room("John Doe", 1)
        hotel.reserve_room("Jane Smith", 2)

        # Verificar que las reservaciones se hayan registrado correctamente
        self.assertEqual(len(hotel.reservations), 2)
        self.assertEqual(hotel.rooms_available, 7)  # 10 habitaciones iniciales - 3 habitaciones reservadas

    def test_cancel_reservation(self):
        # Prueba para cancelar una reservación en un hotel
        hotel = Hotel("Hilton", "San Antonio", 10)

        hotel.reserve_room("John Doe", 1)
        hotel.reserve_room("Jane Smith", 2)

        # Cancelar la reservación de Jane Smith
        hotel.cancel_reservation("Jane Smith", 1)

        # Verificar que la reservación de Jane Smith se haya cancelado correctamente
        self.assertEqual(len(hotel.reservations), 1)
        self.assertEqual(hotel.rooms_available, 9)  # Se liberó una habitación

if __name__ == "__main__":
    unittest.main()
