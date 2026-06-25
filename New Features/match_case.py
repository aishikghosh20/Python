def status(no):
    match no:
        case 200:
            return  ("ok")
        case 404:
            return "not forund"
        case 500:
            return "Internal server error"
        case _: # default case
            return "Unknown status"
    
print(status(500))
print(status(200))
print(status(404))
print(status(7))