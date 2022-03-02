import random

words=["blue","pink","brown","black","green"]
userGuesses=[]
myWord=random.choice(words)

def askForName():
    name = input("Please enter your name: ")
    if name.isalpha():
        print(f"Welcome {name} ... Let's Play")
        print(len(myWord))
        return name
    return askForName()

def hangmanGame():
    turns=0
    while turns<7:
        matched=0
        userGuess=input("\nGuess any alphabet....  ")
        userGuesses.append(userGuess)
        if userGuess not in myWord:
            turns+=1
            print("Wrong guess... try again")
        else:
            for alpha in myWord:
                if alpha in userGuesses:
                    print(alpha, end=" ") 
                    matched+=1                
                else:
                    print("_", end=" ")
                    continue
            turns+=1
            
        if turns==7 & matched!=len(myWord):
            print("\nYou lost ..... wish you try again later")
        else:
            if matched==len(myWord):
                print("\nYou WON ..... Great Job")
                break
    
userName=askForName()
hangmanGame()



