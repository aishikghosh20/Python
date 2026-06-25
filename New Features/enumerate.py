l = [13,33,39,45,456,"Aishik"]

# to get indexes of the items in the list using enumerate()
for index, item in enumerate(l):
    print(f"{index}. {item}")
print("\n")

# we can make the enumeration start from a specific number
for index, item in enumerate(l, start = 1):
    print(f"{index}. {item}")