###4.2 Ejercicio de programacion 1 - P2
###Sofia Mancias Carrillo - A01196563

import sys
import time
import pandas as pd

def read_file(filename):
    """Read the files."""
    try:
        with open(filename, 'r') as file:
            numbers = [line.strip() for line in file.readlines()]
        return numbers
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


def convert_to_binary(data):
    """Convert our data into binary."""
    try:
        data = int(data)
    except ValueError:
        print("Error: invalid value.")
        return "Error"

    if data < 0:
        sign = "-"
        data = abs(data)
    else:
        sign = ""

    binary_digits = []

    while data > 0:
        remainder = data % 2
        binary_digits.append(remainder)
        data = data // 2

    if not binary_digits:
        return '0'

    binary_digits.reverse()
    binary_number = ''.join(map(str, binary_digits))

    return binary_number


def convert_to_hexadecimal(data):
    """Convert our data into hexadecimals."""
    try:
        data = int(data)
    except ValueError:
        print("Error: invalid value.")
        return "Error"

    hexadecimal_digits = []
    hex_chars = "0123456789ABCDEF"
    if data == 0:
        return "0"
    if data < 0:
        data = (1 << 32) + data

    while data > 0:
        remainder = data % 16
        hexadecimal_digits.append(hex_chars[remainder])
        data //= 16
    hexadecimal_digits.reverse() 
    hexadecimal_number = ''.join(hexadecimal_digits)
    return hexadecimal_number


def main():
    """Get together all the data for the file."""
    if len(sys.argv) < 2:
        print("Usage: python convertNumbers.py dataFile.txt")
        return

    input_file = sys.argv[1]
    numbers = read_file(input_file)

    if not numbers:
        return

    start_time = time.time()

    results = []

    for number in numbers:
        binary = convert_to_binary(number)
        hexadecimal = convert_to_hexadecimal(number)

        if binary is not None and hexadecimal is not None:
            results.append((number, binary, hexadecimal))
        else:
            print(f"Error: The data '{number}' is invalid.")

    end_time = time.time()
    elapsed_time = end_time - start_time

    columns = ['File Num', 'BIN', 'HEX']
    convert_df = pd.DataFrame(results, columns=columns)

    print(convert_df)
    print(f"Time elapsed: {elapsed_time} seconds")

    convert_df.to_csv("ConversionResults.txt", sep='\t')

    with open("ConversionResults.txt", 'a') as results_file:
        results_file.write("\nTime elapsed: {} seconds\n".format(elapsed_time))

if __name__ == "__main__":
    main()
