no = -1
# To check the validity of input
while(no < 0):       
    try:
        no = int(input("Enter Temperature:\n"))
    except ValueError:
        print("ENter a valid no")

def change(f):
    c= 5*(f-32)/9
    return c

print(f"{round(change(no), 2)} C")