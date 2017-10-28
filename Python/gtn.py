from random import randint

# Asks the user for his or her name
name = input('Hello! What is your name? ')

# Greets the user with a banner
banner = ("*" * len(name))
print("{}Let's get started with the guessing game, {}!{}".format(banner, name, banner))

# Computer chooses a random number
comp_random_number = randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

# Function to check guessed number against computer number
def number_check(user_number):
    if user_number > comp_random_number:
        print('Too high!')
    elif user_number < comp_random_number:
        print('Too low!')
    else:
        print('Awesome job! You guessed my number correctly in {} guesses.'.format(count))

# Asks user to guess the number until correct and keep score
count = 1
while True:
    user_number = int(input('Please guess the number: '))
    user_guess = number_check(user_number)
    count +=1
    if user_number == comp_random_number:
        break
