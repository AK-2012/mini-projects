# Guess the number
import math
import random


def main():
    print("This is Guess the Number. ")
    while True:
        lower_limit = intput("Enter the lower limit for the number range. ")
        upper_limit = intput("Enter the upper limit for the number range. ")
        while upper_limit <= lower_limit:
            print("Upper limit must be greater than lower limit.")
            upper_limit = intput("Enter the upper limit for the number range. ")
        tries = intput("How many tries would you like? ", 1)
        number = get_number(lower_limit, upper_limit)
        print(guessing(number, tries, lower_limit, upper_limit))
        again = input("Would you like to play again? ").strip().lower()
        while again not in ["y", "yes", "n", "no"]:
            again = input("Would you like to play again? ").strip().lower()
        if again in ["n", "no"]:
            break
        print("Continuing!")
    print("Thanks for playing!")


def get_number(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)


def guessing(number, tries, lower_limit, upper_limit):
    """Execution of game with user input and returns a message
    based on whether they got the number right"""
    for i in range(1, tries + 1):
        guess = intput("Enter your guess: ", lower_limit, upper_limit)
        if guess < number:
            print("The number is higher.")
        elif guess > number:
            print("The number is lower.")
        else:
            return f"You guessed it! The number was {number}. Total tries: {i}"
        print(f"Tries left: {tries-i}")
    return f"Aw, you didn't guess it. The number was {number}"


def intput(prompt, lower_bound=-math.inf, upper_bound=math.inf):
    # Prompts user to enter a valid number, boundary inclusive, and returns it
    while True:
        try:
            num = int(input(prompt))
            if not lower_bound <= num <= upper_bound:
                raise ValueError
            return num
        except ValueError:
            print("Enter a valid number.")
            continue


if __name__ == "__main__":
    main()
