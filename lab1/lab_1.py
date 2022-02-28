'''Lab_1'''
import re
from statistics import median

def count_words(input_string):
    '''Count amount of words in the text'''
    arr = re.split(r'\, |\. |\; |\! |\? |\... |\ |\!|\.|\?|\...|\,|\;', input_string)
    check_empty(arr)
    dictionary = {}
    for arr_element in enumerate(arr):
        if arr_element != 0 :
            if not dictionary.get(arr_element) :
                dictionary[arr_element] = 1
            else:
                dictionary[arr_element] += 1
    for key, value in dictionary.items():
        print(f"{value} - {key}")
    return dictionary

def check_empty(arr):
    '''Check string on empty elements'''
    if arr.__contains__('') :
        arr.remove('')

def create_dictionary(number_of_ngrams, input_string):
    '''Creating and using dictionary'''
    arr = re.split(r'\, |\. |\; |\! |\? |\... |\ |\!|\.|\?|\...|\,|\;', input_string)
    check_empty(arr)
    output = "".join(arr)
    dictionary = {}
    for i in range(0, len(output) - number_of_ngrams + 1, 1):
        temp = ''
        for j in range (i, i + number_of_ngrams):
            temp += output[j]
        if temp != '' :
            if not dictionary.get(temp) :
                dictionary[temp] = 1
            else:
                dictionary[temp] += 1
    return dictionary

def find_top(dictionary, top_k):
    '''Finding top K amount of n-grams'''
    sorted_dictionary = {}
    sorted_values = sorted(dictionary, key = dictionary.get)
    counter = 0
    for s_v in sorted_values:
        sorted_dictionary[s_v] = dictionary[s_v]
        counter += 1
    if counter < top_k :
        for key, value in sorted_dictionary.items():
            print(f"{value} - {key}")
    else:
        reversed_dictionary = dict(reversed(list(sorted_dictionary.items())))
        k = 0
        for key, value in reversed_dictionary.items():
            if k >= top_k :
                break
            print(f"{value} - {key}")
            k += 1

def main():
    '''Main function'''
    print("Enter N: ")
    number_of_ngrams = int(input())
    print("Enter K: ")
    top_k = int(input())
    with open('/lab_1/data/file.txt', 'r', encoding = "utf8") as file_to_open:
        input_string = file_to_open.read()
        dictionary = count_words(input_string)
        print(f"\nMedian: {median(dictionary.values())}")
        print(f"Average: {sum(dictionary.values()) / len(dictionary.values())}\n")
        dictionary = create_dictionary(number_of_ngrams, input_string)
        find_top(dictionary, top_k)
        file_to_open.close()

main()
