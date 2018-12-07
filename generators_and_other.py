# exercise 1 a
'''Napisz funkcję, która wypisuje wiadomość opcjonalnie wraz z podaną wartością'''


def log(*args):
    print(args)


# exercise 1 b
"""Zwraca średnią liczb podanych jako argumenty pozycyjne"""


def mean(*args):
    return sum(args) / len(args)


print('exercise 1b')
print(mean(1, 2, 3) == 2)
print(mean(2, 2, 4, 4) == 3)
print(mean(1, 2, 3, 4, 5, 61, 2, 12, 123, 123) == 33.6)
print(' ')
# exercise 1 c
"""Sprawdza, czy w danym słowniku znajduje się conajmniej podana liczba elementów"""


def check_dictionary_content(d, **kwargs):
    # for k,v in kwargs.items():
    #   print(k,v) wypisanie kwargs
    # jak v<=0 to nie ma co sprawdzac
    return all(v <= 0 or k in d and d[k] >= v for k, v in kwargs.items())


print('exercise 1c')
d = {'orange': 3, 'apple': 1, 'dogs': 10}
print(check_dictionary_content(d, orange=2) == True)
print(check_dictionary_content(d, orange=2, apple=1) == True)
print(check_dictionary_content(d, dogs=11) == False)
print(check_dictionary_content(d, dogs=9, cats=0) == True)
print(check_dictionary_content(d, apple=0, cats=1) == False)
print(check_dictionary_content(d, **d) == True)
print('  ')
# exercise 2
'''Napisz funkcję która dla listy liczb zwróci listę częściowych udziałów w sumie tych liczb'''


def numbers_to_percents(values):
    return [p / sum(values) for p in values]


print('exercise 2')
print(numbers_to_percents([1, 2, 1]) == [0.25, 0.5, 0.25])
print(numbers_to_percents([1]) == [1])
print(numbers_to_percents([1, 2, 3, 4]) == [0.1, 0.2, 0.3, 0.4])
print(' ')

# exercise 3a
'''
a) Napisz funkcję zwroc_rosnace która dostanie na wejsciu funkcje jednoargumentową oraz argumenty do niej a następnie zwróci te argumenty dla których wynik jest większy od argumentu'''


def zwroc_rosnace(f, *ags):
    return [a for a in ags if f(a) > a]


def f1(n):
    return n ** 2 - 3 * n


def f2(n):
    return 100 - n


def f3(word):
    return word[::-1]


print('exercise 3a')
print(zwroc_rosnace(f1, 4, 6, 2, -5) == [6, -5])
print(zwroc_rosnace(f2, *range(100)) == list(range(50)))
print(zwroc_rosnace(f3, "python", "nie", "jest", "bardzo", "fajny") == ['jest', 'bardzo', 'fajny'])
print(' ')

# exercise 3b
'''
b) Dopisz drugą, podobną funkcję która będzie zwracać argumenty których wyniki są większe od wyników poprzedniego argumentu
'''


def zwroc_rosnace2(f, *args):
    return [args[a] for a in range(1, len(args)) if f(args[a]) > f(args[a - 1])]


def f1(n):
    return n ** 2 - 3 * n


def f2(n):
    return 100 - n


def f3(word):
    return word[::-1]


print('exercise 3b')
print(zwroc_rosnace2(f1, 4, -5, 6, 2) == [-5])
print(zwroc_rosnace2(f2, *range(100)) == [])
print(zwroc_rosnace2(f3, "python", "nie", "jest", "bardzo", "fajny") == ['jest', 'fajny'])
print(' ')
# exercise 4
'''
Napisz funkcję która będzie zwracała który raz jest wywoływana
'''
a = 0


def ile_wywolana():
    global a
    a = a + 1
    return a


print('exercise 4')
print(ile_wywolana() == 1)
print(ile_wywolana() == 2)
print(ile_wywolana() == 3)
print(' ')
# exercise 5
'Napisz generator zwracający nieskończony ciąg licz pierwszych'


def is_prime(n):
    if n < 2:
        return False
    return not any(n % k == 0 for k in range(2, n))


def get_primes2():
    a = 0
    while True:
        if is_prime(a):
            yield a
            a = a + 1
        else:
            a = a + 1


result = get_primes2()

print('exercise 5 - generuje 10 pierwszych liczb pierwszych')
for p in range(10):
    print(next(result))
print(' ')

print('exercise 6a')
# exercise 6 a
'''
Uzupełnij definicje poniższych funkcji/generatorów.'''
"""Tworzy generator liczb naturalnych od liczby k"""


def natural_numbers(k=0):
    while True:
        yield k
        k = k + 1


import types

print(isinstance(natural_numbers(), types.GeneratorType))

for i, n in enumerate(natural_numbers()):
    print(i, i == n)
    if i > 20:
        break
print(' ')
for i, n in enumerate(natural_numbers(1)):
    print(i, i + 1 == n)
    if i > 20:
        break

print(' ')
# exercise 6 b
"""Tworzy generator kolejnych silnii"""


def factorials():
    yield 1
    yield 1
    yield 2
    actual_number = 3
    count = 2
    while True:
        yield actual_number * count
        count = actual_number * count
        actual_number = actual_number + 1
    pass


print('exercise 6 b')
import types

print(isinstance(factorials(), types.GeneratorType))

results = [1, 1, 2, 6, 24, 120, 720, 5040]
for truth, answer in zip(results, factorials()):
    print(truth, truth == answer)

print(' ')

# exercise 7
'''Napisz generator nieskończonego ciągu liczb Fibonacciego.'''


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


print('exercise 7')
generator = fibonacci()
for p in range(10):
    print(next(generator))
