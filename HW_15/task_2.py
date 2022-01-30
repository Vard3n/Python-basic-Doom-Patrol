# Solve the quadratic equation 6x**2 + 11x - 35 = 0 and 5x² - 2x - 9 = 0.
import math
import threading


def the_first_one(a, b, c):
    dis = (b ** 2) - (4 * a * c)

    if (dis > 0):
        root1 = (-b - math.sqrt(dis)) / (2 * a)
        root2 = (-b + math.sqrt(dis)) / (2 * a)
        print(f'The solution are {root1} and {root2}')
    elif (dis == 0):
        root1 = root2 = -b / (2 * a)
        print(f'Two equal and real roots are {root1} and {root2}')
    elif (dis < 0):
        root1 = root2 = -b / (2 * a)
        imaginary = math.sqrt(-dis) / (2 * a)
        print(f'Two distinct complex roots are {root1},{imaginary} and {root2},{imaginary}')


thread1 = threading.Thread(target=the_first_one(6, 11, -35))
thread2 = threading.Thread(target=the_first_one(5, -2, -9))

thread1.start()
thread2.start()
