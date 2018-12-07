# exercise 1
"""Funkcja powinna zwrócić średnią arytmetyczną elementów na liście 'input'"""
"" "The function should return the arithmetic mean of elements in the input list" ""


def avg(input):
    return sum(input) / len(input)


print('exercise 1')
print(avg([2, 2, 2, 2, 2, 2]) - 2 < 0.0000001)
print(avg([4, 6, 55, 18, 17, 12]) - 18.666666666666668 < 0.0000001)
print(avg([86, 89, 24, 45, 62, 17, 61, 63, 30, 13]) - 49 < 0.0000001)
print(' ')

# exercise 2
"""Funkcja powinna zwrocic liste liczb parzystych <= n"""
"" "The function should return a list of even numbers <= n" ""


def even_list(n):
    even_numbers_smaller_than_n = [nn for nn in range(n + 1) if nn % 2 == 0 and nn != 0]
    return even_numbers_smaller_than_n


print('exercise 2')
print(even_list(1) == [])
print(even_list(2) == [2])
print(even_list(-5) == [])
print(even_list(7) == [2, 4, 6])
print(' ')

# exercise 3
""" Funkcja powinna zwrócić sumę kwadratów liczb od 1 do n włącznie """
"" "The function should return the sum of the squares of numbers from 1 to n inclusive" ""


def sum_of_squares(n):
    result = [nn * nn for nn in range(n + 1)]
    return sum(result)


print('exercise 3')
print(sum_of_squares(1) == 1)
print(sum_of_squares(3) == 14)
print(sum_of_squares(10) == 385)
print(' ')

# exercise 4
""" Funckja powinna zwrócić sume wszystkich dodatnich wieloktrotności parametru k mniejszych niż n """
"" "The function should return the sum of all positive multiplicities of parameter k smaller than n" ""


def sum_of_multiples(k, n=101):
    result = [k * p for p in range(n + 1) if k * p < n]
    return (sum(result))


print('exercise 4')
print(sum_of_multiples(5) == 1050)
print(sum_of_multiples(17) == 255)
print(sum_of_multiples(69) == 69)
print(' ')

# exercise 5
""" Funkcja powinna zwrócić liste liczb pierwszych mniejszych od n """
"" "The function should return a list of prime numbers smaller than n" ""


def primes_less_than(n):
    return list(filter(lambda n: False if n < 2 or any(n % k == 0 for k in range(2, n)) else True, range(n)))


print('exercise 5')
print(primes_less_than(5) == [2, 3])
print(primes_less_than(10) == [2, 3, 5, 7])
print(primes_less_than(20) == [2, 3, 5, 7, 11, 13, 17, 19])
print(' ')
# exercise 6
""" Funkcja sprawdza czy *word* jest palindromem """
"" "The function checks if * word * is a palindrome" ""


def is_palindrome(word):
    return word == word[::-1]


print('exercise 6')
print(is_palindrome('ala') == True)
print(is_palindrome('ananas') == False)
print(is_palindrome('ananasa') == False)
print(is_palindrome('tomek') == False)
print(' ')

# exercise 7
""" Zwraca liczbę unikalnych znaków w słowie. Możemy założyć, że słowo składa się z małych liter alfabetu angielskiego """
"" "Returns the number of unique characters in a word. We can assume that the word consists of lowercase letters of the English alphabet" ""


def how_many_different_letters(word):
    return len(set(word))


print('exercise 7')
print(how_many_different_letters('tomek') == 5)
print(how_many_different_letters('ala') == 2)
print(how_many_different_letters('ananas') == 3)
print(how_many_different_letters('jola') == 4)
print(' ')


def list_to_table(word):
    """ Funkcja przyjmuje 9-elementową liste i na jej podstawie tworzy stringa z HTMLową tabelą orzmiaru 3x3
    reprezentującą plansze do gry w kółko i krzyżyk"""
    """The function accepts a 9-element list and on the basis it creates a string with an HTML table 3x3
    representing
    boards
    for playing the noughts and crosses """
    board = '<table style="table-layout: fixed; height: 90px; width: 90px;">'

    # twoj kod

    board += "\n</table>"
    return board


print(list_to_table(['X', '', 'O', '', 'X', '', 'O', '', 'O']))


def divisorsSum(x):
    return sum([y for y in range(1, x) if x % y == 0])


def zaprzyjaznione(n):
    return [(x, divisorsSum(x)) for x in range(1, n) if x == divisorsSum(divisorsSum(x)) and x < divisorsSum(x)]


print(zaprzyjaznione(1) == [])
print(zaprzyjaznione(300) == [(220, 284)])
print(zaprzyjaznione(2000) == [(220, 284), (1184, 1210)])
print(zaprzyjaznione(13000) == [(220, 284), (1184, 1210), (2620, 2924), (5020, 5564), (6232, 6368), (10744, 10856),
                                (12285, 14595)])

# exercise 8
'''  Funkcja powinna sprawdzać, czy dana liczba n jest doskonała
    https://pl.wikipedia.org/wiki/Liczba_doskona%C5%82a'''
'' 'The function should check if the number n is perfect https://pl.wikipedia.org/wiki/Liczba_doskona%C5%82a '''


def is_perfect(n):
    div = [k for k in range(1, int((n + 2) / 2)) if n % k == 0]
    return sum(div) == n


print('exercise 8')
print(is_perfect(6) is True)
print(is_perfect(28) is True)
print(is_perfect(7) is False)
print(' ')
# exercise 9
import fractions

"""Funkcja powinna zwrócić wartość funkcji phi Eulera"""
"" "The function should return the value of the phi Euler function" ""


def phi_euler(n):
    amount = 0
    for k in range(1, n + 1):
        if fractions._gcd(n, k) == 1:
            amount += 1
    return amount


print('exercise 9')
print(phi_euler(6) == 2)
print(phi_euler(64) == 32)
print(phi_euler(97) == 96)
print(' ')

import re


def HowManyIntegers(n):
    return sum(1 for x in range(n) if re.match('^[0279]+$', str(x))) - 1


print(HowManyIntegers(1) == 0)
print(HowManyIntegers(10) == 3)  # 2,7,9
print(HowManyIntegers(28) == 6)  # 2,7,9,20,22,27
