print("Welcome To Our Restraunt...................." )#greeting the 
#con='yes'
#bill=0
eat=input('''Sir Would You Like To Give Your Order..........
          Say \"yes\" For Ordering And Say \"no\" For Delaying The Order
           :   --->>>''')
#come=input('do you want to eat')
#zender=input("Enter your zender sir or mamdam")
bill=0
menu={'coffee':220,
      'dosa':180,
      'chowmein':120,
      'cold drinks':70,
      'maggie':30,
      'pasta':120
}

while eat=='yes':
   print("The Menu : ")
   print("coffee : Rs220\ndosa : Rs180\nchowmein : Rs120\ncold drinks : Rs70\nmaggie : Rs30\npasta :Rs 120")
   order=input('Can I Take Your Order   ---->>>>')
   if order in menu.keys():
         bill=bill+menu[order]
         print(f"Here Is Your Order Which is {order}")
   else :
          print(f"{order} Is Not Available In Our Restraunt")
   eat=input("Do You Want Something Else If Yes say \"yes\"  Otherwise say \"no\" For Concluding   ---->>>>")
print(f"Here Is Your Bill ---->>>Rs{bill}\nThanks For Visting Our Restraunt\nHope you like Our Restraunt...............")
