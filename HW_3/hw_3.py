#1 Define the id
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print('\n', id(int_a),'\n', id(str_b),'\n', id(set_c),'\n', id(lst_d),'\n', id(dict_e))

#2 Append 4 and 5
print(lst_d)
lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(id(lst_d))

#3 Define the type
print('\n', type(int_a), '\n', type(str_b), '\n', type(set_c), '\n', type(lst_d), '\n', type(dict_e))

#4
print('\n', isinstance(int_a, int),'\n',isinstance(str_b, str), '\n',isinstance(set_c, set), '\n',isinstance(lst_d, list), '\n',isinstance(dict_e, dict))

#5
print("Anna has {} apples and {} peaches.".format(6,4))

#6
print("Anna has {1} apples and {0} peaches.".format(6,4))

#7
print("Anna has {ap} apples and {pc} peaches.".format(ap=6,pc=4))

#8
print("Anna has {0:5} apples and {1:3} peaches.".format(6,"four"))

#9
apl= 6
pch = 4
print(f"Anna has {apl} apples and {pch} peaches.")

#10
apl= 6
pch = 4
print("Anna has %s apples and %s peaches." % (apl, pch))

#11
apl= 6
pch = 4
fruits = {"apple": apl, "pea": pch}
print("Anna has %(apple)s apples and %(pea)s peaches." % fruits)

#12
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num**2)
    else:
        lst.append(num**4)
print(lst)

list_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comprehension)

#13
list_comprehension2 = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension2)

lst2 = []

for num in range(10):
    if num % 2 == 0:
        lst2.append(num//2)
    else:
        lst2.append(num*10)
print(lst2)

#14
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

dict_comprehension = {num:num**2 for num in range (1,11) if num %2 == 1 }
print(dict_comprehension)

#15
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

dict_comp = {num: num **2 if num % 2 == 1 else num // 0.5 for num in range(1,11) }
print(dict_comp)

#16
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)

d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
print(d)

#17
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)

d = {}
for x in range(10):
    if x**3 % 4 == 0:
        d[x] = x**3
    else:
        d[x] = x
print(d)

#18
def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(10,22))

lmb = lambda x,y: x if x < y else y
print(lmb(10,22))

#19
foo = lambda x, y, z: z if y < x and x > z else y
print(foo(10,22,44))

def foo(x,y,z):
    if y < x:
        return z
    elif x > z:
        return z
    else:
        return y
print(foo(10,22,44))

# 20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))

#21
print(sorted(lst_to_sort, reverse=True))

#22
new_lst= list(map(lambda x: x* 2, lst_to_sort))
print(new_lst)
#23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
Up_number = list(map(lambda x, y: x+y, list_A, list_B))
print(Up_number)