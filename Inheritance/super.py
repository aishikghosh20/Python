class baselevel:
    a =1
class level1(baselevel):
    b=2
    def __init__(self):
        print("Hello!!")
class level2(level1):
    c =3
    def __init__(self):
        super().__init__() # access the constructor to the parent too
        print("World")

o =baselevel()
print(o.a)

o = level1()
print(o.a, o.b)

o = level2()
o.c =5
print(o.a, o.b, o.c)