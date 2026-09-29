'''Problem 2: Find the number of digits in the given number'''
num = abs(int(input('Enter a number: ')))
digits = 1
while(num > 10):
    num = num // 10
    digits = digits + 1
print(digits)
