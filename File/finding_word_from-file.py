with open("poems.txt") as f:
    content =f.read()
    word = input("ENter the word to search:\n")
    lower_content= content.lower()
    if (word.lower() in lower_content):
        print("The word is present in the file")
    else:
        print("NOT PRESENT")