def first_pick():
    while True:

        first_num = int(input("Type the first Number: "))
        the_symbol = input("Please type the sign '+': ")

        if the_symbol != '+':
            print('Wrong symbol! Please type +')
            continue
        else:
            second_num = int(input("Type the second Number: "))
            the_res = first_num + second_num
            print(f"{first_num} {the_symbol} {second_num} = {the_res}")
            with open('result.txt', 'a') as file:
                file.write(str(f"\n {first_num} {the_symbol} {second_num} = {the_res} "))


def second_pick():
    while True:

        first_num = int(input("Type the first Number: "))
        the_symbol = input("Please type the sign '-' ")

        if the_symbol != '-':
            print('Wrong symbol! Please type -')
            continue
        else:
            second_num = int(input("Type the second Number: "))
            the_res = first_num - second_num
            print(f"{first_num} {the_symbol} {second_num} = {the_res}")
            with open('result.txt', 'a') as file:
                file.write(str(f"\n {first_num} {the_symbol} {second_num} = {the_res} "))
