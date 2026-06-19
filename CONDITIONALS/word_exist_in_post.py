post = input("Enter the post:\n")
word = input("Enter the word you want to find:\n")
new = post.lower()

if (word.lower() in new):
    index= new.index(word.lower())
    print(f"The word exists at index: {index}")
else:
    print("THe word is not present inthe post")
