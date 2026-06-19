p1 = "Check my bio!!"
p2 = "Join my discord"
p3 = "Click the"

message = input("Enter the comment:\n")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This comment is a spam")
else:
    print("This comment is not  a spam")