import random

guess = ''
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == 0:
    toss = 'heads'
elif toss == 1:
    toss = 'tails'

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
