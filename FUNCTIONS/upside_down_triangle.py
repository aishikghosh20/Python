no = -1
# To check the validity of input
while(no < 0):       
    try:
        no = int(input("Enter Height:\n"))
    except ValueError:
        print("ENter a valid no")

def triangle(n):
    if (n ==1):
        print("*")
        return
    print("*"*n)
    triangle(n-1)

triangle(no)
