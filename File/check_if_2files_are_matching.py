with open("file.txt","r") as f:
    content1 = f.read()

with open("myfile.txt","r") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes these files are identical")
else:
    print("No these files are not identical")