import argparse
from ast import arguments
import configparser

from yaml import parse
from fabric import Fabric
from tests.person import Person


simple_lambda = lambda q: q*q
int_glob = 73
str_glob = 'global'
float_glob = 2.2
boolean_glob = True
none_glob = None
list_1 = [1, '2', 3.3]
tuple_1 = (1, '2', 3.3)
set_1 = {1, '2', 3.3}
dict_1 = {'Name': 'Petr', 'Age' : 23, 'has_job': False}

class SimpleClass:
    def __init__(self):
        self.can_say = True
        self.count = 5
        self.word = "ku"
    def say_kuku(self):
        return self.word * self.count

class ComplexClass:
    def __init__(self):
        self.simple_class = SimpleClass()
        self.const = int_glob
        self.name = 'ComplexClass'
    def func_with_glob(self):
        return "local_str" + str_glob

def cmplx_func(a):
    b = int_glob
    return simple_func(2)*b**a

def simple_func(a):
    return a+10



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest = "configuration_file")
    parser.add_argument("-p", "--path", dest = "path_file")
    parser.add_argument("-f", "--format", dest = "format_file")
    args = parser.parse_args()

    if args.configiration_file:
        config = configparser.ConfigParser()
        config.read(args.configiration_file)
    
    

main()