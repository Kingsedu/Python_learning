# Two main types of numbers:
# integer # Floating Point # Long #complex number;
# main uses are integer and Floating Point;
# by defaults python divisions are float;
# integer division //
# print( 1 / 3 )
# # print( 1/2 * 2 )
# print(10 % 3)
# print(25 % 4)
# print(13 % 2)

# print(10 // 3)

# x = 100
# kha_le_esi_mother_of_dra_gos = 1
# print(x + kha_lee_si_mother_of_dra_gos)
# python_is_awesome = 100
# just_another_variable = python_is_awesome
# print(just_another_variable + python_is_awesome)
# print(type(just_another_variable + python_is_awesome))
# my_name, my_age, my_class = 'Kingsley', 25, 'pieces'
# print(my_name)
# __no_touchy_
# in python -> integers, strings, lists, dictionaries, and even functions are object
# mutable
# python types ---> int, float, bool, str, tuple (Not mutable);
# python types ---> list, dict, sets (mutable)
# game_over = False

# print(game_over)
# number_of_nothingness = None

# number_of_nothingness = {}

# print(number_of_nothingness)

# #NoneType
# value_name = None

# if value_name and value_name is None:
#     print("instance of None type")

# str_one = "player"
# str_two = "stupid coach"
# print(str_one + " " + str_two)

# num_one = 10
# num_one += 30

# # num_one = 10 + 30
# print(num_one)

# x = 20
# formatted = f"i 've told you {x} times already"

# print(formatted)
# print(f"this is a way of doing a string")

# formatted_decimal = "i've nothing with {} number".format(10 / 2)
# print(formatted_decimal)
string_name = "teddy"
# print(type(string_name[0]))
# string_name[0] = 'd'
# print(string_name)
# strings in python are not mutable

# value_one = 3.14256
# int_value_one = int(value_one)
# print(int_value_one)
# int_value = 10
# float_int_value = float(int_value)
# print(float_int_value)
# for x in ['a', 'b', 'c', 'd']:
#     print(x)

# def convertor_app():
#     num_miles = input('how many miles did your run today: ')
#     if(type(num_miles) is str):
#        converted_number = int(num_miles) * 2.4
#     return f"this is the {converted_number} from miles to kilometer"

# print(convertor_app())
# color = "purple"

# if(color == "purple"):
#     print("the color is purple")
# name = input()
# if name == "Ar_ya Stark".lower():
#     print("va_lar Mor_ghu_lis")
# elif name == "John Snow":
#     print("Bastard")
# else:
#     print("carry on")

# color_fav = input("what is your favorite color: ")
# if color_fav == "purple":
#     print("excellent choice")
# elif color_fav == "teal":
#     print("not bad")
# elif color_fav == "sea-foam":
#     print("mediocre")
# elif color_fav == "pure darkness":
#     print("i like how you think")
# else:
#     print("YOU MONSTER")
# print(type("izu") is str)
# animal = input("what is your favorite animal : ")
# if animal:
#     print(f"hmm_mmmmmm so {animal} is your favorite animal, na wa")
# else:
#     print("Why didn't you pick an animal?")
# age = input("what is your age: ")
# number_format = int(age)
# if number_format >= 18 and number_format <= 45:
#     print("you are allowed to vote but vote for peter Obi")
# elif number_format > 10 and number_format < 18:
#     print("please you are not allowed to vote")
# elif number_format > 45:
#     print("you done old")
# else:
# #     print("you did not pic an age")
# name = ""
# print(bool(not name))
"""
so when you using the not in python, when i do not something it flips it, more like when i do something like != in javascript and typescript,
like
age = 14
if age ====> True
if not age =====> False
"""
# print({} is [])
# print({} == [])
# print([] is [])
# a = [1, 2, 3, 4]
# b = [1, 2, 3, 4]

# print(a is b)
# print(a == b)

# a = ['a', 'b', 'c', 'd']
# a = b
# print( a is b )
# x = 13
# y = 13

# print( x is y )
# a = { 'a' : "kings", 'b': 'queen'}

# b = {'a': "kings", 'b': "queen"}

# print(a == b)
# print( a is b )

# x = "kings"
# y = "kings"

# print(x is y)

# for x in range(0, 20):
#     print(x)

