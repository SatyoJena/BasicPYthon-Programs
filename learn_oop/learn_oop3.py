'''
you can pass objects into objects
'''
def add(a:float,b:float)-> float:
    return a+b
def subtract(a:float,b:float)-> float:
    return a-b
def multiply(a:float,b:float)-> float:
    return a*b
def divide(a:float,b:float)-> float:
    return a/b

class Operation:
    def __init__(self,my_func):
        self.operation = my_func
