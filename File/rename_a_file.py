with open("old.txt","r") as f:
    content1 = f.read()

with open("renamed.txt","w") as f:
    f.write(content1)