# print([0,...,10])
# def bubbleSort(arr):
#     # de_fence coding
#     if len(arr) <= 1:
#         return arr
#     for x in arr:
#         if arr[x] > arr[x+1]:
#             # swap
# x = 0
# for char in "hello":
#     x += 1
#     if char == "l":
#         print("i have reached the first l", x)
#         break

# for letter in "coffee":
#     print(letter * 10)

# def bubbleSort(list_arr):
#     if len(list_arr) <= 1:
#         return list_arr
#     for l in list_arr:
#         x = 0
#         for j in list_arr:
#             if j[x] > j[x + 1]:
#                 [list_arr[x], list_arr[x + 1]] = [list_arr[x + 1], list_arr[x]]

#         x += 1

# def bubbleSort(list_arr):
#     if len(list_arr) <= 1:
#         return list_arr

#     for i in range(len(list_arr)):
#         swapped = False
#         for j in range(len(list_arr) - i - 1):
#             if list_arr[j] > list_arr[j + 1]:
#                 swapped = True
#                 list_arr[j], list_arr[j + 1] = list_arr[j + 1], list_arr[j]

#         if not swapped:
#             break

#     return list_arr

# print(bubbleSort([5, 3, 8, 2]))


# print(list(range(100, 50, -2)))
x = 0

# while True:
#     print("this is while loop")
#     if x == 10:
#         print("****************** it reached ", x)
#         break

#     x += 1

# msg = input("whats the secret password ?:  ")
# while msg != "bananas":
#     print("WRONG")
#     msg = input("whats the secret password")
# print("CORRECT")

# for x in range(0, 10):
#     print(x)

# for x in ['a', 'b', 'c', 'd']:
#     print(x)

# list_arr_one = ['w', 'x', 'y', 'z']
# value_range = range(len(list_arr_one))

# print(value_range)

# print(len(list_arr_one))

# for i in range(len(list_arr_one)):
#     print(i, list_arr_one[i])

# def selectionSort(list_arr):
#     if not isinstance(list_arr, list):
#         return 'not a list'
#     if len(list_arr) <= 1 :
#         return list_arr

#     for x in range(len(list_arr) - 1):
#         minIndex = x
#         for idx in range(x + 1, len(list_arr)):
#             if list_arr[idx] > list_arr[minIndex]:
#                 minIndex = idx


#         if minIndex != x:
#             list_arr[idx], list_arr[minIndex] = list_arr[minIndex], list_arr[idx]
#     return list_arr

# print("\U0001f600")


# def run_simily_face():
#     x = 1
#     max_num = 11
#     let_run = True
#     while let_run:
#         print("\U0001f600" * x)
#         x += 1
#         if x > max_num:
#             break

# run_simily_face()
# print("this is my typing python on a script level")
# int str bool float and NoneType
# = on the left name of the object on the right
# nameValue = "Izu" -----> left is the variable-name = object
# my_items = ["fish", "egg", "meat", "oat", "milk"] my_items is the variable name bound to a list object, not the reference itself;
# python creates a list object containing 5 strings.
# python binds the name my_items to that list object;

# my_items = ["fish", "egg", "meat", "oat", "milk"]
# # other_items = my_items
# other_items = ["fish", "egg", "meat", "oat", "milk"]
# print(my_items == other_items)
# print(my_items is other_items)
# print(other_items is my_items)
a, b, _ = 1, 2, 3

# print(_)

# myList = ['Alice', 'mike', 'Bob', 'Alexander']

# myList.append('Ned')
# print(myList)
# print(myList[-3])

# print(myList[-3] == myList[2])
# myList.insert(0, 'kingsley')
# print(myList)


# print(myList)
# print(len(myList))

# # print(myList.index('kingsley'))
# print('********this is **********')
# print(myList)
# # print(myList.pop())
# my_pop_item = myList.pop()

# print(myList)

# print(my_pop_item)

# tuple_val = ('10.20.30.40', 8808)
# print(len(tuple_val))
# one_val_tuple = (8080,)

# print(len(one_val_tuple))

# tuple_look_like_string = 'this value',

# print(type(tuple_look_like_string))

# one_name = list('ashley')
# name_vales = list(('ashley', 'matt', 'micheal'))
# print(name_vales, one_name)


# print('ashley' in name_vales)

