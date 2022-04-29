'''
Custom JSON serializer class
'''


import packing


class JSON:
    def __init__(self) -> None:
        self.position = 0

    def load():
        return
    
    def loads():
        return 

    def dump(self, obj, filename):
        with open(filename, 'w+') as file:
            file.write(self.dumps(obj)) 

    def dumps(self, obj):
        print(type(packing.convert_object(obj)))
        return self.convert_to_str(packing.convert_object(obj))
    
    def convert_to_str(self, value, key='') -> str:
        if isinstance(value, (int, float, bool, str, type(None))):
            return self.convert_to_simple_dimple(value, key)
        elif isinstance(value, (tuple, list, set, frozenset)):
            return self.convert_to_collections_popit(value, key)
        elif isinstance(value, dict):
            print(value)
            return self.convert_to_dictionary_squish(value, key)
        print(value)
        # raise ValueError("Error")
    
    def convert_to_simple_dimple(self, value, key) -> str:
        result = ''
        if len(key):
            result += f'{key}: '
        if isinstance(value, type(None)):
            result += 'null'
        elif isinstance(value, bool):
            if value:
                result += 'true'
            else:
                result += 'false'
        elif isinstance(value, (int, float)):
            result += str(value)
        elif isinstance(value, str):
            result += f'"{value}"'
        return result
    
    def convert_to_collections_popit(self, value, key) -> str:
        result = ''
        if len(key):
            result += f'{key}: '
        # result += f'[ type: {value}, '
        result += f'[ "__{type(value).__name__}__", '
        for v in value:
            result += f'{self.convert_to_str(v)}, '
        if result[-2]==',':
            result = result[:-2]
        result += ']'
        return result

    def convert_to_dictionary_squish(self, value, key) -> str:
        result = ''
        if len(key):
            result += f'{key}: '
        result += '{'
        for _key, _value in value.items():
            result += f'{self.convert_to_str(_value, self.convert_to_str(str(_key)))}, '
        if result[-2]==',':
            result = result[:-2]
        result += '}'
        self.position += 2
        return result

    def deconvert_str(self, value) -> object:
        if self.position >= len(value):
            raise ValueError("Incorrect position")
        elif isinstance(value[self.position], (int, float)):
            return self.deconvert_to_number(value)
        elif isinstance(value[self.position: self.position + 4], ("True", "False")):
            return self.deconvert_to_bool(value)
    
    def deconvert_to_number(self, value) -> int or float:
        return "sdfghjk"

    def deconvert_to_bool(self, value) -> bool:
        return ""
    
