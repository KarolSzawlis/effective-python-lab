# zadanie 1
def flow_rate(weight, time, units_per_kg=1000, period=60):
    if type(units_per_kg) is not int or type(period) is not int:
        raise TypeError
    return (weight * units_per_kg) / (time / period)


weight = 0.5
time = 3
flow = flow_rate(weight, time)
print("{0:.3} kg per second".format(flow))

flow = flow_rate(weight, time, period=60, units_per_kg=1000)
print("{} grams per minute".format(flow))

flow = flow_rate(weight, time, period=1, units_per_kg=1)
print("{0:.3} kg per second".format(flow))

flow = flow_rate(weight, time)
print("{0:.3} grams per minute".format(flow))
# zadanie 2
from time import time

""" Wypisuje czas wywołania udekorowanej funckji """


def timeit(func):
    def wrapper(*args):
        start = time()
        result = func(*args)
        end = time()
        print("Function " + func.__name__ + " took: " + str(end - start) + " seconds")
        return result

    return wrapper


@timeit
def squares_list(n):
    squares = []
    for i in range(n):
        squares.append(i ** 2)
    return squares


@timeit
def squares_comprehension(n):
    return [i ** 2 for i in range(n)]


@timeit
def squares_map(n):
    return map(lambda x: x ** 2, range(n))


n = 1000000
l = squares_list(n)
c = squares_comprehension(n)
m = squares_map(n)
# zadanie 3
"""
   Zwraca pochodną funkcji w punkcie, wg. wzoru f'(x) = [f(x+h) - f(x)]/h, 
   gdzie h jest parametrem dekoratora, jeśli nie zostanie podany, należy przyjąć 1000 * epsilon maszynowy
   """
import sys

sys.float_info.epsilon  # epsilon maszynowy


def derivate(epsilon=None):
    if epsilon is None:
        epsilon = sys.float_info.epsilon * 1000

    def wrapper(function):
        def wrapper_f(x):
            return (function(x + epsilon) - function(x)) / epsilon

        return wrapper_f

    return wrapper


@derivate(0.01)
def f(x):
    return x * x


@derivate(0.00001)
def g(x):
    return x * x * x + 3


def test(a, b, eps=1):
    return abs(round(a) - round(b)) < eps


print(test(f(100), 200.0))
print(round(f(0)) == 0.0)

print(test(g(100), 30000.0))
print(round(g(0)) == 0.0)

from random import random

for x in [random() * 1000. for _ in range(20)]:
    print(f(x), 2 * x, '\t', test(f(x), 2 * x))
    print(g(x), 3 * x ** 2, '\t', test(g(x), 3 * x ** 2))

# zadanie 4
"""Sprawdza czy udekorowanej funckji zostały podane odpowiednie parametry zdefiniowane 
       w argumentach dekoratora"""


def accepts(*types):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for arg, typ in zip(args, types):
                if not isinstance(arg, typ):
                    raise TypeError
                return function(*args, **kwargs)

        return wrapper

    return decorator


@accepts(str)
def capitalize(word):
    return word[0].upper() + word[1:]


print(capitalize('ola') == 'Ola')

try:
    capitalize(2)
except TypeError:
    print(True)


@accepts(float, int)
def static_pow(base, exp):
    return base ** exp


print(static_pow(2., 2) == 4.)
print(static_pow(2., exp=2) == 4.)
print(static_pow(base=2., exp=2) == 4.)

try:
    static_pow('x', 10)
except TypeError:
    print(True)

try:
    static_pow(2, 2.2)
except TypeError:
    print(True)


# zadanie 5
def returns(*types):
    def wrapper(function):
        def wrapper_f(*args, **kwargs):
            result = function(*args, **kwargs)
            if any(type(z) is not y for y, z in zip(types, result)):
                raise TypeError
            else:
                return result

        return wrapper_f

    return wrapper


@returns(str)
def str_only_identity(word):
    return word


print(str_only_identity('hello') == 'hello')

try:
    str_only_identity(10)
except TypeError:
    print(True)


@returns(int, int)
def split_indices(x):
    return x[0], x[1]


print(split_indices(x=[6, 9]) == (6, 9))

try:
    split_indices('AB')
except TypeError:
    print(True)


# zadanie 8
def my_function(x, y):
    return {
        1: y * y,
        2: x + y,
        3: x * y,
        4: 0
    }[x]


print(my_function(1, 3) == 9)
print(my_function(2, 4) == 6)
print(my_function(3, 1) == 3)
print(my_function(4, 9) == 0)