# def append_square_number(list_arr):
#     new_list = []
#     if  not isinstance(list_arr, list):
#         return "this is not a list"
#     for item in list_arr:
#         if not isinstance(item, int):
#             return "item is not a number"
#         elif isinstance(item, int):
#             new_list.append(item * 2)
#         else:
#             return "nothing to print here"
#     return new_list


# new_loop_idea = append_square_number([1, 2, 3, 4, 5, 6, 7])
# print(append_square_number([2, 4, 5, "item", 10]))

# def square_number(list_arr):
#     new_list = []
#     for item in list_arr:
#         new_list.append(item * 2)
#     return new_list

# print(square_number([2, 3, 4, 5]))

# i = 0
# while i < len(new_loop_idea):
#     print(new_loop_idea[i])
#     i += 1

# first_list = [1, 2, 3, 4]
# first_list.append(5, 6, 7, 8) #does not work
# first_list.append([5, 6, 7, 8])

# print(first_list)
# correct_list = [1, 2, 3, 4]

# correct_list.extend([5, 6, 7, 8])

# print(correct_list)
# correct_list.clear()

# print(correct_list)
# names_list = ['colt', 'blue', 'ar_ya', 'lena', 'colt', 'selena', 'pablo']
# new_reversed_names_list = names_list.reverse()
# print(names_list)

# names_list.sort()
# print(names_list)
# words = ["Coding", "Is", "Fun!"]
# new_sentence = " ".join(words)
# print(new_sentence)

# first_list = [1, 2, 3, 4, 5, 6]

# print(first_list[1::2])
# #i thought this will skip the last value, based on it not in the steps of 2, [1, 2{starting index}, _, 4{starting index}, _, 6]

# print(first_list[::2]) #[1,3,5]

# another_first_list = [1, 2, 3, 4, 5, 6]
# another_first_list[1::-1]
# # start from index of 1, end at None and step backwards in 1 steps [ 1, 2{starting index}, ], now why is 1 inclusive [2, 1]

# another_first_list[:1:-1]
# # start from index of None and end at 1, but step 1 backwards;
# # [6, 5, 4, 3]

# another_first_list[2::-1]
# start from the index 2----> remember that 2 is inclusive---> starting index, ends at None and step -1 step backwards at -1;
# [1, 2, 3, 4, 5, 6] = [6, 5, 4, 3]

# i feel im missing an important detail here

# def swap_values(arr, x, y):
#     val = arr[x]
#     arr[x] = arr[y]
#     arr[y] = val
#     return arr


# swap_list = [1, 2, 3, 4]
# val = swap_list[2]
# print(val)
# swap_list[2] = swap_list[1]
# swap_list[1] = val
# print(swap_list)

# print(swap_values([1, 2, 3, 4], 1, 2))

# double_list = [ x*2 for x in another_first_list ]
# print(double_list)

# print(10 / 2)

# even_list = []

# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# new_color_list = [color.upper() for color in colors]
# print(new_color_list)

# eve_list = [num for num in another_first_list if num % 2 == 0]
# print(eve_list)

# names_name = ['Elie', 'Tim', "Matt"]
# first_char = [char[0] for char in names_name]
# print(first_char)
# numbers_vals = [1, 2, 3, 4, 5, 6]


# answer2 = [num for num in numbers_vals if num % 2 == 0]
# print(answer2)

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(nested_list[2][1])
# print(nested_list[-1][-2])

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# [[print(val) for val in l] for l in nested_list]

# nested_list = [[num for num in range(1, 4)] for num in range(1, 4)]
# print(nested_list)


# instructor = ['colt', True, 4, "python", False, True, 'colt']
# obj_value = {}

# def check_dict(obj):
#     new_dict = {}
#     for x in obj:
#         if x in new_dict:
#             new_dict[x] += 1
#         else:
#             new_dict[x] = 1
#     return new_dict

# print(check_dict(instructor))


# print(instructor["name"])
# print(instructor[("ned",)])
# cats = dict(name="kitty", age=0.5)
# print(cats)

# print(cats["name"])

# del instructor[15]

# print(instructor)

# artist = {
#     "first" : "Neil",
#     "last" : "Young"
# }

# full_name = artist["first"] + " " + artist["last"]

# print(full_name)

