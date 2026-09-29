'''Problem 3: Write a Python code using functions which checks whether the input coordinates form a triangle or not'''
'''Approach 2: Using slope of lines connecting two points'''
import math

def slope(xi, yi, xj, yj):
    if(xi == xj):
        return(math.inf)
    else:
        return((yj - yi) / (xj - xi))
    
x1 = float(input('Enter x coorinate of 1st point: '))
y1 = float(input('Enter y coorinate of 1st point: '))
x2 = float(input('\nEnter x coorinate of 2nd point: '))
y2 = float(input('Enter y coorinate of 2nd point: '))
x3 = float(input('\nEnter x coorinate of 3rd point: '))
y3 = float(input('Enter y coorinate of 3rd point: '))
s1 = slope(x1, y1, x2, y2)
print(f'\nSlope of the line connecting points ({x1}, {y1}) and ({x2}, {y2}) = {s1}')
s2 = slope(x2, y2, x3, y3)
print(f'\nSlope of the line connecting points ({x2}, {y2}) and ({x3}, {y3}) = {s2}')
if(s1 != s2):
    print('\nTriangle')
else:
    print('\nNot a triangle')
