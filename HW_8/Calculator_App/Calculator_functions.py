def main_process():
    while True:
        print("The Calculator!")
        first_num = int(input("Type the first Number: "))
        the_symbol = input("What operation you wish to make (ex: '+','-','*' or '/'): ")
        second_num = int(input("Type the second Number: "))
        if the_symbol in ('+', '-', '*', '/'):
            if the_symbol == '+':
                the_res = first_num + second_num
                print(f"{first_num} {the_symbol} {second_num} = {the_res}")
                with open('result.txt', 'a') as file:
                    file.write(str(f"\n {first_num} {the_symbol} {second_num} = {the_res} "))
            elif the_symbol == '-':
                the_res = first_num - second_num
                print(f"{first_num} {the_symbol} {second_num} = {the_res}")
                with open('result.txt', 'a') as file:
                    file.write(str(f"\n {first_num} {the_symbol} {second_num} = {the_res} "))
            elif the_symbol == '*':
                the_res = first_num * second_num
                print(f"{first_num} {the_symbol} {second_num} = {the_res}")
                with open('result.txt', 'a') as file:
                    file.write(str(f"\n {first_num} {the_symbol} {second_num} = {the_res} "))
            elif the_symbol == '/':
                if second_num != 0:
                    the_res = first_num / second_num
                    print(f"{first_num} {the_symbol} {second_num} = {the_res}")
                    with open('result.txt', 'a') as file:
                        file.write(str(f"\n {first_num} {the_symbol} {second_num} = {the_res} "))
                else:
                    print("You can't divide by zero ")
        else:
            print('Please type a valid symbol')