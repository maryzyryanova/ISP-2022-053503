def countWords(arr):
    dictionary = dict()
    for i in range(0, len(arr)):
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
    arr = str.split()
    countWords(arr)

main()




