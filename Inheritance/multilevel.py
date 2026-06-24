class baselevel:
    a =1
class level1(baselevel):
    b=2
class level2(level1):
    c =3

o =baselevel
print(o.a) # prints the attribute
# print(o.b) <== wont work as a b attribute doent exist in baselevel

o = level1
print(o.a, o.b)
# print(o.c) <== wont work as a c attribute doent exist in level1

o = level2
print(o.a, o.b, o.c)