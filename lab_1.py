def countWords(arr):
    dictionary = dict()
    for i in range(0, len(arr)):
        counter = 1
        for j in range(i+1, len(arr)):
            if(arr[i] == arr[j]):
                counter += 1
        dictionary[arr[i]] = counter
    for key, value in dictionary.items():
        print(f"{value} - {key}")
    return dictionary

def main():
    str = input()
    print(f"Your string: {str}")
    arr = str.split()
    countWords(arr)

main()




