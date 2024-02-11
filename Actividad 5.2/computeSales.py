### 5.2 Ejercicio de programacion 2
### Sofia Mancias Carrillo - A01196563

import json
import sys
import time


def read_files(price_file, sales_file):
    """Read the files."""
    try:
        with open(price_file, 'r') as f:
            price_data = json.load(f)
            if not isinstance(price_data, list):
                price_data = [price_data]
        with open(sales_file, 'r') as f:
            sales_data = json.load(f)
        return price_data, sales_data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error: {e}.")
        return {}, []


def calculate_total_cost(price_data, sales_data):
    """Calculate the total cost for all sales."""
    total_cost = 0
    for sale in sales_data:
        item_name = sale['Product']
        # We verify if the product is in the list
        for product in price_data:
            if product['title'] == item_name:
                price = product['price']
                total_cost += sale['Quantity'] * price
                break
        else:
            print(f"Warning: The product '{item_name}' was not found in the product list.")
    return total_cost


def main():
    """In the main function get together all the data for the file."""
    if len(sys.argv) != 3:
        print("Error: Most input 2 files for this code.")
        print("Usage: python computeSales.py priceCatalogue.json salesRecord.json")
        return

    price_file = sys.argv[1]
    sales_file = sys.argv[2]
    start_time = time.time()
    price_data, sales_data = read_files(price_file, sales_file)
    total_cost = calculate_total_cost(price_data, sales_data)
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Total Sale: ${total_cost:.2f}")
    print(f"Time elapsed: {elapsed_time} seconds")
    with open('SalesResults.txt', 'w') as results_file:
        results_file.write(f"Total Sale: ${total_cost:.2f}\n")
        results_file.write(f"Time elapsed: {elapsed_time} seconds")


if __name__ == "__main__":
    main()
