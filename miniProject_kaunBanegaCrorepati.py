import time
print("Welcome Kaun Banega Karorpati..........")
print('''Here Is The Rules Of The Game: 
         1 . There are total 10 questions and if you gave the correct answer for all those question you would take 7crores to your home
         2 . If you gave wrong answer to any question , the game would end .
         3 . You would take 1lakh if you will give correct answer for first 4 questions and you will get 1crore if you will 
             give correct answer for first 8 questions and you will get 7crores if you will give correct answer for first 10 questions''')
takeHomeMoney=0
questions=[['what is capital of india','bejing','new delhi','washington','katmandu'],
['what is capital of usa','washington','new delhi','bejing','katmandu'],
['what is capital of china','bejing','washington','new delhi','katmandu'],
['what is capital of nepal','katmandu','new delhi','washington','bejing'],
['what is national fruit of india','mango','guava','papaya','grapes'],
['what is capital of usa','washington','new delhi','bejing','katmandu'],
['what is capital of china','bejing','washington','new delhi','katmandu'],
['what is capital of nepal','katmandu','new delhi','washington','bejing'],
['what is national fruit of india','mango','guava','papaya','grapes']]
answer=['new delhi','washington','bejing','katmandu','mango','washington','bejing','katmandu','mango']
for i in range(len(questions)):
    print("\n\n")
    print(f"Here Is The {i+1} Question Of You...")
    print(questions[i][0])
    print(f"Options are :   a . {questions[i][1]}           b . {questions[i][2]}")
    print(f"                c.  {questions[i][3]}           d . {questions[i][4]}")
    x=input("Answer is : ")
    if x==answer[i]:
        print(f"{x} Is A Correct Answer !!!!!!!")
    else:
        print("Sorry Wrong Answer!!!!!!!")
        break
    if i==3:
        takeHomeMoney=100000
    elif i==7:
        takeHomeMoney=100000000
    elif i==len(answer)-1:
        takeHomeMoney=700000000
print("You won :Rs",takeHomeMoney)
time.sleep(2)
print("Thanks For Playing.........")