'''Problem 2: Write a Python code using functions to calculate area and perimeter of circle and rectangle'''
'''Approach 1: Standard code'''
PI = 22 / 7
def circle_area(r):
    return(PI * r * r)

def circle_perimeter(r):
    return(2 * PI * r)

def rectangle_area(l, b):
    return(l * b)

def rectangle_perimeter(l, b):
    return(2 * (l + b))

r = float(input('\nEnter the radius of the circle: '))
cArea = circle_area(r)
print(f'\nArea of circle with radius {r} = {cArea} sq. units')
cPerimeter = circle_perimeter(r)
print(f'\nPerimeter of circle with radius {r} = {cPerimeter} units')
l = float(input('\nEnter the length of the rectangle: '))
b = float(input('Enter the breadth of the rectangle: '))
rArea = rectangle_area(l, b)
print(f'\nArea of rectangle with length {l} and breadth {b} = {rArea} sq. units')
rPerimeter = rectangle_perimeter(l, b)
print(f'\nPerimeter of rectangle with length {l} and breadth {b} = {rPerimeter} units')
