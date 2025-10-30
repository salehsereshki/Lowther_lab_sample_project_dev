import pandas as pd
import add_resolver
import sys


#To load data tables based on a file name and a loader function name.
#In this file there should be a function with the name loader_func that takes a single argument add (the resolved file path).
def load_dt(fn, loader_func):
    add = add_resolver.get_file_name(fn)
    mod = sys.modules[__name__]  # current module object
    func = getattr(mod, loader_func, None)  # look up symbol by name
    if not callable(func):
        raise NameError(f"No callable named {loader_func!r} in {mod.__name__}")
    return func(add)


def sample_input(add):
    return pd.read_csv(add, sep='\t')
