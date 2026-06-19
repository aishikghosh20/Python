n = int(input("ENter the no :\n"))

for i in range (2,n):
    if (n%i)==0 :
        print("The no is Composite")
        break
else:
    print("The no is prime")
