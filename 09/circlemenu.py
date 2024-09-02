#WAP to display a menu for calculating area of a circle or perimeter of a circle
import math

radius = int(input("Enter the radius: "))

print('1. Area of the circle')
print('2. Perimeter of the circle: ')

choice = int(input('Enter the choice: '))

if choice == 1:
    area = (math.pi) * math.pow(radius,2)
    print(area)
elif choice == 2:
    p = 2 * (math.pi) * radius
    print(p)

