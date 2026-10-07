condition = False
while condition:
    print("verity")

minimum_number = 1
maximum_number = 10

import random

n = random.randint(minimum_number, maximum_number)

while True:
    z = input("Try to guess my number! Enter 'exit' to quit: ")
    if z.lower() == "exit":
        break
    try:
        guess = int(z)
    except ValueError:
        print("Please enter a valid number or 'exit'.")
        continue

    if guess > n:
        print("greater")
    elif guess < n:
        print("less")
    else:
        print("You guessed it!")
        break