# print(f"{artist['first']} {artist['last']}")
# for x in instructor:
#     print(instructor[x])

# value_list = instructor.values()
# # print(type(value_list))

# # print(value_list)
# # for x in value_list:
# #     print(x)

# instructor_keys = instructor.keys()
# # print(type(instructor.items()))
# # print(instructor_keys)
# instructor_items = instructor.items()

# for k,v in instructor_items:
#     print(f"this is the key {k} and this is the value {v}")


# print("name" in instructor)
# print("Colt" in value_list)

# number_list = [1, 2, 3, 4, 5, 6]
# new_number_list = number_list.copy()

# new_number_list.append(5)

# # print(new_number_list)
# # print(number_list)

# number_one = ["a", "b", "c"]
# number_two = number_one


# # number_two.append("ned")

# # print(number_one)
# new_user = {}.fromkeys(['name', ("access",), 6], "bread")

# # print(new_user)

# another_new_user = new_user.fromkeys("a", "this_value")

# # print(f"this is another new user {another_new_user}")

# from_dict = {}.fromkeys("needy", "kai")
# print(from_dict)

# instructor = {
#     "name": "Colt",
#     "own_dogs": True,
#     "num_courses": 4,
#     "favorite_languages": "Python",
#     "is_funny": False,
#     "leaner" : "ned",
#     15: 200,
#     ("ned",): "a tuple value"
# }
# value_popItem = instructor.popitem()
# print(value_popItem)
# # print(instructor)


# new_pop_item = instructor.popitem()

# print(type(new_pop_item))


# playlist = {
#     "title": "patagonia bus"
# }

# numbers = [1, 2, 3, 4, 5]
# result = [num * 2 for num in numbers if num > 2]
# # result = [6, 8, 10]
# result_alt = [num * 2 for num in numbers if num % 2 == 0]
# result_alt = [4, 8]

# conditional_expression
# [value_if_true if condition else value_if_false for num in numbers]
# numbers_value = [1, 2, 3, 4]
# results = [num * 2 if num % 2 == 0 else num * 3 for num in numbers_value]

# print(numbers_value)
# numbers = range(1, 21)
# result = [
#     num
#     for num in numbers
#     if num % 2 == 0
#     if num > 10
# ]

# number_value = [1, 2, 3, 4, 5, 6]

# results = ["Even" if num % 2 == 0 else "divisible by 3" if num % 3 == 0 else "Others" for num in number_value]

# print(results)

# number_value = range(1, 20)
# results = ["Even" if num % 2 == 0 elif "Divisiable by 3"  num % 3 == 0 else "Others"  for num in number_value]
# when it comes to list comprehension, the elif condition is not used, the only thing used in this is the if and else, nothing more, nothing less;

# number_value = range(1, 30)
# results = [
#     "Even" if num % 2 == 0 else "Divisible by 3" if num % 3 == 0 else "Others" for num in number_value
# ]
# print(results)

# numbers_range = range(1, 11)
# results = ["Even" if num % 2 == 0 else "Odd" for num in numbers_range if num > 5]
# print(results)

# print(type(like_tuple[0]))
# print(type(len(like_tuple)[0]))

# total_length = 0
# for songs in playlist['songs']:
#     total_length += songs['duration']

# print(total_length)

# {____:____ for loop}

# numbers_dict = dict(first=1, second=2, third=3)

# squared_numbers = {key:value * 2 for key, value in numbers_dict.items()}

# experimental_dict = dict(name="john", state="plateau_state", fav="music", attitude="spicy" )

# # print(squared_numbers)
# # experimental_dict_look_like_list = experimental_dict.items()
# # for key, value in experimental_dict_look_like_list:
# #     print(f"this is the {key} and also the {value}")
# range_value = range(1, 11)

# result_range_value = {num: num * 2 for num in range_value}

# # print(result_range_value)
# str_one = "ABC"
# string_array = ["a", "b", "d", "a", "c", "d", "i", "g", "b"]

# # char_count = {for char in string_array }

# str_one = "ABC"
# str_two = "123"
# combo = {str_one[i]:str_two[i] for i in range(0, len(str_one))}
# print(combo)
# num_list = [1, 2, 3, 4]
# dict_list_evenOrOdd = {num:("even" if num % 2 == 0 else "Odd") for num in num_list}

