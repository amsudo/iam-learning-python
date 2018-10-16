__author__ = 'charles'

# Secret number
secret = 5

# Read input and store in variable name
print("Please guess a number between 1 and 10: ")
guess = int(input("> "))

if guess >= 1 and guess <= 10:
    if guess == secret:
        print("Wow, you got it on first time.")
        print("Yes the secret number is {}".format(secret))
    elif guess < secret:
            print("Please guess higher!")
            guess = int(input("> "))
            if guess == 5:
                print("Well done, you guessed correctly.");
            else:
                print("Sorry, you have not guessed correctly");
    else:
            print("Please guess lower!")
            guess = int(input("> "))
            if guess == secret:
                print("Well done, you guessed correctly.");
            else:
                print("Sorry, you have not guessed correctly");
else:
    print("Sorry, your guess is not between 1 to 10.")


# Comparison / Relational operator
# ==, !=, <>, >, <, >= and <=

# if, elif and else

