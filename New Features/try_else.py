try:
    a= int(input("Enter a number\n"))
except ValueError:
    print("Invalid input") 
else:
    print ("Input was successful") # the else block will be carried out if the try is successful