# print(dict_list_evenOrOdd)

# frequency_count = {char:(string_array.count(char) if char else 0) for char in string_array }
# print(frequency_count)
# tuple_numbers = (1, 2, 3, 4, 5)
# tuple_numbers[0] = "a" tuple are immutable in python
# print(tuple_numbers[0])
# is_tuple = "my_name",
# print(type(is_tuple))

# print(list(['chinedu', True, False]))
# for tup in tuple_numbers:
#     print(tup)

# months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

# locations = {
#     (35.6895, 39.69167): "Tokyo Office",
#     (40.7128, 74.0060): "New York Office",
#     (37.7749, 122.4149): "San Fran_ciso office"
# }
# this is a bad example, because u are suppose to use the office location to locate the lat , long
# print(locations[(35.6895, 39.69167)])
# playlist = {
#     'title' : 'patagonia bus',
#     'author' : 'colt steel',
#     'songs' : [
#         {'title': 'song1', 'artist':['blue'], 'duration': 2.5},
#         {'title': 'song1', 'artist':['blue'], 'duration': 5.25},
#         {'title': 'song1', 'artist':['blue'], 'duration': 2.0},
#     ]
# }

# like_tuple = playlist.items()
# list_like_tuple = list(like_tuple)
# print(list_like_tuple)
# print(type(list_like_tuple[0]))


# x = y = [7, 8, 9]
# # x = [13, 8, 9]

# # print(y)

# x.append(10)

# print(y)

# y = 10 + "my_name"
# print(y)

# tuples ---> count, index

# list_arr = [1 ,2 ,3 ,4, 5]
# print(list_arr.index(6)) ValueError

# tuple_idx = (1, 2, 3, 4, 5)
# print(tuple_idx(6)) value Error also
# tuple also uses Slices,
# set does not support indexing,
# keyError
# unique_set = set({1, 2, 2, 3, 4, 5, 5, 6, 6, 6, 7})
# print(6 in unique_set)

# unique_set.add(8)
# unique_set.add(8)

# unique_set.remove(6)
# print(unique_set)
# #using .discard avoids keyError
# unique_set.discard(6)
# print(unique_set)
# #copy, clear
# unique_set_copy = unique_set.copy()

# print(unique_set_copy == unique_set)
# print(unique_set_copy is unique_set)
# math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
# biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# union_students = math_students | biology_students
# print(union_students)
# intersection_students = math_students & biology_students
# print(intersection_students)
# dict_obj = {'a': 2, 'b': 3, 'c': 4}
# dict_comprehension = {key:value * 2 for key, value in dict_obj.items()}

# print(dict_comprehension)

# why is set not in an ordered form;
# num_set = {2, 3, 4, 5, 6, 7, 8}
# set_comprehension = {x**2 for x in num_set}
# print(set_comprehension)

# def are_all_vowels_in_string(string):
#     return len({char for char in string if char in 'aeiou'}) == 5
# print(are_all_vowels_in_string('abcdeifgiou'))

# tuples are ordered collections of elements, they are immutable
# tuples are faster than lists and useful for protecting data
# sets are unordered collections of unique values


# DRY --> Don't repeat yourself
# WET ---> write everything twice
# RTFM ---> Read the Fucking Manuel

# def display_header():
#     user_name = input('What is your name: ')
#     # print(user_name)
#     return f"my name as a user is {user_name}"

# print(display_header())

# def return_value(arg):
#     return arg

# def first():
#     print("First started")
#     second()
#     print("First ended")

# def second():
#     print("Second started")
#     third()
#     print("Second ended")

# def third():
#     print("Third started")
#     print("Third ended")

# first()

# x = 100

# def change_number():
#     global x
#     x = 500

# change_number()

# y = x + 100
# print(x)
# print(y)
# global x tells

# x = 100

# def outer():
#     x = 20

#     def inner():
#         nonlocal x
#         x = 50

#     inner()
#     print("outer: ", x)
# outer()
# print("global: ", x)


# def product(num1, num2):
#     return num1 * num2

# def last_element(list_arr):
#     return list_arr.pop()

# def last_element_(list_arr):
#     length = len(list_arr)
#     return list_arr[length - 1]

# def last_element__(list_arr):
#     return list_arr[-1]

