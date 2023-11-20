#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        res = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e)),file = sys.stderr)
        return none
    else: 
        return res

