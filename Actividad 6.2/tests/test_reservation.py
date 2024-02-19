### 6.2 Ejercicio de programacion 3
### Sofia Mancias Carrillo - A01196563

import unittest
from booking.reservation import Reservation
from booking.customer import Customer
from booking.hotel import Hotel

class TestReservation(unittest.TestCase):
    def setUp(self):
        # Configuramos dos hoteles de ejemplo
        self.hotel1 = Hotel("Hilton", "San Antonio", 10)
        self.hotel2 = Hotel("Marriott", "Austin", 25)

        # Configuramos dos clientes de ejemplo
        self.customer1 = Customer("John Doe", "johndoe@example.com")
        self.customer2 = Customer("Jane Smith", "janesmith@example.com")

    def test_create_reservation(self):
        # Prueba para crear una reserva
        reservation1 = Reservation(self.customer1, self.hotel1, 1, "10/3/2024", "12/3/2024")
        reservation1.create_reservation()
        reservation2 = Reservation(self.customer2, self.hotel2, 2, "1/3/2024", "6/3/2024")
        reservation2.create_reservation()

        # Verificar que las reservas se hayan registrado correctamente
        self.assertEqual(len(self.hotel1.reservations), 1)
        self.assertEqual(len(self.hotel2.reservations), 1)

    def test_cancel_reservation(self):
        # Prueba para cancelar una reserva
        reservation1 = Reservation(self.customer1, self.hotel1, 1, "10/3/2024", "12/3/2024")
        reservation1.create_reservation()
        reservation2 = Reservation(self.customer2, self.hotel2, 2, "1/3/2024", "6/3/2024")
        reservation2.create_reservation()

        # Cancelamos la reserva usando las instancias previamente configuradas
        reservation1.cancel_reservation()

        # Verificar que la reserva se haya cancelado correctamente
        self.assertEqual(len(self.hotel1.reservations), 1)
        self.assertEqual(len(self.hotel2.reservations), 1)

if __name__ == "__main__":
    unittest.main()
