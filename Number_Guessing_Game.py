""" condition = False
while condition:
    print("verity") """

minimum_number = 1
maximum_number = 11

import random

n = random.randint(minimum_number, maximum_number)
guess = 0
guess_history = []

while True:
    z = input("Try to guess my number! Enter exit to quit")
    guess_history.append(z)
    if z == "exit":
        break
    elif int(z) > n:
        print("lower")
        guess = guess+1
        print(guess_history)
    elif int(z) < n:
        print("greater")
        guess = guess+1
        print(guess_history)
    elif int(z) == n:
        guess = guess + 1
        print("correct")
        print(f"It took you {guess} attempts")
        print("here is your guess history", guess_history)
        break
    if guess == 100:
        print("you lose! no more attempts. The number was", n)
        print("here is your guess history", guess_history)
        break

