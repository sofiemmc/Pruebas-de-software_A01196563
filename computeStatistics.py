###4.2 Ejercicio de programacion 1 - P1
###Sofia Mancias Carrillo - A01196563

import os
import sys
import time
import pandas as pd


def read_file(filename):
    """Read the files."""
    data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                cleaned_line = ''.join(char for char in line if char.isdigit() or char == '.')
                cleaned_line = ''.join(char if char.isdigit() or char in '.-' else ' ' for char in line)
                try:
                    number = float(cleaned_line.strip())
                    data.append(number)
                except ValueError:
                    print(f"Ignoring invalid value: {cleaned_line.strip()}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    return data


def mean(data):
    """Define the mean."""
    if not data:
        return None
    return sum(data) / len(data)


def median(data):
    """Define the meadian."""
    if not data:
        return None
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]



def mode(data):
    """Define the mode."""
    # it seems we have more than one mode for some, we are going to stick to just dislaying one value to be as accurate to the teachers results
    if not data:
        return None
    frequency = 0

    for number in data:
        n = data.count(number)
        if n > frequency:
            frequency = n
    mode = []

    for number in data:
        n = data.count(number)
        if n == frequency and number not in mode:
            mode.append(number)
    if len (mode) != len (data):
        return mode[0]
    else:
        return None


def standard_deviation(data):
    """Define the standard deviation."""
    if not data:
        return None
    # it seems that to match the teacher result we have to use a different formula than in def variance() taking out the -1
    mean_value = mean(data)
    sta_dev = sum((x - mean_value) ** 2 for x in data) / len(data)
    return sta_dev ** 0.5


def variance(data):
    """Define the variance."""
    if not data:
        return None
    mean_value = mean(data)
    return sum((x - mean_value) ** 2 for x in data) / (len(data) - 1)


def compute_statistics(filepath):
    """Compute descriptive statistics for the file."""
    data = read_file(filepath)
    if not data:
        print(f"No valid data found in the file '{filepath}'.")
        return None, None, None, None, None, None

    # count here is going to dispay count after cleaning the data in def read_file()
    count_val = len(data)
    mean_val = mean(data)
    median_val = median(data)
    mode_val = mode(data)
    std_deviation_val = standard_deviation(data)
    variance_val = variance(data)

    return count_val, mean_val, median_val, mode_val, std_deviation_val, variance_val


def main():
    """Get together all the data for the file."""
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py /path/to/folder")
        return

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Folder '{folder_path}' not found.")
        return

    start_time = time.time()

    file_statistics = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            file_name_no_ext = os.path.splitext(file_name)[0]
            count_val, mean_val, median_val, mode_val, std_deviation_val, variance_val = compute_statistics(file_path)
            file_statistics.append((file_name_no_ext, count_val, mean_val, median_val, mode_val, std_deviation_val, variance_val))

    end_time = time.time()
    elapsed_time = end_time - start_time

    columns = ['TC', 'COUNT', 'MEAN', 'MEDIAN', 'MODE', 'SD', 'VARIANCE']
    statistics_df = pd.DataFrame(file_statistics, columns=columns, index=None)
    statistics_df = statistics_df.transpose()

    print(statistics_df)
    print(f"Time elapsed: {elapsed_time} seconds")

    statistics_df.to_csv("StatisticsResults.txt", sep='\t')

    with open("StatisticsResults.txt", 'a') as results_file:
        results_file.write("\nTime elapsed: {} seconds\n".format(elapsed_time))


if __name__ == "__main__":
    main()
