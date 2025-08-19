import random

def logic(a, b,c,d,e,f):

    if a==b:
        print("Its a DRAW!!!!")
    elif a==1 :
        if b==3:
            print("You WON!!!")
            return "WIN"
        else:
            print("You LOSS!!!")
            return "LOSS"
    elif a==2:
        if b==1:
            print("You WON!!!")
            return "WIN"
        else:
            print("You LOSS")
            return "LOSS"
    elif a==3:
        if b==2:
            print("You WON!!!")
            return "WIN"
        else:
            print("You LOSS!!!")
            return "LOSS"



dict1 = {1:"Rock", 2: "Paper", 3:"Scissor" }

win=0
loss=0
draw=0

loop_state= True
while loop_state:
    player_input= int(input("Enter your choice(Rock=1, Paper=2, Scissor=3): "))
    if player_input!= 1 and player_input!= 2 and player_input!= 3:
        print("Invalid input!!!")
        continue


    bot_input= random.randint(1,3)

    print(f"Your input: {dict1[player_input]} & Bot input: {dict1[bot_input]}" )

    check= logic(player_input,bot_input,dict1,win,loss,draw)

    if check=="WIN":
        win+=1
    elif check=="LOSS":
        loss+=1
    else:
        draw+=1


    loop2= True
    while loop2:
        score= input("Do you want see the score(y/n):").lower()
        if score== "y":
            print(f"Total Wins: {win} and Total Losses: {loss} and total Draws: {draw}")
            break
        elif score== "n":
            break
        else:
            print("Enter valid input!!!")
            continue

    loop3= True
    while loop3:
        repeat= input("Do you want to play again(y/n):").lower()
        if repeat== "n":
            loop_state=False
            break
        elif repeat== "y":
            loop_state= True
            break
        else:
            print("Invalid input!!")
            continue

