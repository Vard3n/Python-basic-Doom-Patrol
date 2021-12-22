def first_pick():
    a = int(input("First Number: "))
    b = input("The sign: ")
    c = int(input("Second Number: "))
    d = a + c

    if b != '+':
        print('Wrong symbol!')

    print(f"{a} {b} {c} = {d}")
    with open('result.txt', 'a') as file:
        file.write(str(f"\n {a} {b} {c} = {d} "))


def second_pick():
    a = int(input("First Number: "))
    b = input("The sign: ")
    c = int(input("Second Number: "))
    d = a - c

    if b != '-':
        print('Wrong symbol!')

    print(f"{a} {b} {c} = {d}")
    with open('result.txt', 'a') as file:
        file.write(str(f"\n {a} {b} {c} = {d} "))
