h= int(input("Enter Height:\n"))
w= int(input("Enter Width:\n"))
for i in range(1,h+1):
    if(i == 1 or i==h):
        print("*"*w)
    else:
        print("*"," "*(w-4),"*")