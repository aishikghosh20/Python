a =(1, 35,46.69, False, "Aishik", 35, 'a') #This is a tuple

# To count the occurance of a something in it
no =a.count(35)
print(no)

# To get the index of an element
i =a.index(35) # the 1st occurance
print(i)

# To concanate
b = ("jojo", 43.76, True, None, 12, '!')
print(a+b)

#To repeat
print(b * 4)

# To check the presence of an element
print(35 in a) # returns boolean data
print(35 in b)

# TO get the element at a known index
print(a[1])

# Slicing
print(b[2:5])

# Nested Tuples
c = ((34.5, False, 12),("Good", '@', True))
print(c[0][2])
print(c[1][1])
