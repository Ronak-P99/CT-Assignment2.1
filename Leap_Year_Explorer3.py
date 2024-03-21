#Problem 3

user_year = int(input("Please enter a year: "))

if user_year % 4 == 0 and user_year % 100 or user_year % 400 == 0:
    print(f"The year {user_year} is in fact a leap year!")
else:
    print(f"The year {user_year} is not a leap year!")