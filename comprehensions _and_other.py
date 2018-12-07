# exercise 1
""" Sprawdza czy podane wyrazy są anagramami """

"" "Checks if the given words are anagrams" ""

def check_anagram(first, second):
    return sorted(first) == sorted(second)


'''
def check_anagram(first, second):
    return {k: sum([1 for x in first if k == x]) for k in first} == {k: sum([1 for x in second if k == x]) for k in second}
'''


def gaderypoluki(text, key):
    """ The function should
    encrypt( or decrypt) the
    text
    with GADERYPOLUKI( or similar)
    https: // pl.wikipedia.org / wiki / Gaderypoluki
    """
    key = key.lower()
    text = text.lower()
    d = {k: v for k, v in zip(key[::2] + key[1::2], key[1::2] + key[::2])}
    return ''.join([d.get(x, x) for x in text])


print(gaderypoluki('Ala ma kota', 'GADERYPOLUKI') == 'gug mg iptg')
print(gaderypoluki('gug mg iptg', 'GADERYPOLUKI') == 'ala ma kota')

print('exercise 1')
print(check_anagram("abcd", "dcba") == True)
print(check_anagram("aba", "baa") == True)
print(check_anagram("aba", "ba") == False)
print(check_anagram("tom marvolo riddle ", "i am lord voldemort") == True)
print(' ')
# exercise 2,3,4
'''Zapisz każdą z poniższych 4 funkcji w postaci list/dict/set comprehension. Nie należy używać żadnych zmiennych tymczasowych ani dodatkowych linii, każda funkcja ma zostać wyrażona w postaci: 
def FUNKCJA(ARGUMENTY):
    return COMPREHENSION'''
'''Write each of the following 4 functions in the form of list / dict / set comprehension. Do not use any temporary variables or additional lines, each function is to be expressed in the form:
def FUNCTION (ARGUMENTS):
     return COMPREHENSION '''
# exercise 2
"""Zwraca podlistę "data" zawierającą wyłącznie parzyste liczby"""
"" "Returns the data sub-list containing only even numbers" ""

def even_numbers_from_list(data):
    return [d for d in data if d % 2 == 0]


print('exercise 2')
print(even_numbers_from_list([1, 2, 3, 4]) == [2, 4])
print(even_numbers_from_list(range(10)) == list(range(0, 10, 2)))
print(even_numbers_from_list(range(1000)) == list(range(0, 1000, 2)))
print(even_numbers_from_list([10, 2, 3, 4, 6, -3, -4]) == [10, 2, 4, 6, -4])
print(' ')

# exercise 3
"""Zwraca listę trójek, gdzie i'ta trójka to (i, i'te słowo, długość i'tego słowa)"""
"" "Returns a list of triples, where i and threes are (i, i'te word, length i'th words)" ""

def words_analyze(words):
    return [(words.index(word), word, len(word)) for word in words]


print('exercise 3')
print(words_analyze(['tomek', 'jadzia']) == [(0, 'tomek', 5), (1, 'jadzia', 6)])
print(words_analyze([]) == [])
print(' ')

# exercise 4
"""Zwraca słownik gdzie kluczami są wszystkie słowa występujące w tekście
    rozpoczynające się na zadaną literę, a wartością ile razy wystąpiy"""

"""Returns a dictionary where the keys are all words appearing in the text
     beginning with a given letter, and the number of times appears"""
def count_words_starting_with_given_letter(text, letter):
    return {word: len([w for w in text.split() if w == word]) for word in text.split() if word[0] == letter}


print('exercise 4')
print(count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'o') == {'ola': 2, 'o': 1})
print(count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'k') == {'kota': 1})
print(count_words_starting_with_given_letter('ola ma kota o imieniu ola', 'x') == {})
print(' ')
# exercise 5
'''
    Funkcja przyjmuje:
    - dwa słowniki a i b
    - dwuargumentową funkcję f
    Funkcja jako wynik powinna zwrócić słownik, który będzie sumą dwóch słowników.
    Sumę dwóch słowników powinniśmy rozumieć jako słownik, w którym zbiór kluczy będzie równy
    sumie zbiorów kluczy ze słowników a i b. Gdy jakiś klucz występuje w obu słownikach, to wartość ma być
    wynikiem funkcji f obliczonej na wartościach dla danego klucza w słowniku a i słowniku b
    '''
