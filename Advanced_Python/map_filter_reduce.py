from functools import  reduce

l =[1,3,4,2,4,5,2,5,6] # this is the input list

# Map:
square = lambda x:x*x
sqlist = map (square, l) # map applies this fuction to all the items in the list
print(list(sqlist))

print("\n")


# Filter:
# def even_check(n):
#     if (n%2 == 0):
#         return True
#     return False
even_check = lambda x:(x%2 == 0)

onlyeven = filter (even_check, l) # filters out the items which are not meeting the condition of the function
print(list(onlyeven))

evenlist = map (even_check,l) #  for a visual check
print(list(evenlist))

print("\n")


# Reduce:
sum = lambda x,y:x+y

# print(sum(l)) ==> wont work as 2 arguments are neede 

# to make it work reduce() is used
print(reduce(sum, l)) 
