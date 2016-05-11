#coding: utf-8

"""
Define a method get_fundoc (func), func parameter is an arbitrary function object, 
the function returns the object description document, if the document does not 
describe the function, it returns "not found"
"""
def get_fundoc(func):
    """A funtion to get builtin_function_or_method or funtion's doc file"""
    if type(func) is "function" or "builtin_function_or_method":
        if func.__doc__:
            return func.__doc__
        else:
            return "Nono"
    else:
        return "This not Function"
    
"""
Define a method get_cjsum (), find all integers within the range of 1-100 and square. 
Returns the result to an integer type.
"""
def get_cjsum(num):
    """A funtion to sum range 1-100,and return a int type answer."""
    if num <= 100:
        sq_sum = 0
        for i in range(num+1):
            sq_sum += i**2
        return sq_sum
    else:
        return "This number is over our range 100."

"""
Define a method list_info (list), the parameter list is a list of objects, how to ensure 
that the list in the function list some related operations will not affect the value of 
the original list of elements, such as: 

a = [1,2,3] 

def list_info (list): 
    '' To list related operations, not directly write only one return [1,2,5], so no sense '' '

print list_info (a): returns the result: [1,2,5] 

print a output: [1,2,3] 

Write operation code function in vivo.
"""
def list_info(a_list):
    """operate a list in funtion's filed, but don't change origine list"""
    b = a_list.copy()
    a_list.append(1)
    a_list[0]="great"
    a_list = b
    return a_list
"""
Define a method get_funcname (func), func parameter is an arbitrary function objects,
you need to determine whether the function can be called, if you can call it returns 
the function name (Type str), otherwise it returns "fun is not function".
"""
def get_funcname(func):
    """Print a function's name"""
    if callable(func):
        return func.__name__
    else:
        return "fun is not function"

