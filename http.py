# http hyper-text-transfer-protocol;
# URL uniform resource locator
list_arr = []
not_empty = ["a"]
# print(bool(list_arr))
# print(bool(not_empty))
# print( not list_arr)

# print("my" + " name")

# Object-Oriented-Programming
# print(help(list)) 
nums = [1, 2, 3, 4, 5]
nums.append(10)
# print(nums)

class User:
    def __init__(self, first):
        # print("this init runs automatically, just like constructor in typescript and javascript")
        # the properties is on the left side:
        self.name = first

user_one = User("izu")
# user_two = User()
# user_three = User()
# the init automatically runs before even the instance of the object runs
# print('this is user_one',user_one)
# print(user_one.name)
# print('this is user_two',user_two)
# print('this is user_three',user_three)


# print("this is python", user_one)

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.def_model = model
        self.def_year = year

car = Vehicle('V6', 'toyota', 2008)
# print(car)
class Person:
    def __init__(self, first, last, age):
        self.first_name = first
        self.surname = last
        self.age = age

        
    def full_name(self):
        return f"this is the first name : {self.first_name} and the last name is {self.surname}"
    
    def initials(self):
        return f"this is the initials {self.first_name[0].upper()}.{self.surname[0].upper()}"
    def my_likes(self, my_like):
        if my_like == "ice_cream":
            return f"this is my fav ---> {my_like} and {self.first_name} doesn't like {my_like}"
        return f"i don't like {my_like} pass it to {self.first_name}"
# p = Person('izu', 'eze', 29)
# print(p.full_name())
# print(p.initials())
# print(p.my_likes('ice_cream'))

# class BankAccount:
#     def __init__(self, owner, account_blocked, balance = 0.0,):
#         self.personal_owner = owner
#         self.my_balance = balance
#         self.account_blocked = True
        
#     def deposit_method(self, amount):
#         try:
#             transform_amount = int(amount)
#             if isinstance(transform_amount, int, float) and self.my_balance :
                
#             else:
#                 raise TypeError("this is not a number")
#         except Exception as error:
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance
    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
ned_account = BankAccount('ned', 100000.00)
print(ned_account.get_balance())


# class SocialsUser:
#     active_users = 0
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         SocialsUser.active_users += 1
#     def full_name(self):
#         return f"{self.first} {self.last}"
#     def log_active_users():
#         SocialsUser.active_users -= 1

# my_socials = SocialsUser('john', 'ken', 12)
# second_socials = SocialsUser('mary', 'ken', 34)
# print(SocialsUser.active_users)


# class Pet:
#     allowed = ['cat', 'dog', 'fish', 'rat']
#     def __init__(self, name, species):
#         if species not in Pet.allowed:
#             raise ValueError(f"You can't have a {species} pet!")
#         self.name = name
#         self.species = species

""" Question: why don't i use {self.species} in the raise Error, because since the user is going to have to input a species, why am i not using self.species and even in the if conditions why am i not doing is self.species, because i have to check the instant species from the object. why am i doing just self"""

# cat = Pet('missy', 'cat')
# dog = Pet('thanos', 'dog')

# print(id(cat.allowed) == id(dog.allowed))
# print(id(cat.allowed) is id(dog.allowed))
# print(id(cat.allowed))
# print(id(dog.allowed))
# cat.allowed = ['tiger', 'snake']
# print(id(cat.allowed))
# print(id(cat.allowed) == id(dog.allowed))

class User:
    active_user = 0
    
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_user} active users"
    @classmethod
    def from_string(cls, data_str):
        first, last, age = str.split(",")
        return cls(first, last, int(age))
    
    def __init__(self, name, person):
        self.name = name
        self.person = person
        User.active_user += 1
    def get_total_user(self):
        User.active_user += 1
        return User.active_user

user = User('ned', 'GoodPerson')
user_one = User('sky', 'Good-Dancer')
print(user.display_active_users())
print(User.display_active_users())
print(User.active_user)