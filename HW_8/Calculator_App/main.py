from Calculator_functions import *

while True:

    print("1. For Adding the Numbers:\n" +
          "2. For Subtraction:")

    menu_flag = int(input("What operation do you need?: "))
    if menu_flag == 1:
        first_pick()
    elif menu_flag == 2:
        second_pick()