'''Lab_1'''
import os
from splitter import Words, Letters

try:
    number_of_ngrams: int = int(input("Enter N: "))
    top_k: int = int(input("Enter K: "))
    if number_of_ngrams == 0 or top_k == 0:
        raise ValueError("Incorrect input")
    with open(r'/lab_1/data/file.txt', encoding = "utf8") as file_to_open:
        if os.path.getsize('/lab_1/data/file.txt') == 0:
            raise EOFError("File is empty")
        input_string: str = file_to_open.read()
        words: Words = Words(input_string, top_k, number_of_ngrams)
        letters: Letters = Letters(input_string, top_k, number_of_ngrams)
        words.count_words()
        words.print_dictionary()
        print(f"\nMedian: {words.find_median()}")
        print(f"Average: {words.find_average()}\n")
        letters.create_dictionary()
        letters.find_top()
        file_to_open.close()

except ValueError as value_error:
    print(value_error)

except EOFError as exception:
    print(exception)
