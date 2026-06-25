try :
    a= int(input("Enter a number\n"))
except ValueError:
    print("Invalid input") # this is carried out when an error arises during the input - like entering a character instead of an int-type value

print ("Input was successful")