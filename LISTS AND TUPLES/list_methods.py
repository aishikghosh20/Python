data = ["Aishik", "Jojo", 6, 67.06, True, 'A', None] # this is a list 
print(data)

# To add something at the end of the list
data.append("Mojo")
print(data)
data.append(1556.665)
print(data)

# To reverse the list
data.reverse()
print(data)

# To sort lists
l1 =[1,67,23,45,93,98.2367,73.789,27]
l1.sort()
print(l1)

# To insert
l1.insert(4,68.76)
print(l1)

# To remove elements
print(l1.pop(4)) # returns the element which was removed from the list
print(l1)
l1.remove(45) # removes a known element
print(l1)

