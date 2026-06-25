try:
    a= int(input("Enter a number\n"))

except ValueError:
    print("Invalid input") 

else:
    print ("Input was successful") # the else block will be carried out only if the try is successful

finally:
    print ("An Input was made by the user") # the else block will always be carried out 