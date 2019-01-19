
'''zadanie 1
Prepare a demo of the program finding zero space using the Newton method. Using argparse (link) or optparse (link), handle:
fixed starting point,
step size in a derivative,
number of method steps,
accuracy
help
We run the program by specifying, e.g.

./newton.py x ** 2 + x + 1 -h 0.00001
'''
import argparse
import parser


def derv(f, x0, dx):
    x = x0
    f_x = eval(f)
    x = x0 + dx
    f_x_dx = eval(f)
    return (f_x_dx - f_x) / dx


arg_parser = argparse.ArgumentParser(description='Newton Method')

arg_parser.add_argument('formula', type=str, help='function_formula (use x as the variable name)')
arg_parser.add_argument('start_point', type=float, help='Start point')
arg_parser.add_argument('step', type=float, help='Step size')
arg_parser.add_argument('steps', type=int, help='Number of steps')
arg_parser.add_argument('precision', type=float, help='Desired precision')

args = arg_parser.parse_args()
print("---------")
print("Args")
print(args)
print("---------")

x_k = args.start_point
print(f"Starting from point {x_k}")

code = parser.expr(args.formula).compile()
print(code)

for i in range(args.steps):
   x = x_k
   x_k = x_k - (eval(code)) / derv(code, x_k, args.step)
   print(f'Current point is: {x_k}')

'''
Exercise 2
The task should be performed using the BagOfWords program from previous classes.
Make it so that punctuation, numbers and all other characters do not interfere with
parsing text. Run it on the text of the hamlet. How many times does the word hamlet appear?
  What are the ten most common words?
'''
from io import IOBase
import re
from collections import defaultdict


class BagOfWords:
    def __init__(self, text):
        if isinstance(text, IOBase):
            text = text.read()
        self.text = re.sub(r'[^a-zA-Z ]', '', text)
        self.words = defaultdict(int)
        for word in self.text.split():
            self.words[word] += 1

    #         self.words={x:sum(1 for y in text.split() if x==y) for x in text.split()}

    def __str__(self):
        return str(self.words)

    def __iter__(self):
        return iter(sorted(self.words, key=self.words.get, reverse=True))

    def __add__(self, other):
        return BagOfWords(self.text + ' ' + other.text)

    def __getitem__(self, key):
        if key not in self.words:
            return 0
        else:
            return self.words[key]

    def __setitem__(self, key, item):
        self.words[key] = item
        self.text += (' ' + key) * (item - self[key])



import requests
file = requests.get("http://www.gutenberg.org/cache/epub/1787/pg1787.txt", stream=True)
with open("hamlet.txt", 'wb') as location:
    location.write(file.content)

hamlet = BagOfWords(open('hamlet.txt'))
print(hamlet['Hamlet'])
for i, v in enumerate(hamlet):
    print(v)
    print(hamlet[v])
    if i == 10:
        break

'''
exc 3
Use the pickle to save and read the class from the previous task of Hamlet. Compare methods and size.
'''
import pickle
for i in range(5):
    with open('ham'+str(i)+'.pickle', 'wb') as pickle_file:
        pickle.dump(hamlet,pickle_file, i)

'''
exc 4
By using https://gist.github.com/pamelafox/986163
enter the current time in: all countries, showing
grouped to the continents,
run a simulation display
  more countries as the country breaks north,
  the display delay sets proportional to the real time
'''


from time import time
import shutil
from datetime import datetime
import pytz
import requests
from setuptools.namespaces import flatten

import pprint

file = requests.get(
    "https://gist.github.com/pamelafox/986163/raw/f5f9db4f1b287804fd07ffb3296ed0036292bc7a/countryinfo.py",
    stream=True).raw
with open("mycountryinfo.py", 'wb') as location:
    shutil.copyfileobj(file, location)
import mycountryinfo

countryList = {y['continent']: {x['name']: datetime.now(pytz.timezone(x['timezones'][0])).strftime("%H:%M:%S") for x in
                                mycountryinfo.countries if x['continent'] == y['continent']} for y in mycountryinfo.countries}
pprint.pprint(countryList)
# while True:
#     countryList = {
#         y['continent']: {x['name']: datetime.now(pytz.timezone(x['timezones'][0])).strftime("%H:%M:%S") for x in
#                          mycountryinfo.countries if x['continent'] == y['continent']} for y in mycountryinfo.countries}
#     a = list(flatten([[y for y, z in x.items() if z == "00:00:00"] for _, x in countryList.items()]))
#     if a:
#         print(a)






'''
exc 5
For the BagOfWords class, write save and load methods that use json to write and read data.
'''
import json
from io import IOBase
import re
from collections import defaultdict


class BagOfWords:
    def __init__(self, text):
        if isinstance(text, IOBase):
            text = text.read()
        self.text = re.sub(r'[^a-zA-Z ]', '', text)
        self.words = defaultdict(int)
        for word in self.text.split():
            self.words[word] += 1

    #         self.words={x:sum(1 for y in text.split() if x==y) for x in text.split()}

    def __str__(self):
        return str(self.words)

    def __iter__(self):
        return iter(sorted(self.words, key=self.words.get, reverse=True))

    def __add__(self, other):
        return BagOfWords(self.text + ' ' + other.text)

    def __getitem__(self, key):
        if key not in self.words:
            return 0
        else:
            return self.words[key]

    def __setitem__(self, key, item):
        self.words[key] = item
        self.text += (' ' + key) * (item - self[key])

    def save(self, filename):
        with open(filename, 'w') as outfile:
            json.dump(self.words, outfile)

    @staticmethod
    def load(filename):
        with open(filename, 'r') as inpfile:
            data = json.load(inpfile)
            return BagOfWords(''.join([(k + ' ') * v for k, v in data.items()]))