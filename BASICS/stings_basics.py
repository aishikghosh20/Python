name = "Aishik"
length = len(name)

# slicing of the string
short1 = name[0]
print (short1)

short2 = name[1:4]
print(short2)

# negative slicing
short3 = name[-1]
print (short3)

short4 = name[-4:-1]
print(short4)


print(name[1:]) # same as name[1:len(name)]
print(name[:4]) # same as name[0:4]

# Skipping while slicing
short5 = name[1:5:2] # '2' makes string to skip ever 2nd char from the range- 1 to 4
print(short5)