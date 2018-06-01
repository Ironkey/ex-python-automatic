print('Hello wolrd!')
print ('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The Length of your name is:')
print(len(myName))
print('What is your age?')   # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')

if myName == 'Alice':
    print('Hi, Alice')
elif myAge < 12:
    print('You are not Alice, kiddo.')
elif myAge > 100:
    print('You are not Alice, Grannie.')
elif myAge > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
