#Problem 2.1

number_1 = int(input("Hello, please give me three numbers! Number 1: "))
number_2 = int(input("Number 2: "))
number_3 = int(input("Number 3: "))

if number_1 >= number_2 and number_1 >= number_3:
    print(f"The highest value is {number_1}!")
elif number_2 >= number_1 and number_2 >= number_3:
    print(f"The highest value is {number_2}!")
else:
    print(f"The highest value is {number_3}!")

#Problem 2.2: I used the same outline as previous problem and changed greater than to less than
    
if number_1 <= number_2 and number_1 <= number_3:
    print(f"The lowest value is {number_1}!")
elif number_2 <= number_1 and number_2 <= number_3:
    print(f"The lowest value is {number_2}!")
else:
    print(f"The lowest value is {number_3}!")

#Problem 2.3: I used the same outline as previous problem and used different comparison operators!

if number_1 == number_2 and number_1 == number_3:
    print("All numbers are equal!")
elif number_2 == number_1 or number_2 == number_3:
    print(f"Two of your numbers are equal! Which is the number: {number_2}")
elif number_3 == number_1 or number_3 == number_2:
    print(f"Two of your numbers are equal! Which is the number: {number_2}")
    


