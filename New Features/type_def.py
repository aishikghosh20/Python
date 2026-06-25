# Using type defination to annotate the type of the variable
n : int = 5
name : str = "Aishik"

def  sum(a:int , b:int) -> int:  # To annotate that this function will take in 'int' type parameters and return an 'int' value
    return a+b

# This is mainly used to help programmers indentify the types of variables and functions when working on other's codes 