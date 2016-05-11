#coding=utf-8
#author count99 in 1/12/2016
import types
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if (isinstance(args[0], list) and len(args)==1)or isinstance(args[0], str) or isinstance(args[0], tuple) or isinstance(args[0], set):
        temp = [i for i in args[0]]
        args=temp
    elif isinstance(args[0], range):
        temp = [i for i in args[0]]
        args=temp
    elif isinstance(args[0], types.GeneratorType):
        temp = []
        for i in args[0]:
            temp.append(i)
        args=temp
    elif isinstance(args[0],filter):
        temp = []
        for i in args[0]:
            temp.append(i)
        args=temp
    current = args[0]
    if key is not None:
        for item in args:
            if key(item) < key(current):
                current = item
    else:
        for item in args:
            if item < current:
                current = item
    return current

def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if (isinstance(args[0], list) and len(args)==1)or isinstance(args[0], str) or isinstance(args[0], tuple) or isinstance(args[0], set):
        temp = [i for i in args[0]]
        args=temp
    elif isinstance(args[0], range):
        temp = [i for i in args[0]]
        args=temp
    elif isinstance(args[0], types.GeneratorType):
        temp = []
        for i in args[0]:
            temp.append(i)
        args=temp
    elif isinstance(args[0],filter):
        temp = []
        for i in args[0]:
            temp.append(i)
        args=temp
    current = args[0]
    if key is not None:
        for item in args:
            if key(item) > key(current):
                current = item
    else:
        for item in args:
            if item > current:
                current = item
    return current   

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert max(3, 2) == 3, "Simple case max"
#     assert min(3, 2) == 2, "Simple case min"
#     assert max([1, 2, 0, 3, 4]) == 4, "From a list"
#     assert min("hello") == "e", "From string"
#     assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
#     assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print (max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]))