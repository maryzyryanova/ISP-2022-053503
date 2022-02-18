import re

def countWords(arr):
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

def main():
    str = input()
    print(f"Your string: {str}")
    arr = re.split('\, |\. |\; |\! |\? |\... |\ ', str)
    countWords(arr)

main()




