### 6.2 Ejercicio de programacion 3
### Sofia Mancias Carrillo - A01196563

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_customer(self):
        with open("customers.txt", "a") as file:
            file.write(f"{self.name},{self.email}\n")

    @staticmethod
    def delete_customer(name):
        with open("customers.txt", "r") as file:
            lines = file.readlines()
        with open("customers.txt", "w") as file:
            for line in lines:
                if not line.startswith(name):
                    file.write(line)

    @staticmethod
    def display_customer_info(name):
        with open("customers.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if data[0] == name:
                    print("Customer Name:", data[0])
                    print("Email:", data[1])
                    break
            else:
                print("Customer not found.")

    @staticmethod
    def modify_customer_info(name, new_name=None, new_email=None):
        with open("customers.txt", "r") as file:
            lines = file.readlines()
        with open("customers.txt", "w") as file:
            for line in lines:
                data = line.strip().split(",")
                if data[0] == name:
                    if new_name:
                        data[0] = new_name
                    if new_email:
                        data[1] = new_email
                    file.write(",".join(data) + "\n")
                else:
                    file.write(line)
