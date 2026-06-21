no = -1
# To check the validity of input
while(no < 0):       
    try:
        no = int(input("Enter a no:\n"))
    except ValueError:
        print("ENter a valid no")


def factorial(no):
    if (no ==0 or no==1): # base case to stop the loops
        return 1
    return (no*factorial(no-1))

fact = factorial(no)
print(f"The factorial of {no} is {fact}")