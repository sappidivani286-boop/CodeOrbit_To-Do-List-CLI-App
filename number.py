
import random

print("===== NUMBER GUESSING GAME =====")

while True:
    number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number from 1 to 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low!")

        elif guess > number:
            print("Too high!")

        else:
            print("It is a correct guess!")
            print("Number of attempts =", attempts)
            break

    choice = input("Do you want to play again? (yes/no): ")

    if choice.lower() != "yes":
        print("Thanks for playing!")
        break