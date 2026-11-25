# from random import random
# from collections import defaultdict
# import datetime
# import dateutil.parser
import random as rad
import keyword as python_keywords
from new_file import run_script

print(run_script('chinedu', 'ned'))
# from array import *
# # While python lists can contain values corresponding to diﬀerent data types, arrays in python can only contain
# # values corresponding to same data type. In this tutorial, we will understand the Python arrays with few examples.

# my_array = array('i', [1, 2, 3, 4, 5])
# another_array = array('x', ['ned', True, 2, 4, {'a': 1, 'b': 2}])
# print(my_array[1])
# print(another_array[3])
# print(datetime.date(2026, 11, 14))
# print(datetime.time(8, 27, 18))
# print(datetime.datetime(2026, 11, 14, 8, 27, 18))
# val = random()
# print(val)
# def flip_coin():
#     rand = random()
#     if rand > 0.5:
#         return "Heads"
#     else:
#         return "Tails"

# def is_odd_number(num):
#     if num % 2 != 0:
#         return True
#     else:
#         return False

# print(is_odd_number(4))
# print(is_odd_number(9))

# instructor = 'Colt'

# def say_hello():
#     return f"Hello {instructor}"
# print(say_hello())

# total = 0
# def increment():
#     total += 1
#     return total

# first_value = hash(25)
# second_value = hash(25)

# print(first_value == second_value)
# print(first_value is second_value)
# test_set = {1, 2, 3, 4, 5}
# test_set.add(6)
# print(test_set)
# print(len([]))
# list_arr = ["Alice","Bob","Craig","Diana","Eric"]

# idx = list_arr.index("Diana")
# print(idx)

state_capitals = {
    "Arkanasas": "Little Rock",
    "Colorado": "Denver",
    "California" : "Sacramento",
    "Georgia": "Atlanta"
}

# for key, value in state_capitals.items():
#     print(f"the capital of {key} is : {value}")
# for key in state_capitals.keys():
#     print('the state of {} the capital is {}'.format(key, state_capitals[key]))

# my_set = {1, 2, 3, 4, 6}
# for s in my_set:
#     print(s)

# student = defaultdict(list)

# print(student["levels"])
# student = {
#     "name": "John",
#     "age": 20
# }
# def default_name():
#     return "Unknown"

# student = defaultdict(default_name, student)

# print(student["level"])
# print(student["age"])

# print(dir(__builtins__))

# a = frozenset('abracatanbra')
# a.add('z')
# print(a)
# long_num = 123456L
# print(dir(datetime))
# dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
# print(dt)

# dtm = 

# def outer():
#     x = 10

#     def inner():
#         x = 20
#         print("Inner: ", x)

#     inner()
#     print("Outer: ", x)
# outer()

# def outer():
#     x = 10
    
#     def inner():
#         nonlocal x
#         x = 20
#         x = x + 5
#         print("Inner: ", x)
#     inner()
#     print("Outer: ", x)

# outer()
# def foo():
#    if True:
#        a = 5
#        print(a)
# foo()
# def boo():
#     if False:
#         b = 20
#         print(b)
# boo()
# total = 0
# def increment():
#     global total
#     total += 1
#     return total

# print(increment())

# def colorize(text, color):
#     colors = ("cyan", "yellow", "blue", "green", "magenta")
#     if type(text) is not str:
#         raise TypeError("text must be instance of str")
#     if color not in colors:
#         raise ValueError("color is invalid color")
#     print(f"Printed {text} in {color}")

# colorize("hello", "red")

# try:
#     foobar
# except:
#     print("Problem")
# print("after the try")

# try:
#     colt
# except NameError:
#     print("this is the nameError")

# try:
#     num = int(input("please enter number: "))
# except Exception as error:
#     print(f"this is not a number {error}")
# else:
#     print("this ran because the try block run")
# finally:
#     print("this is the finally block that runs clean up")
# the else block runs when the try block is successful,

# def divide(a,b):
#     pdb.set_trace()
#     try:
#         result = a / b
#     except Exception as error:
#         print(f'something went wrong, {error}')
#     else:
#         print("this ran because the try block is successful")
#         return result

# print(divide(10,'a'))

print(rad.choice(["apple", "banana", "cherry", "durian"]))

"""
import random
import random as omg_so_random
from random import *
from random import choice, shuffle
from random import choice as randItem, shuffle as 
"""


def contains_keyword(*args):
    for words in args:
        if python_keywords.iskeyword(words):
            return True
    return False

