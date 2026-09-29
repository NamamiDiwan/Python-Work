'''Problem 4: Convert the given flowchart into a Python code'''
print('Travel from City A to City B')
Time = int(input('Enter time: '))
Longer = int(input('Define longer: '))
if(Time >= Longer):
    Price = int(input('Enter Price: '))
    Higher = int(input('Define higher: '))
    if(Price >= Higher):
        print('Train')
    else:
        print('Coach')
else:
    Price = int(input('Enter Price: '))
    Higher = int(input('Define higher: '))
    if(Price >= Higher):
        print('Daytime flight')
    else:
        print('Red eye flight')
print('Arrive City B')
