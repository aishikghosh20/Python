l = []

for i in range(4):
    a= input(f"ENter the name {i+1}:\n")
    l.append(a)

for name in l:
    if(name.startswith('S')):
        print(f"Hello! {name}")