a= int(input("Enter a dividend\n"))
b= int(input("Enter a divisor\n"))

if (b==0):
    raise ZeroDivisionError("Division by 0 is not possible") # Custom error message to display

print(f"The result is : {a/b}")