# def single_letter_counts(string,letter):
#     count = 0
#     for char in string:
#         if char == letter:
#             count += 1
#     return count

# # print(single_letter_counts("hello", "a"))

# def multiple_letter_count(string):
#     return {key: string.count(key) for key in string}

# print(multiple_letter_count("abracatabra"))
# #so using count bring the function to be O(n^2)

# def multiple_letter_count_(string):
#     new_obj = {}
#     for char in string:
#         if char in new_obj:
#             new_obj[char] += 1
#         else:
#             new_obj[char] = 1
#     return new_obj

# print(multiple_letter_count_("abracatabra"))


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# first, *middle, last = numbers

# print(first)
# print(middle)
# print(last)

# numbers_arr = [10, 20, 30]

# print(*numbers_arr)

# first = [10, 20, 30]

# second = [40, 50, 60]

# combined = [*first, *second]

# print(combined)

# def add_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total


# def display(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# display(name="kingsley", age=25, location="plateau_state")

# def display_info(*args, **kwargs):
#     print("Positional :", args)
#     print("Keyword :", kwargs)

# display_info("kingsley", 25, location="plateau_state", country="Nigeria")

# def fav_colors(**kwargs):
#     print(kwargs)

# fav_colors(name="kingsley", color="purple", food="rice")

# def display_info(a, b, *args, instructor="colt", **kwargs):
#     return [a, b, args, instructor, kwargs]
# print(display_info(1, 2, 3, last_name="steel", job="instructor"))
# unpacking = [1, 2, 3, 4, 5]
# print(*unpacking)


# obj_list = {
#     "name": "kingsley",
#     "age": 25,
#     "location": "plateau_state"
# }
# def display_obj(name, age, location):
#     return f"my name is {name}, my age is {age} and i live in {location}"

# print(display_obj(**obj_list))

# def add_and_multiply_numbers(a, b, c, d):
#     return (a + b) * (c + d)

# data = dict(a=1, b=2, c=3, d=4)
# print(add_and_multiply_numbers(**data))

# def square(num): return num * num

# print(square(5))

# square_two = lambda num: num * num

# add = lambda x, y: x + y

# print(square_two.__name__)
# print(add.__name__)
# print(square.__name__)

# nums = [2, 3, 4, 5, 6]

# doubles = map(lambda num: num * 2, nums)

# print(list(doubles))
# print(list(doubles)) # this will return an empty list because the map object is exhausted after the first conversion to a list

# people = ["Elie", "Tim", "Matt"]

# capitalize_first_name = map(lambda name: name.capitalize(), people)
# print(capitalize_first_name)
# print(list(capitalize_first_name))


# def decrement_list(list_arr):
#     return list(map(lambda num: num - 1, list_arr))


# print(decrement_list([1, 2, 3, 4, 5]))
""" FILTER this works in the same way with map, but if filters based on conditions and returns a filter objects"""

# arr = [1, 2, 3, 4, 5, 6]

# even = list(filter(lambda num: num % 2 == 0, arr))
# # print(even)
# peoples_names = ["austin", "penny", "anthony", "angel", "billy"]
# a_names = list(filter(lambda a: a.startswith("a"), peoples_names))
# # print(a_names)

# users = [
#     {"username": "samuel", "tweets": ["I love cake", "it depends on the cake"]},
#     {
#         "username": "Katie",
#         "tweets": ["I love cats, if you know hoe to use the safe word"],
#     },
#     {"username": "jeff", "tweets": []},
#     {"username": "bobs123", "tweets": []},
#     {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
#     {"username": "guitar_gal", "tweets": ["dogs are the best"]},
# ]

# in_active_users = [user for user in users if len(user['tweets']) == 0]
# print(in_active_users)
# empty_tweets = list(filter(lambda tweet: len(tweet['tweets']) == 0, users))
# print(empty_tweets)
# numbers = [1, 2, 3, 4, 5, 6]
# result = list(
#     map(
#         lambda num: num * 10,
#         filter(lambda num: num % 2 == 0, numbers)
#     )
# )
# transformation happens from the inner most functions,

# names_list = ['Lassie', 'Colt', 'Rusty']

# name_ = list(map(lambda name: f"Your instructor is {name}", filter(lambda value: len(value) < 5, names_list)))
# print(name_[0])

