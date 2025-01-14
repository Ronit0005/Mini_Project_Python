import random
#comp=random.choice([0,1,2])
comp=random.randint(0,2)
user=int(input('Enter the 0 for Snake_1 for Water_2 for Gun : '))
if user==0 or user==1 or user==2:
    game=['snake','water','gun']
    def check(comp,user):
       if comp==user:
           return 0
       elif (comp==0 and user==1):
           return -1
       elif comp==2 and user ==0:
           return -1
       elif comp==1 and user==2:
           return -1
       else :
           return 1
    x=check(comp,user)
    print(f"You entered : {game[user]}\nComputer entered :{game[comp]} ")
    if x==0:
        print("Draw") 
    elif x==-1:
        print('You Lose') 
    else:
        print("You won")
else:
    raise ValueError("Input The Valid Input \nInput can be only 0 , 1 or 2")   