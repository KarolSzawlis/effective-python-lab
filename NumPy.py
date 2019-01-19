import numpy as np

'''
Excercise 1.
Create a random array of 10,000 numbers, then add 1 to each element.
Then write the exact same function using numpy and its tables. Compare the duration of your solutions.
'''
p = np.random.rand(10000)
print(p)
print(len(p))
p = p + 1
print(p)
'''
Exercise 2.
Write functions that calculate 10,000 random numbers for each element of the array using a loop and using numpy, compare their speed as in the previous task.
'''
np_array = np.random.rand(10000)
np_array = np.sin(np_array) + np.cos(np_array)
'''
Exercise 3.
Write a more powerful form of the following functions. Add every test confirming the speed of the suggested solution.
def cube_sum(x):
    """Zwraca sume szescianow elementow"""
    result = 0
    for i in range(len(x)):
        result += x[i] ** 3
    return result

def almost_variance(x):
    """Oblicza 1/n * SUM (x_i - mean(x))^4"""
    m = sum(x) / len(x)
    result = 0
    for i in range(len(x)):
        result += (x[i] - m) ** 4
    result /= len(x)
    return result
'''


def cube_sume(x):
    return sum(x ** 3)


print(cube_sume(np.array([1, 2, 3])))


def almost_variance(x):
    return 1.0 / x.size * np.sum(np.power(x - np.mean(x), 4))


'''
Zadanie 4.
Using broadcasting (see the figure below) create a multiplication table, i.e. tables such that
Can you do it with one command
without using loops /comprehensions?
'''
A = (np.arange(1, 11).reshape((10, 1)) * np.arange(1, 11))
print(A)

'''
exc 6.
Write functions for "whitening" a set of points, i.e. applying the following transformation
(again, do it without using loops etc.) where is the average of the following column,
  and this is the standard deviation after this column, e.g.
  In particular, the average for individual columns of the new matrix should be 0 and standard deviation 1.
  '''


def white(x):
    mean = np.mean(x, 0)
    std = np.std(x, 0)
    return ((x - mean) / std)


arr = np.reshape(np.arange(10), (5, 2))
print(white(arr))
'''
exc 7
Having given tables of any size (for simplicity, you can accept one or two) and number x find the closest x value in A, i.e.
for example.
Again, can you do it without a loop, etc.?
'''


def closest(x, A):
    return A[np.argmin(np.abs(x - A))]


print(closest(1.5, np.array([1, -4.3])))
'''
exc 8 
implement a simple polynomial calculation with given coefficients
'''


def poly(x, a):
    return a.pop() + sum(np.cumprod(np.full(len(a), x)) * a[::-1])


print(poly(0.5, [1, 2, 3]))
print(np.poly1d([1, 2, 3])(0.5))
'''Zad 9.
Write functions for image processing to gray scale according to the following formula:
'''
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('images/pie.png')
plt.imshow(img)
plt.imshow(np.sum(img * np.array([0.2126, 0.7152, 0.0722]), axis=2), cmap='gray')
'''
Task 10.
Only with the help of the numpy methods, write the code for linear interpolation between a pair of points (any dimensionality) by the formula:

The code should immediately generate interpolations for many values, eg for 10 different ones
'''
x1 = np.array([1, 2, 3, 5])
x2 = np.array([5, 4, 3, 9])
lambda_ = np.arange(0, 1.1, 0.1)
print((x1.reshape(-1, 1) * lambda_ + (1 - lambda_) * x2.reshape(-1, 1)).T)
