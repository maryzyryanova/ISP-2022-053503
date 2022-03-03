'''Lab_1'''
import array
import re
import os
from statistics import median

from isort import file

def count_words(input_string) -> dict:
    '''Count amount of words in the text'''
    arr: array = re.split(r'\, |\. |\; |\! |\? |\... |\ |\!|\.|\?|\...|\,|\;', input_string)
    check_empty(arr)
    dictionary: dict = {}
    for arr_element in arr:
        if arr_element != 0 :
            if not dictionary.get(arr_element) :
                dictionary[arr_element] = 1
            else:
                dictionary[arr_element] += 1
    return dictionary

def print_dictionary(dictionary) -> None:
    '''Function to print dictionary'''
    for key, value in dictionary.items():
        print(f"{value} - {key}")

def check_empty(arr) -> None:
    '''Check string on empty elements'''
    if arr.__contains__('') :
        arr.remove('')

def create_dictionary(number_of_ngrams, input_string) -> dict:
    '''Creating and using dictionary'''
    arr: array = re.split(r'\, |\. |\; |\! |\? |\... |\ |\!|\.|\?|\...|\,|\;', input_string)
    check_empty(arr)
    output: str = "".join(arr)
    dictionary: dict = {}
    for i in range(0, len(output) - number_of_ngrams + 1, 1):
        temp: str = ''
        for j in range (i, i + number_of_ngrams):
            temp += output[j]
        if temp != '' :
            if not dictionary.get(temp) :
                dictionary[temp] = 1
            else:
                dictionary[temp] += 1
    return dictionary

def find_top(dictionary, top_k) -> None:
    '''Finding top K amount of n-grams'''
    sorted_dictionary: dict = {}
    sorted_values: dict = sorted(dictionary, key = dictionary.get)
    counter: int = 0
    for s_v in sorted_values:
        sorted_dictionary[s_v] = dictionary[s_v]
        counter += 1
    if counter < top_k :
        print_dictionary(sorted_dictionary)
    else:
        dictionary: dict = reversed(list(sorted_dictionary.items()))
        print_top(dictionary, top_k)

def print_top(dictionary, top_k) -> None:
    '''Function to print top K elements'''
    k: int = 0
    for key, value in dictionary.items():
        if k >= top_k :
            break
        print(f"{value} - {key}")
        k += 1

def main() -> None:
    '''Main function'''
    try:
        number_of_ngrams: int = int(input("Enter N: "))
        top_k: int = int(input("Enter K: "))
        with open(r'/lab_1/data/file.txt', encoding = "utf8") as file_to_open:
            if os.path.getsize('/lab_1/data/file.txt') == 0:
                raise EOFError("File is empty")
            input_string: str = file_to_open.read()
            dictionary: dict = count_words(input_string)
            print(f"\nMedian: {median(dictionary.values())}")
            print(f"Average: {sum(dictionary.values()) / len(dictionary.values())}\n")
            dictionary: dict = create_dictionary(number_of_ngrams, input_string)
            find_top(dictionary, top_k)
            file_to_open.close()

    except ValueError as value_error:
        print(value_error)

    except EOFError as exception:
        print(exception)

main()
