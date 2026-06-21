import random, time, os
options = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

replay = True
player_score = 0
computer_score =0

def gui():
    # GUI element for a menu
    print("\033[1;96m          ROCK  PAPER  SCISSORS\033[0m")
    print("\033[36m==========================================")
    print("\033[1;33m               CHOICES\033[0m")
    print("\033[36m==========================================\033[0m")
    print("\033[1;36m1 : Rock\t2 : Paper\t3 : Scissors\033[0m\n")
    #To prompt for user input and check its validity
    valid = False
    while not(valid):
        try:
            choice = int(input("\033[36mEnter a choice:\033[0m\n"))
        except ValueError:
            print("\033[1;91mENTER A VALID INPUT\033[0m\n")
            time.sleep(1)
            continue
        if (choice >0 and choice<4):
            valid = True
        else:
            print("\033[1;91mENTER A VALID CHOICE\033[0m\n")
            time.sleep(1)
    
    return choice


def comp_choice():
    # To get a random computer choice and print it
    comp_choice = random.choice(list(options.keys()))
    print("\033[1;96m\nComputer is choosing...\033[0m")
    time.sleep(1.5)
    print("\033[1;96mComputer has made its choice...\033[0m")
    time.sleep(1)
    print("\033[1;95mTHE COMPUTER CHOSE:\033[0m", end = "")
    time.sleep(1)
    print(f"\033[1;93m {options[comp_choice]}\033[0m")
    return comp_choice

def check(choice,comp_choice):
    time.sleep(1)
    if choice == comp_choice:
        print("\033[1;93m      DRAW\033[0m")
        return -1
    elif (choice==1 and comp_choice==3) or (choice==3 and comp_choice==2) or (choice==2 and comp_choice==1):
        print("\033[1;92m     YOU WIN!!\033[0m")
        return 1
    else:
        print("\033[1;91m     YOU LOST\033[0m")
        return 0

while (replay):
    choice= gui()
    cmp_choice = comp_choice()
    result = check(choice, cmp_choice)
    if result==1:
        print("\033[1;92m+1POINTS TO THE PLAYER!!\033[0m")
        player_score +=1
    elif result==0:
        print("\033[1;91m+1POINTS TO COMPUTER!!\033[0m")
        computer_score +=1
    else:
        print("\033[1;93mNO POINTS ALLOTED\033[0m")
    
    print("\n\033[36mDO YOU WANT TO CONTINUE PLAYING?\033[0m")
    print("\033[36m1. \033[1;92mYES\033[0m  \033[36m2. \033[1;91mNO\033[0m\n")
    valid = False
    while not(valid):
        try:
            decision = int(input("\033[36mENTER CHOICE: \033[0m\n"))
        except ValueError:
            print("\033[1;91mENTER A VALID INPUT\033[0m\n")
            time.sleep(1)
            continue
        if (decision == 1):
            print("\n")
            valid = True
            time.sleep(1)
        elif (decision ==2):
            time.sleep(1)
            replay =False
            valid = True
        else:
            print("\033[1;91mENTER A VALID CHOICE\033[0m\n")
            time.sleep(1)

print("\n")
print("\033[1;93m===========FINAL SCORES============\033[0m")
print(f"\033[1;97mPLAYER: {player_score}\033[0m")
print(f"\033[1;97mCOMPUTER: {computer_score}\033[0m")

time.sleep(1)
print("\n\033[1;95m!!Thank you for playing!!\033[0m")
time.sleep(1)
print("\n\033[1;95mCoded by: Aishik Ghosh\033[0m")
input("\nPress Enter to Exit...")