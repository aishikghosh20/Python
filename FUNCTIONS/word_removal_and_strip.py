l = ["Aishik", "Harry", "Renu", "Ram"]

word= input("Enter The word to remove:\n")

def remover(l, word):
    n =[]
    for item in l:
        if(not(item==word)):
            n.append(item.strip(word))
    return n
    
print(l)
print(remover(l,word))