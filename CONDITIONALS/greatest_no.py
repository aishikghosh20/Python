a1= int(input("Enter no 1:\n"))
a2= int(input("Enter no 2:\n"))
a3= int(input("Enter no 3:\n"))
a4= int(input("Enter no 4:\n"))

if (a1>a2 and a1>a3 and a1>a4):
    print("The greatest nos is:",a1)
elif (a2>a1 and a2>a3 and a2>a4):
    print("The greatest nos is:",a2)
elif (a3>a1 and a2<a3 and a3>a4):
    print("The greatest nos is:",a3)
else:
    print("The greatest nos is:",a4)

