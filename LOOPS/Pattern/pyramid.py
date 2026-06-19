h = int(input("ENter the height:\n"))
a=1

for i in range(1,h+1):
    print(" "*(h-i), "*"*a)
    a+=2
