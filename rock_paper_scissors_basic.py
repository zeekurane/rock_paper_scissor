import random
print("Welcome to Rock-Paper-N-Scissors!")
options=["rock","paper","scissors"]

def whowins(a,b):
    if a=='rock':
        if b=='paper':
           return "Computer wins!"
        elif b=='scissors':
           return "You win!"
        else :
            return "Tie!" 
    if a=='paper':
        if b=='scissors':
           return "Computer wins!"
        elif b=='rock':
           return "You win!"
        else :
            return "Tie!" 
    if a=='scissors':
        if b=='rock':
           return "Computer wins!"
        elif b=='paper':
           return "You win!" 
        else :
            return "Tie!"   
    
    
while True:
    user_input=input("Pick any-one from rock / paper / scissors. Enter \'Q\' to exit the game. ").lower()
    if user_input=="q":
        quit()
    elif user_input not in options:
        print("Error!")
        continue
    
    computer_input=random.randint(0,2)
    print("Computer chooses "+ options[computer_input] + ".")
    print(whowins(user_input,options[computer_input]))
    