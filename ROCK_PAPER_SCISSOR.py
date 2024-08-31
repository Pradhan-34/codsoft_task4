import random
print("WELCOME TO ROCK, PAPER AND SCISSOR GAME")
print("PRESS R FOR ROCK : PRESS P FOR PAPER : PRESS S FOR SCISSOR")
print("ROCK BEATS SCISSOR : SCISSOR BEATS PAPER : PAPER BEATS ROCK")
def main():
    
    uc=input("ENTER YOUR CHOICE ")
    cc=random.choice(["R","P","S"])
    print("USER CHOICE IS ",uc)
    print("COMPUTER CHOICE IS ",cc)


    if cc==uc:
        print("MATCH DRAW")
    elif (cc=="R") and (uc=="P" or "p"):
        print("YOU WIN")
    elif (cc=="S") and (uc=="P" or "p"):
        print("YOU LOSE")
    elif (cc=="P") and (uc=="S" or "s"):
        print("YOU WIN")
    elif (cc=="P") and (uc=="R" or "r"):
        print("YOU LOSE")
    elif (cc=="R") and (uc=="S" or "s"):
        print("YOU LOSE")
    elif (cc=="S") and (uc=="R" or "r"):
        print("YOU WIN")
    else:
        print("ENTER A VALID CHOICE")
    
    a=input("WANT TO PLAY AGAIN??? (Y/N)")
    if a=="y" or a=="Y":
        main()
    elif a=="n" or a=="N":
        print("THANKS FOR PLAYING")
        exit()
    else:
        print("INVALID INPUT")
        exit()    
main()
  
