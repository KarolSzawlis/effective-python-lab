# exercise 1
"""Filtruje z iterable elementy, dla których funkcja func zwraca False zostawiając pozostałe"""
"" "Filters with iterable elements for which the function func returns False leaving the remaining" ""


def _filter(func=None, iterable=[]):
    if func:
        for k in iterable:
            if func(k):
                yield k
    else:
        for k in iterable:
            if k:
                yield k


print('exercise 1')
from types import GeneratorType

print(isinstance(_filter(), GeneratorType))
print(list(filter(lambda x: x > 0, [0, -3, 1, 6])) == list(_filter(lambda x: x > 0, [0, -3, 1, 6])))
print(list(filter(None, [2, -3, 1, 6])) == list(_filter(None, [2, -3, 1, 6])))
print(list(filter(None, [True, False, False])) == list(_filter(None, [True, False, False])))
print(list(filter(None, [0, -3, 1, 6])) == list(_filter(None, [0, -3, 1, 6])))
print(' ')


# exercise 2
def _map(func, iterable, *args):
    """Mapuje elementy iterable na wartości fuknckji func"""
    "" "Maps iterable elements to fuknckji func values" ""
    for i in zip(iterable, *args):
        yield func(*i)


print('exercise 2')
from types import GeneratorType

print(isinstance(_map(None, None), GeneratorType))
print(list(map(lambda x: x.upper(), 'ala ma kota')) == list(_map(lambda x: x.upper(), 'ala ma kota')))
print(list(map(lambda x, y: x + y, [1, 2, 3, 4], [5, 6, 7, 8])) == list(
    _map(lambda x, y: x + y, [1, 2, 3, 4], [5, 6, 7, 8])))
print(' ')

# exercise 3
"""Zwraca listę odwróconych słowa które nie są palindromami."""
"""Zwraca listę odwróconych słowa które nie są palindromami."""


def reverse_nonpalindromes(words):
    return list(map(lambda w: w[::-1], filter(lambda w: w != w[::-1], words)))


print('exercise 3')
print(reverse_nonpalindromes(["aa", "ab"]) == ["ba"])
print(reverse_nonpalindromes(["eht", "dog", "ala"]) == ["the", "god"])
print(' ')

# exercise 4
"""Zwraca sumę kwadratów nieparzystych liczb"""
"" "Returns the sum of squares of odd numbers" ""
from functools import reduce


def squares_of_odds(values):
    return reduce(lambda a, b: a + b, map(lambda x: x * x, filter(lambda x: x % 2 == 1, values)))


print('exercise 4')
print(squares_of_odds([1, 2, 3, 4, 5, 6]))
print(squares_of_odds([1, 2, 3, 4, 5, 6]) == 35)
print(squares_of_odds([10, 13, 5, 6]) == 194)
print(' ')
# exercise 5
"""zwraca czy wszystkie liczby są dodatnie"""
"" "returns if all numbers are positive" ""


def all_are_positive(numbers):
    return not list(filter(lambda n: n < 0, numbers))


print('exercise 5')
print(all_are_positive([]))  # PS: tu sie im wykraczy bez inicjalizatora :)
print(all_are_positive([1, 2, 3]))
print(not all_are_positive([-1, 2, 3]))
print(not all_are_positive([5, 6, -2, 1]))
print(' ')

# exercise 6
"""Przepisz poniższą funkcję korzystając wyłącznie z funkcji reduce, map i filter oraz lambd"""
"" "Rewrite the following function using only the reduce, map and filter and lambd functions"""


def flatten(lists):
    return reduce(lambda x, y: x + y, lists)


print('exercise 6')
print(flatten([[]]) == [])
print(flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4])
print(flatten([["1", 1.1], []]) == ["1", 1.1])
print(' ')

# exercise 7
"""Konwertuje liste temperatur w stopniach Celsjusza do skali Fahrenheita"""
"" "Converts list of temperatures in degrees Celsius to Fahrenheit scale" ""


def celsius_to_fahrenheit(x):
    return map(lambda yy: 1.8 * yy + 32, x)


print('exercise 7')
print(list(celsius_to_fahrenheit([0, 10, 100])) == [32.0, 50.0, 212.0])
print(list(celsius_to_fahrenheit([-123, 0])) == [-189.4, 32.0])
print(' ')

# zadaninie 8
"""Zwraca iloczyn liczb w liście x większych od k"""
"" "Returns the product of numbers in list x greater than k" ""
from functools import reduce


def product_greater_than(x, k=0):
    return reduce(lambda x, y: x * y, filter(lambda xx: xx > k, x))


print('exercise 8')
print(product_greater_than([1, 2, 3]) == 6)
print(product_greater_than([1, 2, 3], 2) == 3)
print(product_greater_than([-4, 5, 10, 23, 123], -5) == -565800)
print(' ')

from functools import reduce

# exercise 9
"""Łączy słowa (o długości co najmniej k) z listy x w zdanie - nie używa reduce"""
"" "Combines words (at least k length) from the list x in the sentence - does not use reduce" ""


def create_sentence(x, k=0):
    return ' '.join(filter(lambda x: len(x) >= k, x))


print('exercise 9')
print(create_sentence(['ala', 'ma', 'kota']) == 'ala ma kota')
print(create_sentence(['ala']) == 'ala')
print(create_sentence(['ala', 'ma', 'pieknego', 'kota'], k=3) == 'ala pieknego kota')
print(' ')
# zadani 10
"""Zwraca k-elementową krotke składającą się z kolejnych elementów list podanych jako arguemnty pozycyjne, 
  jeżeli ich suma jest większa niż parametr k"""
"""Returns the k-element tuple consisting of subsequent elements of the lists given as positional arguments,
   if their sum is greater than the parameter k """


def tuple_if_sum_greater(k, *lists):
    return filter(lambda x: sum(x) > k, zip(*lists))


print('exercise 10')
print(list(tuple_if_sum_greater(0, [1, 2, 3])) == [(1,), (2,), (3,)])
print(list(tuple_if_sum_greater(4, [1, 2, 3], [2, 3, 4])) == [(2, 3), (3, 4)])
print(list(tuple_if_sum_greater(10, [1, 2, 3], [2, 3, 4])) == [])
print(list(tuple_if_sum_greater(0, [1, 2], [3, 4], [5, 6])) == [(1, 3, 5), (2, 4, 6)])
print(' ')
# exercise 11
"""Zwraca zbiór liczb pierwszych od 0 do N włącznie"""
"" "Returns a set of prime numbers from 0 to N inclusive" ""
from math import sqrt


def primes(N):
    return set(filter(lambda n: False if n < 2 or any(n % k == 0 for k in range(2, n)) else True, range(N + 1)))


print('exercise 11')
print(primes(5) == {2, 3, 5})
print(primes(10) == {2, 3, 5, 7})
print(primes(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                      43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97})
print(' ')
