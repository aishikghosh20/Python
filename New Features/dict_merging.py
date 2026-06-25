dict1 = {1:"one",2:"two",3:"three"}
dict2 = {2:"Aishik",4:"four", 5: "Five"}

merged = dict1 | dict2 # merging the two dictionaries
# The keys which are present in the 2nd dictionaries will have their values updated

print(merged)