# An if after the for filters elements.
# An if ... else before the for decides what value to put into the resulting list.
# in_active_users = [user for user in users if len(user["tweets"]) == 0]
# # print(in_active_users)
# # 2. Multiple if conditions on the right
# # You can have more than one filtering condition.

# active_users = [
#     user
#     for user in users
#     if len(user["tweets"]) > 0
#     if user["username"].startswith("K")
# ]
""" when ypu have 2 if statement on the right, thats after the for loop, its just like a nested If statements """

# print(active_users)
# statues = [
#     "Active" if len(user["tweets"]) > 0 else "Inactive" for user in users
# ]
# # *VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE
# # print(statues)

# statues_check = [
#     "active" if len(user['tweets']) > 0 else "inactive" for user in users if user['username'].startswith(("b", "d"))
# ]
# # print(statues_check)

# users = [
#     {"name": "John", "tweets": ["Hello", "Python"]},
#     {"name": "Mary", "tweets": []},
#     {"name": "David", "tweets": ["Learning Python"]},
#     {"name": "Sarah", "tweets": []}
# ]

# results = [
#     user["name"] if len(user["tweets"]) > 0 else "No Tweets"
#     for user in users
#     if user['name'] != "David"
# ]

# print(results)


# def remove_negatives(list_arr):
#     return list(filter(lambda num: num >= 0, list_arr))


# # print(remove_negatives([-7, 0, -1, 1, -5, 5, 8, 4,]))

# all(["a", "e", "i", "o", "u"])

# print(any())
# any takes one argument but the argument must be an iterable

# Use a generator expression when you only need to process values one at a time. Use a list when you need to store the results and reuse them.
# Approach B — Generator expression O(1) space complexity, O(n) time complexity
# results_two = list((num * 2 for num in range(1, 6)))
# print(results_two)
# import sys
# sys.getsizeof


# def is_all_strings(list_arr):
#     return all(type(string) is str for string in list_arr)


# print(is_all_strings(["a", "b", "c", "d"]))
# print(is_all_strings(["a", "b", "c", 1]))
"""
sort() modifies the original list directly (in-place).

sorted() returns a new sorted list without modifying the original iterable.
"""
# this sort() does not return anything, but modifies the original list in place.
# numbers_to_sort = [5, 2, 9, 1, 5, 6]
# sorted_results = numbers_to_sort.sort()
# print(sorted_results)
# print(numbers_to_sort)

# numbers_to_sort_two = [5, 2, 9, 1, 5, 6]
# sorted_results_two = sorted(numbers_to_sort_two)
# print(sorted_results_two)
# ? this gives an error 
# tuples_nums = (4, 1, 6, 10, 5, 8)
# tuples_nums.sort()
# print(
#     tuples_nums
# )  # this will throw an error because tuples are immutable and do not have a sort() method

# sorted(iterable, reverse=False)
# when sorted collects a  tuple and it sorts it, it returns a list

# users = [
#     {"username": "samuel", "tweets": ["I love cake", "it depends on the cake"]},
#     {
#         "username": "Katie",
#         "tweets": ["I love cats, if you know hoe to use the safe word"],
#     },
#     {"username": "jeff", "tweets": []},
#     {"username": "bobs123", "tweets": []},
#     {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
#     {"username": "guitar_gal", "tweets": ["dogs are the best"]},
# ]


# new_user = sorted(users, reverse=True, key=lambda user: user['username'])
# print(new_user)


# add = lambda x, y: x + y

# print(add(5, 10))
# user_with_tweets = sorted(users, reverse=False, key=lambda user: len(user['tweets']))
# print(user_with_tweets)

# print()

"""
    [{'username': 'samuel', 'tweets': ['I love cake', 'it depends on the cake']}, {'username': 'Katie', 'tweets': ['I love cats, if you know hoe to use the safe word']}, {'username': 'doggo_luvr', 'tweets': ['dogs are the best']}, {'username': 'guitar_gal', 'tweets': ['dogs are the best']}, {'username': 'jeff', 'tweets': []}, {'username': 'bobs123', 'tweets': []}]
"""

# without_tweets = list(filter(lambda user: len(user['tweets']) == 0, users))

