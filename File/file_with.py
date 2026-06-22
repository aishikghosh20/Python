f = open("myfile.txt")
print(f.read())
f.close()

# To avoid f.close() we can write this using a with statement
with open("myfile.txt") as f:
    print(f.read()) 
