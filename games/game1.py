import random
print("Welcome to Rock paper and scissors game. Gmae will be out of 5")
list=["rock","paper","scissors"]
name=input("Player's names:")
comp=0
play=0
while play<=5 or comp<=0:
    a=input("Enter your choice:")
    if a not in list:
        print("Choose from rock, paper and scissors only.")
    else:
        b=random.choice(list)
        if b==a:
            print("Comp:",b)
            print("Tie")
        elif a=='rock' and b=='scissors':
            print("Comp:",b)
            print("Winner:",name)
            play=play+1
            print('Player:',play,'Comp:',comp)
        elif a=='rock' and b=='paper':
            print("Comp:",b)
            print("Winner: Comp")
            comp=comp+1
            print('Player:',play,'Comp:',comp)
        elif a=='paper' and b=='scissors':
            print("Comp:",b)
            print("Winner: Comp")
            comp=comp+1
            print('Player:',play,'Comp:',comp)
        elif a=='paper' and b=='rock':
            print("Comp:",b)
            print("Winner:",name)
            play=play+1
            print('Player:',play,'Comp:',comp)
        elif a=='scissors' and b=='paper':
            print("Comp:",b)
            print("Winner:",name)
            play=play+1
            print('Player:',play,'Comp:',comp)
        elif a=='scissors' and b=='rock':
            print("Comp:",b)
            print("Winner: Comp")
            comp=comp+1
            print('Player:',play,'Comp:',comp)
if comp==5:
    print("Comp wins")
else:
    print(name,'Wins')

