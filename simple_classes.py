import re

# exc 1 regexy

# exc 2 - Regexy
'''Atoms
Write a program that (using regular expressions) filters the atoms.log file so that only the lines for a problem-free experiment will remain. ie, for example, such lines as
RUN 000039 COMPLETED. OUTPUT IN FILE yttrium.dat. 1 UNDERFLOW WARNING.
whether
RUN 000058 COMPLETED. OUTPUT IN FILE cerium.dat. ALGORITHM DID NOT CONVERGE AFTER 100000 ITERATIONS.
you can only assume that each line fits the following scheme
RUN [[NUMBER OF EXACTLY 6 DIGITS]] COMPLETED. OUTPUT IN FILE [[NAME]]. Date. [[ANYTHING]]'''
regex = re.compile('^RUN[ ][0-9]{1,6}[ ]COMPLETED. OUTPUT IN FILE (.*?).dat.$')
i = 0
j = 0
with open('atoms.txt', 'r') as G:
    for line in G:
        if regex.match(line):
            print(line)

import re

pattern = r'^RUN \d{6} COMPLETED. OUTPUT IN FILE .+\.dat.$'

with open('lab6_files/atoms.log') as atoms:
    for line in atoms:
        if re.match(pattern, line):
            print(line)
# exc 3
'''
messages
Write a program that prints lines from the system log "messages.txt" that contain information about the invalid username ('invalid user') '' '
'' '
Process the program so that it displays formatted messages, i.e.
Jun 29 20:18:40 noether sshd [5805]: Invalid user tester from 218.189.194.200
should be converted into
Niepoprawna nazwa użytkownika: "tester", połaczenie z 218.189.194.200 nawiązano 29 czerwca o godz. 20:18
'''

pattern = r'^(\D{3} \d+) (\d{2}:\d{2}:\d{2}) .+ Invalid user (.+) from ((\d+\.){3}\d+)$'

with open('lab6_files\messages.txt') as messages:
    for line in messages:
        match = re.match(pattern, line)
        if match:
            print('Niepoprawna nazwa użytkownika: "' + match.group(3) + '", połączenie z ' + match.group(4) +
                  ' nawiązano ' + match.group(1) + ' o godz. ' + match.group(2))
# exc 4 - Collections
from collections import Counter


def count_letters(word):
    cnt = Counter()
    for w in word:
        cnt[w] += 1
    return cnt


print(count_letters('aaaaa') == {'a': 5})
print(count_letters('abbccaaaa') == {'a': 5, 'b': 2, 'c': 2})
print(count_letters('abc') == {'a': 1, 'b': 1, 'c': 1})

from collections import defaultdict


def group_words_by_first_letter(text):
    d = defaultdict(list)
    for word in text.split():
        d[word[0]].append(word)
    return d


print(group_words_by_first_letter("ala ma kota") == {'a': ['ala'], 'm': ['ma'], 'k': ['kota']})
print(group_words_by_first_letter("ala ma kota ala ma psa") == {'a': ['ala', 'ala'], 'm': ['ma', 'ma'], 'k': ['kota'],
                                                                'p': ['psa']})
print(group_words_by_first_letter("ala ma kota ale marysia ma konia") == {'a': ['ala', 'ale'],
                                                                          'm': ['ma', 'marysia', 'ma'],
                                                                          'k': ['kota', 'konia']})


# exc 5
class FrozenDictionary(object):
    """
    The equivalent of frozenset for sets, i.e. a dictionary that is not modifiable,
     and thus it can be, for example, an element of sets, or a key in another dictionary.
    """

    def __init__(self, dictionary):
        """Creates a new frozen dictionary from the given dictionary"""
        self.dictionary = dictionary

    def __hash__(self):
        result = 0
        for k, v in self.dictionary.items():
            result += hash(k) + hash(v)
        return result

    def __eq__(self, d):
        """Compares our dictionary with the frozen dictionary d"""
        return self.dictionary == d.dictionary

    def __repr__(self):
        """Returns the representation of our dictionary as a string"""
        return repr(self.dictionary)
        # return str(self.dict) wersja golisza


print('-----------------------------------------------------------------------')
dicts = [FrozenDictionary({'ala': 4}),
         FrozenDictionary({'ala': 1, 'jacek': 0}),
         FrozenDictionary({'ala': 4}),
         FrozenDictionary({'ala': 2}),
         FrozenDictionary({'jacek': 0, 'ala': 1})]

s = set(dicts)
print(dicts[0] == dicts[2])
print(dicts[0] != dicts[3])
print(len(s) == 3)

# Should be something like this: set([{'ala': 4}, {'ala': 1, 'jacek': 0}, {'ala': 2}])
print(s)
print('-----------------------------------------------------------------------')


# exc 6

class BagOfWords(dict):
    def __init__(self, arg=''):
        if type(arg) != str:
            arg = arg.read()
        for word in arg.split():
            self[word] = arg.count(word)

    def __str__(self):
        tuple_list = [(key, val) for key, val in self.items()]
        sorted_list = [(key, value) for key, value in reversed(sorted(tuple_list, key=lambda x: x[1]))]
        return str(sorted_list)

    def __contains__(self, item):
        return item in self.keys()

    def __iter__(self):
        tuple_list = [(key, val) for key, val in self.items()]
        sorted_list = [key for key, _ in reversed(sorted(tuple_list, key=lambda x: x[1]))]
        return iter(sorted_list)

    def __add__(self, item):
        new_bag = BagOfWords()
        self_set = set(self.keys())
        item_set = set(item.keys())
        for key in self_set.union(item_set):
            if key in self_set and key in item_set:
                new_bag[key] = self[key] + item[key]
            elif key in self_set:
                new_bag[key] = self[key]
            else:
                new_bag[key] = item[key]
        return new_bag


bow1 = BagOfWords("ala ma kota ala ma ala")
bow2 = BagOfWords("tomek tez ma kota")
bow3 = bow1 + bow2
print('tomek' in bow1)  # False
print('tomek' in bow3)  # True
print('ala' in bow3)  # True
print(bow3)  # ala:3, ma:3, kota:2, tez:1, tomek:1
