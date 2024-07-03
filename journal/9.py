# A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years unless they are also divisible by 400.
#WAP that asks user for a year and print whether it is a leap year or not.

year = int(input("Enter the year:  "))

if year%4 == 0 or year%400 == 0 and year%100 != 0:
    print(f"{year} is a leap year")
else:
    print(f'{year} is not a leap year')

