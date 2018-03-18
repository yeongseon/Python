# Python function
#
def greet(name):
    return "Hello {}".format(name)

greet_someone = greet
greet_someone("Yeongseon")
print(greet_someone("Yeongseon"))

#
def greeting(name):
    def greet_message():
        return "Hello"
    return "{} {}".format(greet_message(), name)
print(greeting("Yeongseon"));

#
def change_name_greet(func):
    name = "Youngsun"
    return func(name)
print(change_name_greet(greet))

#
def uppercase(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

new_greet = uppercase(greet)
print(new_greet("yeongseon"))
