import random

range = 1, 10
random_number = random.randint(*range)
tries = 0
guess = ""
guess_limit = 4
out_of_guesses = False

user = input("What is your name? ")
print("What's up, " + user + ".")

print("Can you guess the number between 1 and 10?")

while guess != random_number and not(out_of_guesses):
    if tries < guess_limit:
        guess = int(input("Guess a number: "))
        tries += 1
    else:
        out_of_guesses = True

    if out_of_guesses:
        print("Out of guesses, you lose.")
    else:
        print("You win! It took you " + str(tries) + " tries to guess the right number, " + user + ".")

