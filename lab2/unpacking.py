from asyncio import constants
from types import CodeType, FunctionType
from packing import check_iterable, check_function

def deconvert_object(obj) -> object:
    if isinstance(obj, (int, float, bool, str, type(None))):
        return obj
    elif isinstance(obj, dict):
        if "type" in obj.keys():
            if "function" == obj["type"]:
                return unpacking_function(obj)
            elif "class" == obj["type"]:
                return unpacking_class(obj)
            elif "object" == obj["type"]:
                return unpacking_object(obj)
        return unpacking_iterable(obj)
    elif check_iterable(obj):
        return unpacking_iterable(obj)

def unpacking_function(obj) -> object:
    print(f'unpack function : \n{obj}')
    arguments = obj["arguments"]
    _globals = obj["globals"]
    _constants = []
    for key in _globals:
        if key in arguments["co_names"]:
            _globals[key] = deconvert_object(_globals[key])
    for value in list(arguments["co_consts"]):
        if check_function(deconvert_object(value)):
            _constants.append(deconvert_object(value).__code__)
            continue
        _constants.append(value)
    arguments["co_consts"] = _constants
    for value in arguments:
        if check_iterable(arguments[value]) and not isinstance(arguments[value], str):
            _constants = []
            for v in arguments[value]:
                if v == None:
                    _constants.append(None)
                else:
                    _constants.append(v)
            arguments[value] = _constants
    return FunctionType(CodeType
                    (arguments['co_argcount'],
                     arguments['co_posonlyargcount'],
                     arguments['co_kwonlyargcount'],
                     arguments['co_nlocals'],
                     arguments['co_stacksize'],
                     arguments['co_flags'],
                     bytes(arguments['co_code']),
                     tuple(arguments['co_consts']),
                     tuple(arguments['co_names']),
                     tuple(arguments['co_varnames']),
                     arguments['co_filename'],
                     arguments['co_name'],
                     arguments['co_firstlineno'],
                     bytes(arguments['co_lnotab']),
                     tuple(arguments['co_freevars']),
                     tuple(arguments['co_cellvars'])), 
                     _globals)

def unpacking_iterable(obj) -> object:
    if isinstance(obj, list) or isinstance(obj, set) or isinstance(obj, tuple):
        result = []
        for value in obj:
            result.append(deconvert_object(value))
        if isinstance(obj, set):
            return set(result)
        elif isinstance(obj, tuple):
            return tuple(result)
        elif isinstance(obj, list):
            return list(result)
    elif isinstance(obj, dict):
        result = {}
        for key, value in obj.items():
            result[key] = deconvert_object(value)
        return result

def unpacking_class(obj) -> object:
    result = {}
    for key, value in obj.items():
        result[key] = deconvert_object(value)
    return type(obj["name"], (), result)

def unpacking_object(obj) -> object:
    result = type(obj.get("class"), (), {})()
    for key, value in obj.items():
        if key != "class":
            setattr(result, key, deconvert_object(value))
    return result