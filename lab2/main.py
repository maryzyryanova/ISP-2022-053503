import argparse
import re
from unit_tests.test_data import SimpleClass



from fabric import Fabric

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
    deserializer.dump(SimpleClass(), "serialized_data/data.json")
    #deserializer.load(source_path)
    serializer.dump(deserializer.load(source_path), f'serialized_data/data.{result_format}')

main()