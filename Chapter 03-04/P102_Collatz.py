import sys
def collatz(number):
    while True:
        if number == 1:
            break
        elif number % 2 == 0:
            number = int(number/2)
            print('짝수 ' + str(number))
            collatz(number)
        elif number % 2 != 0 :
            number = int(3 * number +1)
            print('홀수 ' + str(number))
            collatz(number)

print('Enter number : ')

try:
    num = int(input())
except ValueError:
    print('숫자로 입력해라 ㅂㅂ2')
    sys.exit()

collatz(num)
