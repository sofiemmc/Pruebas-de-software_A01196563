###4.2 Ejercicio de programacion 1 - P3
###Sofia Mancias Carrillo - A01196563

import sys
import time
import pandas as pd

def read_file(file_name):
    """Read the files."""
    try:
        with open(file_name, 'r') as file:
            words = [word.strip() for line in file for word in line.split()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return []


def calculate_word_frequencies(words):
    """Calculate the frequency of each word."""
    word_count = {}
    for word in words:
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count


def main():
    """Get together all the data for the file."""
    if len(sys.argv) < 2:
        print("Usage: python wordCount.py fileWithData.txt")
        return

    file_name = sys.argv[1]
    words = read_file(file_name)
    if not words:
        return

    total_words = len(words)

    start_time = time.time()
    word_count = calculate_word_frequencies(words)
    end_time = time.time()
    elapsed_time = end_time - start_time

    count_df = pd.DataFrame(list(word_count.items()), columns=['Words', 'Frequency'])
    count_df = count_df.sort_values(by='Frequency', ascending=False)
    count_df.to_csv("WordCountResults.txt", index=False,  sep='\t')

    print(count_df)
    print(f"\nTotal words processed: {total_words}")
    print(f"Time elapsed: {elapsed_time} seconds")

    with open("WordCountResults.txt", 'a') as results_file:
        results_file.write(f"\nTotal words processed: {total_words}")
        results_file.write(f"\nTime elapsed: {elapsed_time} seconds")


if __name__ == "__main__":
    main()
