l = [1,2,3,4,5,6,7,8,9,10]

try:
    no = int(input("Enter the number of the multiplication table:\n"))
except ValueError:
    print("Invalid input")

table = [no*i for i in l]
print (table)

with open("tables.txt","a") as f:
    f.writelines(str(table) + '\n')