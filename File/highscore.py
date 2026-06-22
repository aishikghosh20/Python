import random

def game():
    score = random.randint(1,62)
    print(f"Your score is : {score}")
    # to fetch the previous highscore
    with open("highscore.txt") as f:
        highscore = f.read()
        if (highscore!=""):
            highscore = int(highscore)
        else:
            highscore =0
    
    #to check and update the the highsore accordingly
    if(score>highscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))

    return score

game()