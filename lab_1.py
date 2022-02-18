import re
from statistics import median

#count repeated words
def countWords(str):
    arr = re.split('\, |\. |\; |\! |\? |\... |\ ', str)
    checkEmpty(arr)
    dictionary = dict()
    for i in range(0, len(arr)):
        if(arr[i] != 0):
            if(not dictionary.get(arr[i])):
                dictionary[arr[i]] = 1
            else:
                dictionary[arr[i]] += 1
    for key, value in dictionary.items():
        print(f"{value} - {key}")
    return dictionary

#deleting null element
def checkEmpty(arr):
    if(arr.__contains__('')):
        arr.remove('')

#create a dictionary of n-grams
def createDictionary(N, str):
    arr = re.split('\, |\. |\; |\! |\? |\... |\ ', str)
    checkEmpty(arr)
    for i in range(len(arr) - 1):
        arr[i] += arr[i+1]
        output = arr[i]
    dictionary = dict()
    for i in range(0, len(output) - N + 1, 1):
        temp = ''
        for j in range (i, i + N):
            temp += output[j]
        if(temp != ''):
            if(not dictionary.get(temp)):
                dictionary[temp] = 1
            else:
                dictionary[temp] += 1
    for key, value in dictionary.items():
        print(f"{value} - {key}")
    return dictionary

#choosw the biggest K elemenets
def findTopK(dictionary, K):
    sorted_dictionary = dict()
    sorted_values = sorted(dictionary, key = dictionary.get)
    for s in sorted_values:
        sorted_dictionary[s] = dictionary[s]
    dictionary = reversed(sorted_dictionary)

def main():
    print("Enter N: ")
    N = (int)(input())

    print("Enter K: ")
    K = (int)(input())

    print("Your text: ")
    str = input()

    dictionary = countWords(str)
    print(f"Median: {median(dictionary.values())}")
    print(f"Average: {sum(dictionary.values()) / len(dictionary.values())}")
    dictionary = createDictionary(N, str)
    findTopK(dictionary, K)

main()