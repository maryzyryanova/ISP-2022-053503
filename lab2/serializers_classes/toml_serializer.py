'''
Custom TOML serializer class
'''

import toml

class TOML:
    def load(self, filename):
        with open(filename, 'r') as f:
            return self.loads(f.read())

    def dump(self, obj, filename):
        with open(filename, 'w+') as file:
            file.write(self.dumps(obj)) 

    # @staticmethod 
    # def load(filename):
    #     return toml.load(filename)
    
    @staticmethod 
    def loads(obj):
        return toml.loads(obj) 

    # @staticmethod 
    # def dump(obj, filename):
    #     with open(filename, 'w+') as f:
    #         toml.dump(obj, f)

    @staticmethod 
    def dumps(obj):
        toml.dumps(obj)
    

# from toml.encoder import _dump_str, TomlEncoder, unicode


# def _dump_str_prefer_multiline(v):
#   multilines = v.split('\n')
#   if len(multilines) > 1:
#     return unicode('"""\n' + v.replace('"""', '\\"""').strip() + '\n"""')
#   else:
#     return _dump_str(v)


# class MultilinePreferringTomlEncoder(TomlEncoder):
#   def __init__(self, _dict=dict, preserve=False):
#     super(MultilinePreferringTomlEncoder, self).__init__(_dict=dict, preserve=preserve)
#     self.dump_funcs[str] = _dump_str_prefer_multiline