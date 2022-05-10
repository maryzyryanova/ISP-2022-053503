import argparse
import re


from fabric import Fabric


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
    argparser = argparse.ArgumentParser()
    argparser.add_argument ("source", type=str, help="Path to source file")
    argparser.add_argument("format", type=str, help="Serialize format (json, toml or yaml) for result")
    argparser.add_argument("-r", "--result-file", type=str,
    help="Path to result file. If not exist, it will be created")
    namespace = argparser.parse_args()
    result_format = namespace.format
    source_path = namespace.source
    source_format = re.search(r"\w+$", source_path).group()
    print(result_format)
    print(source_path)
    print(source_format)
    serializer = Fabric.create_serializer(result_format)
    if source_format == result_format:
        print("Same type")
        exit(0)
    deserializer = Fabric.create_serializer(source_format)
    print("vova gg")
    # serializer.dump(SimpleClass, "serialized_data/data.json")
    deserializer.load(source_path)
    serializer.dump(deserializer.load(source_path), f'res.{result_format}')

main()