# zadanie 1
"""Funkcja powinna zwrócić średnią arytmetyczną elementów na liście 'input'"""


def avg(input):
    return sum(input) / len(input)


print('zadanie 1')
print(avg([2, 2, 2, 2, 2, 2]) - 2 < 0.0000001)
print(avg([4, 6, 55, 18, 17, 12]) - 18.666666666666668 < 0.0000001)
print(avg([86, 89, 24, 45, 62, 17, 61, 63, 30, 13]) - 49 < 0.0000001)
print(' ')

# zadanie 2
"""Funkcja powinna zwrocic liste liczb parzystych <= n"""


def even_list(n):
    even_numbers_smaller_than_n = [nn for nn in range(n + 1) if nn % 2 == 0 and nn != 0]
    return even_numbers_smaller_than_n


print('zadanie 2')
print(even_list(1) == [])
print(even_list(2) == [2])
print(even_list(-5) == [])
print(even_list(7) == [2, 4, 6])
print(' ')

# zadanie 3
""" Funkcja powinna zwrócić sumę kwadratów liczb od 1 do n włącznie """


def sum_of_squares(n):
    result = [nn * nn for nn in range(n + 1)]
    return sum(result)


print('zadanie 3')
print(sum_of_squares(1) == 1)
print(sum_of_squares(3) == 14)
print(sum_of_squares(10) == 385)
print(' ')

# zadanie 4
""" Funckja powinna zwrócić sume wszystkich dodatnich wieloktrotności parametru k mniejszych niż n """


def sum_of_multiples(k, n=101):
    result = [k * p for p in range(n + 1) if k * p < n]
    return (sum(result))


print('zadanie 4')
print(sum_of_multiples(5) == 1050)
print(sum_of_multiples(17) == 255)
print(sum_of_multiples(69) == 69)
print(' ')

# zadanie 5
""" Funkcja powinna zwrócić liste liczb pierwszych mniejszych od n """


def primes_less_than(n):
    return list(filter(lambda n: False if n < 2 or any(n % k == 0 for k in range(2, n)) else True, range(n)))


print('zadanie 5')
print(primes_less_than(5) == [2, 3])
print(primes_less_than(10) == [2, 3, 5, 7])
print(primes_less_than(20) == [2, 3, 5, 7, 11, 13, 17, 19])
print(' ')
# zadanie 6
""" Funkcja sprawdza czy *word* jest palindromem """


def is_palindrome(word):
    return word == word[::-1]


print('zadanie 6')
print(is_palindrome('ala') == True)
print(is_palindrome('ananas') == False)
print(is_palindrome('ananasa') == False)
print(is_palindrome('tomek') == False)
print(' ')

# zadanie 7
""" Zwraca liczbę unikalnych znaków w słowie. Możemy założyć, że słowo składa się z małych liter alfabetu angielskiego """


def how_many_different_letters(word):
    return len(set(word))


print('zadanie 7')
print(how_many_different_letters('tomek') == 5)
print(how_many_different_letters('ala') == 2)
print(how_many_different_letters('ananas') == 3)
print(how_many_different_letters('jola') == 4)
print(' ')


def list_to_table(word):
    """ Funkcja przyjmuje 9-elementową liste i na jej podstawie tworzy stringa z HTMLową tabelą orzmiaru 3x3
    reprezentującą plansze do gry w kółko i krzyżyk"""
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

# zadanie 8
'''  Funkcja powinna sprawdzać, czy dana liczba n jest doskonała
    https://pl.wikipedia.org/wiki/Liczba_doskona%C5%82a'''


def is_perfect(n):
    div = [k for k in range(1, int((n + 2) / 2)) if n % k == 0]
    return sum(div) == n


print('zadanie 8')
print(is_perfect(6) is True)
print(is_perfect(28) is True)
print(is_perfect(7) is False)
print(' ')
# zadanie 9
import fractions

"""Funkcja powinna zwrócić wartość funkcji phi Eulera"""


def phi_euler(n):
    amount = 0
    for k in range(1, n + 1):
        if fractions._gcd(n, k) == 1:
            amount += 1
    return amount


print('zadanie 9')
print(phi_euler(6) == 2)
print(phi_euler(64) == 32)
print(phi_euler(97) == 96)
print(' ')

# zadanie 11
'''
Dla zadanej tablicy o długości  zawierającej liczby całkowite większe od zera. Chcemy znaleźć podtablice, że  kolejnych 
m elementów sumuje się do d.
W czasie liniowym
'''
import re


def HowManyIntegers(n):
    return sum(1 for x in range(n) if re.match('^[0279]+$', str(x))) - 1


print(HowManyIntegers(1) == 0)
print(HowManyIntegers(10) == 3)  # 2,7,9
print(HowManyIntegers(28) == 6)  # 2,7,9,20,22,27
