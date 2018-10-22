# This program says hello and asks for my name.

print('Hello wolrd!')
print ('What is your name?') # ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The Length of your name is:')
print(len(myName))
print('What is your age?')   # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) +1) + ' in a year.')
print('호구야 실수값좀 입력해라: ')
myround = float(input())
if str(type(myround)) == "<class 'float'>" :
    print('니가 입력한 값을 반올림해주마 :' + str(round(myround)))
else:
    print('실수값 모르냐')
