
# This program is a number guessing game.
# The user has a maximum of 7 attempts to guess the number.


import random


secret_number = random.randint(1, 100)
max_attempts = 7

print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.")

for attempt in range(1, max_attempts + 1):

    guess = int(input("Enter your guess: "))

    if guess < 1 or guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    if guess == secret_number:
        print("Correct!")
        print("You guessed the number in", attempt, "attempt(s).")
        break

    elif guess < secret_number:
        print("Too low.")

    else:
        print("Too high.")

else:
    print("You have used all 7 attempts.")
    print("The correct number was:", secret_number)