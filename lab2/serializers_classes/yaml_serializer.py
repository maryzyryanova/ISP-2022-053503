'''
Custom YAML serializer class
'''

from fileinput import filename
import yaml


class YAML:
    @staticmethod 
    def load(obj, filename):
        with open(filename, 'r') as f:
            return yaml.load(obj, f)
    
    @staticmethod 
    def loads(obj):
        return yaml.load(obj)

    @staticmethod 
    def dump(obj, filename):
        with open(filename, 'w+') as f:
            return yaml.dump(obj, f)

    @staticmethod 
    def dumps(obj):
        return yaml.dump(obj)