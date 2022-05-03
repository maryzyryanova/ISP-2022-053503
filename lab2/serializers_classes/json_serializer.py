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
        if value[self.position: self.position + 4] == 'null':
            return self.deconvert_to_none(value)
        elif value[self.position: self.position + 4] == 'true':
            return self.deconvert_to_true(value)
        elif value[self.position: self.position + 5] == 'false':
            return self.deconvert_to_false(value)
        elif value[self.position] == '"':
            return self.deconvert_to_string(value)
        elif value[self.position] == '[':
            return self.deconvert_to_collection(value)
        elif value[self.position] == '{':
            return self.deconvert_to_dictionary(value)
        else:
            return self.deconvert_to_number(value)
    
    def deconvert_to_number(self, value) -> int or float:
        result = ""
        self.position += 1
        while self.position < len(value):
            if value[self.position] == " " or value[self.position] == ",":
                result += value[self.position]
                self.position += 1
        if result.find('.'):
            return float(result)
        return int(result)    

    def deconvert_to_true(self) -> bool:
        self.position += 4
        return True

    def deconvert_to_false(self) -> bool:
        self.position += 5
        return False

    def deconvert_to_collection(self, value) -> set or list or tuple:
        result = ""
        self.position += 1
        collection_type = self.deconvert_str(value)
        while self.position < len(value):
            if value[self.position] == "}" or value[self.position] == "]" or value[self.position] == ")" or value[self.position] == "," or value[self.position] == " ":
                self.position += 1
                continue
            result += self.deconvert_str
            self.position += 1
        self.position += 1
        if collection_type == "__tuple___":
            return tuple(result)
        elif collection_type == "__list__":
            return list(result)
        elif collection_type == "__set__":
            return set(result)

    
    def deconvert_to_string(self, value) -> str:
        result = []
        self.position += 1
        if value[self.position] == '"':
            self.position += 1
        while self.position < len(value):
            if value[self.position] == "'" or value[self.position] == '"':
                continue
            result.append(value[self.position])
            self.position += 1
        self.position += 1
        return result
        
    
    def deconvert_to_dictionary(self, value) -> dict:
        result = {}
        self.position += 1
        while self.position < len(value):
            if value[self.position] == "}" or value[self.position] == "{"  or value[self.position] == " " or value[self.position] == ",":
                self.position += 1
                continue
            key = self.deconvert_to_number(value)
            self.position = value.find(':', self.position) + 2
            value = self.deconvert_str(value)
            result[key] = value
        self.position += 1
        return result

    def deconvert_to_none(self, value) -> None:
        self.position += 4
        return None
    
