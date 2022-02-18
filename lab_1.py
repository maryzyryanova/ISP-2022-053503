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

#average amount of words in sentences
def findAverage(str):
    sentences = re.split('\. |\! |\? |\... ', str)
    checkEmpty(sentences)
    print(sentences)
    words = []
    for s in sentences :
        words.append(re.split('\, |\; |\! |\? |\... |\ ', s))
    print("/n" + words) #to control output

def main():
    str = input()
    dictionary = countWords(str)
    print(f"Median: {median(dictionary.values())}")
    print(f"Average: {sum(dictionary.values()) / len(dictionary.values())}")
    #findAverage(str)
    
main()