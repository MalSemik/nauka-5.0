import sys, operator


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a // b


def modulo(a, b):
    return a % b


def generate_simple_operations_dict():
    return {'+': add, '-': subtract, '*': multiply, '/': divide, '%': modulo}


def generate_lambda_operations_dict():
    return {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b,
            '/': lambda a, b: a // b, '%': lambda a, b: a % b}


def generate_operations_dict_with_operator_module():
    return {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv,
            '%': operator.mod}


operations_by_symbols = generate_operations_dict_with_operator_module()

# for line in sys.stdin:
#     symbol, a, b = line.split()
#     print(operations_by_symbols[symbol](int(a), int(b)))

f = lambda x: x + 10
print(f(10))