# print(without_tweets)
# songs = [
#     {"title": "happy birthday", "play_count": 1},
#     {"title": "Survive", "play_count": 6},
#     {"title": "YMCA", "play_count": 99},
#     {"title": "Toxic", "play_count": 31}
# ]

# most_played = sorted(songs, reverse=True ,key=lambda song: song['play_count'])

# # print(most_played)

# number_list = [2, 3, 4,10, 34, 57, 198]

# max_number = max(number_list)
# print(max_number)

# print(max(1, 2, 5, 90, 1345, 9))

# names_list = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']
# short_name = min(names_list, key=lambda name: len(name))
# print(short_name)

# long_name =  max(names_list, key=lambda name: len(name))
# print(long_name)

# nums = [1, 2, 3, 5, 6]

# nums.reverse()
# print(nums)

# nums_list = [1, 2, 3, 4, 5, 6, 7]
# new_reversed_num_list = list(reversed(nums_list))
# print('*************',new_reversed_num_list)

# print("hello".__len__())

# class SpecialList:
#     def __init__(self, data):
#         self.__data = data

#     def __len__(self):
#         return 50
# l_1 = SpecialList([1, 2, 3, 5,100])
# print(len(l_1))

# value = sum((1, 2, 4, 5), 10)
# print(value)
# print(0.1 + 0.3)
# value_sum = 0.1 + 0.4
# print(value_sum)
# print(0.01 + 0.02)

# def max_magnitude(list_nums):
#     new_value = 0
#     for num in list_nums:
#         if not isinstance(num, int):
#             return False
#         else:
#             abs(num) > new_value # logical error here, i knew something was up
            
#             new_value = abs(num)
#     return new_value

# def max_magnitude_comprehension(list_arr):
#     return max([abs(x) for x in list_arr if type(x) == int])

# def sum_even_values(*args):
#     list_arr = []
#     for x in args:
#         if x % 2 == 0:
#             list_arr.append(x)
#     return sum(list_arr)

# def sum_even_values_method_two(*args):
#     total = 0
#     for x in args:
#         if x % 2 == 0:
#             total += x
#     return total

# print(sum_even_values(1, 2, 3, 4, 5, 6, 7, 8,))

# def sum_floats(*args):
#     total = 0
#     for x in args:
#         if type(x) is float:
#             total += x
#     return total
# def sum_floats_(*args:float) -> float:
#     total = 0
#     for x in args:
#             if type(x) is float:
#                 total += x
#     return total

# names = ["John", "Mary", "David"]
# ages = [25, 30]

# results = zip(names, ages)
# print(list(results))
# results_ages = zip(ages, names)
# print(list(results_ages))
# five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# print(zip(*five_by_two))

midterms = [80, 91, 78]
finals = [98, 89, 53]
# students = ['dan', 'ang','kate']

# results_zip = list(zip(midterms, finals, students))

# print(results_zip)


# scores = list(map(lambda pair: max(pair), zip(midterms, finals)))

# print(scores)
# print('ne_du' + 10)
# print(len(12))
# def colorize(text, color) -> str:
#     if type(text) is not str:
#         raise TypeError("text must be a string")
#     print(f"this is the text {text} and this is the color {color}")

# colorize(123, "red")

# x = 10

# def find_x():
#     x = 40
#     del x
#     # print(x)

# print(find_x())
# print(x)
# foo = 10
# def fun():
#     bar = 20
#     print(bar)
#     print(foo)

foo = 1
# def fun():
#     bar = 2
#     print(globals().keys())
#     print(locals().keys())

# fun()
# n = 10

# result = "Greater than 5" if n > 5 else "Less than or equal to 5"
# print(result)
# score = 75
# grade = (
#     "A" if score >= 90
#     else ("B" if score >= 70 else "C")
# )

# print(grade)

# a = 'short'
# d = 'short'
# b = 5
# c = 5
# print(a is d)

# i = 0
# while i < 7:
#     print(i)
#     if i == 4:
#         print('breaking from this loop')
#         break
#     i += 1

# def break_loop():
#     for i in range(1, 5):
#         if i == 2:
#             return i
#         print(i)
#     return 5

# break_loop()

dic_obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(list(dic_obj.keys()))
# dict_keys(['a', 'b', 'c', 'd']) <--- this is iterable