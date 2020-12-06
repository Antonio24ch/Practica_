# Create a variable containing an integer between 1 and 10 inclusive. Ask the user to guess the number. 
# If they guess too high or too low, tell them they have not won. Tell them they win if they guess the correct number.

secret_number = 5
guess = input('Guess the number between 1-10: ')
if guess.isdigit():
    guess = int(guess)
    if guess == secret_number:
        print('You guessed the correct number! you win!')
    elif guess > secret_number and guess <= 10:
        print('You guessed too high. Sorry you lose!')
    elif guess < secret_number and guess >= 1:
        print('You guessed too low. Sorry you lose!')
    else: 
        print('Out of range')
else:
    print('That\'s not even an integer! What are you playing at?')