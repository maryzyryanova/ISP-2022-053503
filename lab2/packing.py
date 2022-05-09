'''
Functions for packing and coverting different types of objects
'''

import inspect
from types import FunctionType


def check_function(obj) -> bool:
    return inspect.isfunction(obj) or inspect.ismethod(obj) 

def check_iterable(obj) -> object:
    # print("check iterable: {} ")
    return getattr(obj, "__iter__", None) is not None

def get_global(function) -> dict:
    _globals = {}
    for g in function.__code__.co_names:
        if g in function.__globals__:
            _globals[g] = function.__globals__[g]
    return _globals

def convert_object(obj) -> object:
    print(obj)
    if isinstance(obj, (int, float, bool, str, type(None))):
        return obj
    elif check_function(obj):
        return packing_function(obj)
    elif check_iterable(obj):
        return packing_iterable(obj)
    elif inspect.iscode(obj):
        return packing_function(FunctionType(obj, {}))
    elif inspect.isclass(obj):
        return packing_class(obj)
    else:
        return packing_object(obj)

def packing_function(obj) -> dict:
    result = {"type" : "function"}
    print('pack func')
    _globals = get_global(obj)
    args = {}
    if inspect.ismethod(obj):
        obj = obj.__func__
    result["name"] = obj.__name__
    result["globals"] = packing_iterable(_globals)
    for key, value in inspect.getmembers(obj.__code__):
        if key.startswith("co_"):
            if isinstance(value, bytes):
                value = list(value)
            if check_iterable(obj):
                if not isinstance(value, str):
                    packed_values = []
                    for v in value:
                        if v != None:
                            packed_values.append(convert_object(v))
                        else:
                            packed_values.append(convert_object(None))
                    args[key] = packed_values
                    continue
            args[key] = value
    result["arguments"] = args
    return result

def packing_iterable(obj) -> object:
    packed_values = []
    packed_dict = {}
    if isinstance(obj, list) or isinstance(obj, set) or isinstance(obj, tuple):
        for value in obj:
            packed_values.append(convert_object(value))
        if isinstance(obj, tuple):
            return tuple(packed_values)
        if isinstance(obj, set):
            return set(packed_values)
        if isinstance(obj, list):
            return list(packed_values)
        return packed_values
    elif isinstance(obj, dict):
        for key, value in obj.items():
            packed_dict[key] = convert_object(value)
        return packed_dict


def packing_class(obj) -> dict:
    result = {"type" : "class", "name" : obj.__name__}
    for d in dir(obj):
        if d == "__init__":
            result[d] = packing_function(getattr(obj, d))
        if not d.startswith("__"):
            result[d] = convert_object(getattr(obj, d))
    return result

def packing_object(obj) -> dict:
    result = {"type" : "object", "class" : obj.__class__.__name__}
    for d in dir(obj):
        if not d.startswith("__"):
            result[d] = convert_object(getattr(obj, d))
    return result