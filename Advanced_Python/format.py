# Format: "<string>".format(arguments)
a= "{} is a good {}".format("Tommy", "Dog") 
print(a)

# these curly brackets are places for the arguments, which are indexed starting from 0
a= "{0} is a good {1}".format("Tommy", "Dog") 
print(a)

a= "{1} is a good {0}".format("Tommy", "Dog") 
print(a) # changing the indices will change the way the arguments are placed