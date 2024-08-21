from random import randint #import random module and use randint funtion 
uscore=0   #user score initially 0
cscore=0   #computer score initially 0
print("="*10 + "welcome to the rock paper and scissor game" +"="*10)
n=int(input("enter no.of rounds ")) # for how many round you want to play
for i in range(n):
    user=int(input("enter (1 for rock) (2 for paper) (3 for scissor) : "))
    computer=randint(1,3) #now computer generate the number
    if computer==1:
        print("computer select rock")
    elif computer==2:
        print("computer select paper")
    else:
        print("computer select scissor")
    if(user==computer):       #conditions are given 
        print("no score")
    elif ((user==1 and computer==2) or (user==2 and computer==3) or (user==3 and computer==1)):
        print("computer won this round")
        cscore+=1
    elif((user==1 and computer==3) or (user==2 and computer==1 ) or (user==3 and computer==2)) :
        print("user won this round")
        uscore+=1
    else:
        print("invalid input ")
        print("try again")
print("*"*5 + "score of the game" + "*"*5) # score board 
print("|| user score" , uscore ,"          ||")
print("|| computer score" , cscore ,"      ||")
if uscore>cscore:
    print("|| user won the match     ||")
elif uscore==cscore:
    print("|| match draw             ||")
else:
    print("|| computer won the match ||" )
print("_"*12 + "*END*" + "_"*12)
