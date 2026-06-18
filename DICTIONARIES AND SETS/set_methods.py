s = {1, 5.35, "Aishik", True} 
print(s)

# To add new element
s.add(566)
print(s)

# To get the length of the set
print(len(s))

# to remove an element and updates the set
s.remove(566)
print(s)

# pop function
print(s.pop()) # removes a random element and returns that element
print(s)

# clear the entire set
s.clear()
print(s)