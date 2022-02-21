import re
from statistics import median

#count repeated words
def countWords(str):
    arr = re.split('\, |\. |\; |\! |\? |\... |\ |\!|\.|\?|\...|\,|\;', str)
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
    arr = re.split('\, |\. |\; |\! |\? |\... |\ |\!|\.|\?|\...|\,|\;', str)
    checkEmpty(arr)
    output = "".join(arr)
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
    return dictionary

#choose the biggest K elemenets
def findTopK(dictionary, K):
    sorted_dictionary = dict()
    sorted_values = sorted(dictionary, key = dictionary.get)
    counter = 0
    for s in sorted_values:
        sorted_dictionary[s] = dictionary[s]
        counter += 1
    if(counter < K):
        for key, value in sorted_dictionary.items():
            print(f"{value} - {key}")
    else:
        reversed_dictionary = dict(reversed(list(sorted_dictionary.items())))
        k = 0
        for key, value in reversed_dictionary.items():
            if(k >= K): break
            print(f"{value} - {key}")
            k += 1

def main():
    print("Enter N: ")
    N = int(input())
    print("Enter K: ")
    K = int(input())
    f = open('/data/file.txt', 'r')
    str = f.read()
    dictionary = countWords(str)
    print(f"\nMedian: {median(dictionary.values())}")
    print(f"Average: {sum(dictionary.values()) / len(dictionary.values())}\n")       
    dictionary = createDictionary(N, str)
    findTopK(dictionary, K)
    f.close()

main()
