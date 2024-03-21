#Problem 1.1

#Added an int()
number = int(input("Enter a number: ")) 

if number > 0:
    print("The number is positive.")

#Added an extra '='
elif number == 0:
    print("The number is zero.")
    
#Got rid of else condition because it is not needed
else:
    print("The number is negative.")