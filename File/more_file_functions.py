f = open("myfile.txt")
# lines = f.readlines() # creates a list of all the lines in the file
# print(lines)
# print(type(lines))



# line1 = f.readline() # read individual line
# print(line1)
# print(type(line1))

# line2 = f.readline() # read next individual line
# print(line2, type(line2))

# line3 = f.readline() # read next individual line
# print(line3, type(line3))

# # If no more lines exist , will print an empty string
# line4 = f.readline()
# print(line4)



# using loops to read lines
line = f.readline()
while (line !=''):
    print(line)
    line = f.readline()



f.close()