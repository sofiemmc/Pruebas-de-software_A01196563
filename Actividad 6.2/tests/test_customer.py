### 6.2 Ejercicio de programacion 3
### Sofia Mancias Carrillo - A01196563

import unittest
from booking.customer import Customer

class TestCustomer(unittest.TestCase):
    def test_create_customer(self):
        # Prueba para crear un cliente
        customer1 = Customer("John Doe", "johndoe@example.com")
        customer1.create_customer()
        customer2 = Customer("Jane Smith", "janesmith@example.com")
        customer2.create_customer()

        # Verificar que los clientes se hayan agregado al archivo de clientes
        with open("customers.txt", "r") as file:
            customers = file.readlines()
            self.assertTrue(any("John Doe,johndoe@example.com" in line for line in customers))
            self.assertTrue(any("Jane Smith,janesmith@example.com" in line for line in customers))

    def test_delete_customer(self):
        # Prueba para eliminar un cliente
        customer1 = Customer("John Doe", "johndoe@example.com")
        customer2 = Customer("Jane Smith", "janesmith@example.com")
        customer1.create_customer()
        customer2.create_customer()

        # Eliminar uno de los clientes
        customer1.delete_customer("John Doe")

        # Verificar que el cliente eliminado no esté en el archivo de clientes
        with open("customers.txt", "r") as file:
            customers = file.readlines()
            self.assertFalse(any("John Doe,johndoe@example.com" in line for line in customers))
            self.assertTrue(any("Jane Smith,janesmith@example.com" in line for line in customers))

    # Otros métodos de prueba para los diferentes comportamientos de la clase Customer

if __name__ == "__main__":
    unittest.main()
