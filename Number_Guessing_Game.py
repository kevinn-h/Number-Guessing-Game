""" condition = False
while condition:
    print("verity") """

minimum_number = 1
maximum_number = 11

import random

n = random.randint(minimum_number, maximum_number)
guess = 0
while True:
    z = int(input("Try to guess my number! Enter 'exit' to quit: "))
    if z == "exit":
        break
    elif z > n:
        print("lower")
        guess = guess+1
    elif z < n:
        print("greater")
        guess = guess+1
    elif z == n:
        print("correct")
        print(f" you got it correct after{guess} guesses!")
        break

