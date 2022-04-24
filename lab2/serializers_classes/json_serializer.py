'''
Custom JSON serializer class
'''


class JSON:
    def load():
        return
    
    def loads():
        return 

    def dump(self, obj, filename):
        with open(filename, 'w+') as file:
            file.write(self.dumps(obj)) 

    def dumps(self, obj):
        return self.convert_to_str(obj)
    
    def convert_to_str(self, value, key) -> str:
        if isinstance(value, (int, float, bool, str, type(None))):
            return self.convert_to_simple(value, key)
        elif isinstance(value, (tuple, list, set, frozenset)):
            return self.convert_to_collections(value, key)
        elif isinstance(value, dict):
            return self.convert_to_dictionary(value, key)
        raise ValueError("Error")
    
    def convert_to_simple_dimple(self, value, key) -> str:
        result = ''
        if len(key):
            result += f'{key}'
        if isinstance(value, type(None)):
            result += 'null value'
        elif isinstance(value, bool):
            if value:
                result += 'True'
            result += 'False'
        elif isinstance(value, (int, float)):
            result += str(value)
        elif isinstance(value, str):
            result += f'{value}'
        return result
    
    def convert_to_collections_popit(self, value, key) -> str:
        result = ''
        if len(key):
            result += f'{key}'
        result += f'type{value}, '
        for v in value:
            result += f'{self.convert_to_str(value)}, '
        return result

    def convert_to_dictionary_squish(self, value, key) -> str:
        result = ''
        if len(key):
            result += f'{key}'
        result += '{'
        for _key, _value in value.items():
            result += f'{self.convert_to_str(_value, self.convert_to_str(str(_key)))}, '
        result += '}'
        return result