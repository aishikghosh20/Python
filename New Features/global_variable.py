a= 89 # global variable with a global value

def func1():
    a=3 # a temprary local change of the variable, doesnot change the global value of 'a'
    print(a)

func1()
print(a)
print("\n")

a =14  # a change in the global value, affects the global variable
print(a)
print("\n")

# Now to use a function to change the value globally instead of a local change
def func2():
    global a # this "global" keyword gives access to the global variable's value

    a= 3 # this changes the variable's value globally
    print(a)

print(a) # before the change

func2() 

print(a) # after the change


