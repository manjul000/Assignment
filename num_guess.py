# guessing game
import random

lower_num = int(input("PLeas enter a lower limit : "))
upper_num = int(input("Please enter an upper limit : "))

random_num = random.randint(lower_num, upper_num)

guess_num = int(input(f"Please enter your guess number ({lower_num}-{upper_num}): "))

while True:
    if guess_num > random_num:
        guess_num = int(input("Try lower\n--> "))
    elif guess_num < random_num:
        guess_num = int(input("Try higher\n--> "))
    elif guess_num == random_num:
        print("You guessed correctly.")
        break