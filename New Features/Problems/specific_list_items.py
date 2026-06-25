l = [13,33,39,45,456,"Aishik",12.34,'@']

# to set indexes to the items in the list using enumerate()
for index, item in enumerate(l,start=1):
    if (index == 3 or index== 5 or index== 7):
        print(f"{index}. {item}")
print("\n")