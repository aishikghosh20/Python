no = -1
# To check the validity of input
while(no < 0):       
    try:
        no = float(input("Enter Length in Inches:\n"))
    except ValueError:
        print("ENter a valid no")
    
def conversion(inch):
    return inch*2.54

ans = conversion(no)
print(ans)
