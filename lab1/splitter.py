'''Classes'''
import re
from statistics import median

class Words():
    '''Class, where you can split sentences on single  words'''
    splitters: str = r'\, |\. |\; |\! |\? |\... |\ |\!|\.|\?|\...|\,|\;'
    def __init__(self, input_string: str, top_k: int, n_grams: int) -> None:
        '''Constructor'''
        self.input_string: str = input_string
        self.top_k: int = top_k
        self.n_grams: int = n_grams
        self.splitted_string: str = ''
        self.dictionary: dict = {}

    def count_words(self) -> dict:
        '''Count amount of words in the text'''
        self.splitted_string = re.split(self.splitters, self.input_string)
        self.check_empty()
        for arr_element in self.splitted_string:
            if arr_element != 0 :
                if not self.dictionary.get(arr_element) :
                    self.dictionary[arr_element] = 1
                else:
                    self.dictionary[arr_element] += 1
        return self.dictionary

    def print_dictionary(self) -> None:
        '''Print dictionary'''
        for key, value in self.dictionary.items():
            print(f"{value} - {key}")

    def check_empty(self) -> None:
        '''Check string on empty elements'''
        if self.splitted_string.__contains__('') :
            self.splitted_string.remove('')

    def find_median(self) -> float:
        '''Median value of the words in the statement'''
        return median(self.dictionary.values())

    def find_average(self) -> float:
        '''Average value of the words in the sentence'''
        return sum(self.dictionary.values()) / len(self.dictionary.values())

class Letters(Words):
    '''Class, where you can split strings on letters'''
    def print_top(self) -> None:
        '''Print top K elements'''
        k: int = 0
        for key, value in self.dictionary.items():
            if k >= self.top_k :
                break
            print(f"{value} - {key}")
            k += 1

    def create_dictionary(self) -> dict:
        '''Creating and using dictionary'''
        self.splitted_string = re.split(self.splitters, self.input_string)
        super().check_empty()
        output: str = "".join(self.splitted_string)
        for i in range(0, len(output) - self.n_grams + 1, 1):
            temp: str = ''
            for j in range (i, i + self.n_grams):
                temp += output[j]
            if temp != '' :
                if not self.dictionary.get(temp) :
                    self.dictionary[temp] = 1
                else:
                    self.dictionary[temp] += 1
        return self.dictionary

    def find_top(self) -> None:
        '''Finding top K amount of n-grams'''
        sorted_dictionary: dict = {}
        sorted_values: dict = sorted(self.dictionary, key = self.dictionary.get)
        counter: int = 0
        for s_v in sorted_values:
            sorted_dictionary[s_v] = self.dictionary[s_v]
            counter += 1
        if counter < self.top_k :
            super().print_dictionary()
        else:
            self.dictionary = reversed(list(sorted_dictionary.items()))
            self.print_top()