'''
The function accepts:
     - two dictionaries a and b
     - the two-argument function f
     Function as a result should return a dictionary, which will be the sum of two dictionaries.
     The sum of two dictionaries should be understood as a dictionary in which the set of keys will be equal
     sum of key sets from dictionaries a and b. When a key exists in both dictionaries, the value is to be
     the result of the function f calculated on the values for a given key in dictionary a and dictionary b
'''


def merge_dicts(a, b, f):
    return {k: f(a[k], b[k]) if k in a.keys() and k in b.keys() else a[k] if k in a.keys() else b[k] for k in
            set(list(a.keys()) + list(b.keys()))}


def add(a, b):
    return a + b


print('exercise 5')
print(merge_dicts({'a': 1}, {'b': 1}, add) == {'b': 1, 'a': 1})
print(merge_dicts({'a': 1, 'b': 2}, {'b': 1}, add) == {'b': 3, 'a': 1})
print(merge_dicts({'a': 1, 'b': 2}, {'b': 1, 'c': 3, 'a': 7}, add) == {'c': 3, 'b': 3, 'a': 8})
print(' ')

from math import sqrt

# exercise 6
"""Zwraca zbiór liczb pierwszych od 0 do N włącznie"""
'''Returns a set of prime numbers from 0 to N inclusive'''

def primes(N):
    return {prime_number for prime_number in range(2, N + 1) if
            not any(prime_number % y == 0 for y in range(2, prime_number))}


print('exercise 6')
print(primes(5) == {2, 3, 5})
print(primes(10) == {2, 3, 5, 7})
print(primes(100) == {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97})
print(' ')
# exercise 7 - 1
'''
Wykorzystując znieżdzenia generatorów list (https://www.python.org/dev/peps/pep-0202/) napisz funkcje, która
wypisze wszystkie pary (x,y) gdzie 0 < x < n oraz 0 < y < n
'''
'''
Using the list of letter generators (https://www.python.org/dev/peps/pep-0202/) write the functions that
will print all pairs (x, y) where 0 <x <n and 0 <y <n
'''
def func1(n):
    return [(x, y) for x in range(n) for y in range(n)]


print('exercise 7-1')
print(func1(3) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)])
print(func1(0) == [])
print(' ')
# exercise 7 - 2
'''
wypisze tylko takie pary dla których x < y
'''

'''
will print only pairs for which x <y
'''

def func2(n):
    return [(x, y) for x in range(n) for y in range(n) if x < y]


print('exercise 7-2')
print(func2(3) == [(0, 1), (0, 2), (1, 2)])
print(func2(4) == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)])
print(' ')

# exercise 7-3
'''
wypisze tylko takie pary dla których x > y
'''
'''
will print only pairs for which x >y
'''

def func3(n):
    return [(x, y) for x in range(n) for y in range(n) if x > y]


print('exercise 7-3')
print(func3(3) == [(1, 0), (2, 0), (2, 1)])
print(func3(4) == [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)])
print(' ')

# exercise 8
'''
Napisz funkcję powerset, która zwróci listę wszystkich podzbiorów zadanej listy przekazanej jako argument
'''

'''
Write the function powerset, which will return a list of all subsets of the given list passed as an argument
'''
def powerset(x):
    result = [[]]
    for item in x:
        subsetlist = []
        for subset in result:
            subsetlist.append(subset + [item])
        result.extend(subsetlist)
    return result


print('exercise 8')
print(powerset('abc') == [[], ['a'], ['b'], ['a', 'b'], ['c'], ['a', 'c'], ['b', 'c'], ['a', 'b', 'c']])
print(powerset([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
print(powerset(['abc', 5, 6]) == [[], ['abc'], [5], ['abc', 5], [6], ['abc', 6], [5, 6], ['abc', 5, 6]])
