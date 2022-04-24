'''
Functions for packing and coverting different types of objects
'''

import inspect

from numpy import argmax


def check_function(obj) -> bool:
    return inspect.isfunction(obj) or inspect.ismethod(obj) 

def check_iterable(obj) -> object:
    return getattr(obj, "iterable") is not None

def get_global(function) -> dict:
    _globals = {}
    for g in function.__code__.co_names:
        if g in function.__globals__:
            _globals[g] = function.__globals__[g]
    return _globals

def convert_object(obj) -> object:
    if isinstance(obj, (int, float, bool, str, type(None))):
        return obj
    elif check_function(obj):
        return packing_function(obj)
    elif check_iterable(obj):
        return packing_iterable(obj)
    elif inspect.iscode(obj):
        return packing_code(obj)
    elif inspect.isclass(obj):
        return packing_class(obj)
    else:
        return packing_object(obj)

def packing_function(obj) -> dict:
    result = {"type" : "function"}
    _globals = get_global(obj)
    args = {}
    if inspect.ismethod(obj):
        obj = obj.__func__
    result["name"] = obj.__name__
    result["globals"] = packing_iterable(_globals)
    for key, value in inspect.getmembers(obj.__code__):
        if key.startswith("co_"):
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
    return

def packing_code(obj) -> object:
    return

def packing_class(obj) -> object:
    return

def packing_object(obj) -> object:
    return