
#NUMPY
import numpy as np
'''1) Create a 3x3 table containing numbers from 0 to 8, then add the rows. Expected result: [9,12, 15]'''
array=np.arange(9).reshape(3,3)
print(array.sum(axis=0)) # axis=0 lub axis=1 w zaleznosci po czym chce sumowac
'''2)  Create an identity matrix with 4x4 dimensions (or a more difficult version create an identity matrix with True, False values)'''
array=np.eye(4,4)
print(array)
array=array>0
print(array)
'''3) Create a 3x3x3 matrix filled with random numbers '''
array=np.random.rand(27).reshape(3,3,3)
print(array)
'''4)Create a 5x5 matrix where each row will be in the range of 0.4. Expected result:
[[0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]
 [0. 1. 2. 3. 4.]]'''
array=np.arange(0,0.5,0.1)
array=np.repeat(array,5).reshape(5,5).transpose()
print(array)
'''5) Find items where elements from list a and b are equal. Sample lists:'''
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
result=np.where(a==b)
print(result)
'''6) Display all elements from the list that are in the range [0.5]'''
a = np.array([1,2,5,6,7,9,2,3,4])
result=np.where(np.logical_and(a>=0, a<=5))
print(result)
#PANDAS
'''1) Count the frequency of instances of each unique value in the given series'''

import pandas as pd
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
print(ser)
counts=ser.value_counts().to_dict()
print(counts)
'''2) convert to one series.
Dane:
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
Oczekiwany wynik:

0       Red
1     Green
2     White
3       Red
4     Black
5    Yellow
dtype: object'''
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
df=pd.Series((v[i] for v in s for i in range(len(v))))
print(df)


'''
3) Create a DataFrame with 3 columns (A, B, C) and 5 lines. Column A is supposed to contain values from the uniform distribution from 0.1 to rounded to 2 decimal places. Column B is supposed to contain random values from the set ['k', 'm', None] and in column C random values True or False with distribution p (True) = 0.6 and p (False) = 0.4. Example answer:
      A B C
0 0.96 None True
1 0.77 m True
2 0.84 k True
3 0.45 m False
4 0.09 k False
'''
df = pd.DataFrame(0,[0,1,2,3,4], ['A','B','C'])
df['A']=np.random.rand(5).round(2)
df['B']=np.random.choice(['k','m',None],5)
df['C']=np.random.choice([True,False],5,p=[0.6,0.4])
print(df)
#INNE
'''
  Implement the stack using a list with pop, push, isempty
'''
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


stack = Stack()
print(stack.isEmpty())
stack.push('K')
stack.push('A')
stack.push('R')
stack.push('O')
stack.push('L')
print(stack.items)
while not (stack.isEmpty()):
    print(stack.pop())
'''Implement the stack with pop, push, isempty and in the constant time checks the maximum and minimum'''
class Value(object):
    def __init__(self, value):
        self.value = value


class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        v = Value(item)
        if len(self.items) == 0:
            v.max = item
            v.min = item
        else:
            if item > self.items[len(self.items) - 1].max:
                v.max = item
            else:
                v.max = self.items[len(self.items) - 1].max

            if item < self.items[len(self.items) - 1].min:
                v.min = item
            else:
                v.min = self.items[len(self.items) - 1].min
        self.items.append(v)

    def max(self):
        return self.items[len(self.items) - 1].max

    def min(self):
        return self.items[len(self.items) - 1].min

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(5)
stack.push(3)
stack.push(9)
stack.push(12)
print(stack.max())
stack.pop()
print(stack.max())
print(stack.min())
'''Write the functions that accept the letter of the tuples. A single tupla consists of the first name, last name and height. The function returns a list started first by name, last name and last after the increase. Example
input: [(a, b, 1), (a, b, 2), (a, a, 3), (c, b, 4), (a, b, 0), (b, c, 9) ]
output: [(a, a, 3), (a, b, 0), (a, b, 1), (a, b, 2), (b, c, 9), (c, b, 4) ]
*** we assume that the input data is correct'''
from operator import itemgetter
l=[('Tom',19,80),('Tom',19,99),('Tom',19,91),('Json',27,93),('Json',21,85)]
print (sorted(l, key=itemgetter(0,1,2)))
'''
under the address of the url there is a json file http://live.euroleague.net/api/Boxscore?gamecode=22&seasoncode=E2018&disp= containing the stats of the players from the basketball match.
Write a program that will read the name and surname of the player and check how many points he scored in the match. The program's start is given at the bottom.
import requests
import json
s = requests.session()
match_url =' http://live.euroleague.net/api/Boxscore?gamecode=22&seasoncode=E2018&disp='
game = s.get(match_url).text'''
import requests
import json
s = requests.session()
match_url =' http://live.euroleague.net/api/Boxscore?gamecode=22&seasoncode=E2018&disp='
game = s.get(match_url).text
p_in=input()
print(p_in)
game_json = json.loads(game)
players_first_team = game_json['Stats'][0]['PlayersStats']
second_team_players = game_json['Stats'][1]['PlayersStats']
players = players_first_team + second_team_players
for p in range(0,24):
    #print(players[p]["Player"])
    if p_in ==str(players[p]["Player"]):
        print(players[p]["Points"])

'''
We have one hundred two-position switches (ie ones that can be either turned on or off).
Next, we make a hundred steps, at every step we switch every N-th switch
  (where N is the step number). So in the first step we switch all, in the second, only even
   (every second), in the third step the third, the sixth, the ninth and so on until the 99th, in the fourth - every fourth,
   and so on, until the hundredth step in which we switch the last hundredth switch.
How many switches will be switched on after all 100 steps? At the beginning, all switches are turned off.
'''
tab= [False]*100
for change_on in range(1,100):
    tab=[not value if (indx+1)%change_on==0 else value for indx,value in enumerate(tab)]
    print(tab)
print(len(list(filter(lambda x:x==True,tab))))
