def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        print ('Shift must be an integer value.')
        return

    if shift < 1 or shift > 25:
        print('Shift must be an integer between 1 and 25.')
        return

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

print("""What do you want to do:
        1.Encrypt a message   2.Decrypt a message""")
decision = 0 
valid = False
while not(valid):
    try: 
        decision = int(input("\033[36mENTER CHOICE: \033[0m\n"))
    except ValueError:
        print("\033[1;91mENTER A VALID INPUT\033[0m\n")
        continue
    if (decision == 1):
        valid = True
    elif (decision ==2):
        valid = True
    else:
        print("\033[1;91mENTER A VALID CHOICE\033[0m\n")

if (decision ==1):
    text = input("Enter the message to encrypt:\n")
    valid = False
    while not valid:
        try: 
            shift = int(input("Enter the shift amount\n"))
        except ValueError:
            print("\033[1;91mENTER A VALID INPUT\033[0m\n")
            continue
        valid = True

    print(encrypt(text,shift))
else:
    text = input("Enter the message to decrypt:\n")
    valid = False
    while not valid:
        try: 
            shift = int(input("Enter the shift amount\n"))
        except ValueError:
            print("\033[1;91mENTER A VALID INPUT\033[0m\n")
            continue
        valid = True

    print(decrypt(text,shift))

input("Press ENTER to exit...")
