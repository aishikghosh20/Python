try:
    with open("1.txt","r") as  f:
        print(f.read())
except Exception as e: # to get the exception message and print it
    print(e)
    print("\n") 
try:
    with open("2.txt","r") as  f:
        print(f.read())
except Exception as e: # to get the exception message and print it
    print(e)
    print("\n") 
try:
    with open("myfile.txt","r") as  f:
        print(f.read())
except Exception as e: # to get the exception message and print it
    print(e)
    print("\n") 

print("Thank You!!")
