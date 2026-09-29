'''Problem 4: Find whether the entered number is palindrome or not'''
num = int(input('Enter a number: '))
absNum = abs(num)
rev = absNum % 10
absNum = absNum // 10
while(absNum > 0):
    r = absNum % 10
    absNum = absNum // 10
    rev = rev * 10 + r
if(num < 0):
    rev = rev - 2 * rev
if(rev == num):
    print('Palindrome')
else:
    print('Not a palindrome')
