'''Lab_1'''
import os
import splitter

try:
    number_of_ngrams: int = int(input("Enter N: "))
    top_k: int = int(input("Enter K: "))
    with open(r'/lab_1/data/file.txt', encoding = "utf8") as file_to_open:
        if os.path.getsize('/lab_1/data/file.txt') == 0:
            raise EOFError("File is empty")
        input_string: str = file_to_open.read
        splitter.Words.count_words
        print(f"\nMedian: {splitter.Words.find_median}")
        print(f"Average: {splitter.Words.find_average}\n")
        splitter.Letters.create_dictionary
        splitter.Letters.find_top
        file_to_open.close()

except ValueError as value_error:
    print(value_error)

except EOFError as exception:
    print(exception)
