# 1. double_result

def double_result(func):
    def inner(a, b):
        return func(a, b) * 2

    return inner


def add(a, b):
    return a + b


@double_result
def add(a, b):
    return a + b


print(add(5, 5))


# 2. only_odd_parameters

def only_odd_parametrs(func):
    def inner(*args):
        result = func(*args)
        for x in args:
            if x % 2 == 0:
                print("Please use only odd numbers!")
                break
            else:
                return result

    return inner


@only_odd_parametrs
def add(a, b):
    return a + b


print(add(5, 5))
print(add(4, 4))


@only_odd_parametrs
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(multiply(2, 3, 4, 5, 6))


# 3. logger
def logger(func):
    def inner(*args):
        print(f"You called the func{args}")
        result = func(*args)
        print(f"it returned {result}")
        return result

    return inner


@logger
def func(*args):
    return 3 + len(args)


func(4, 4, 4)


# 4. type_check

def type_check(correct_type):
    def check(previous_function):
        def new_function(arg):
            if (isinstance(arg, correct_type)):
                return previous_function(arg)
            else:
                print("Wrong Type")

        return new_function

    return check


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter("Hello World"))
first_letter(['Not', 'A', 'String'])
