import random
print("age guesser!")
print("answer with yes or no")

prev_guessses = []
guessed = False
while(guessed == False):
    guess = random.randint(15,30)
    if guess in prev_guessses:
        continue

    user_res = input(f'are you {guess} years old? ')
    if user_res == 'yes':
        guessed = True
        print("im built different and im right wooo")
    else:
        print('rats n such')
        prev_guessses.append(guess)