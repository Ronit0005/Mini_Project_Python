import time as t
import pandas as pd 
t.sleep(0.5)
choice =int(input('''Enter 1 for shopping 
Enter 2 for meal plannning
Enter 3 for household chores\n-> '''))
if choice==1:
 weekly_requirement={
    "stuff":['tomato','potato','chilli','onion','rice'],
    "quantity":[5,5,1,3,1]
 }
 df=pd.DataFrame(weekly_requirement)
 print("Welcome To Our Service")
 t.sleep(1)
 current_stuff=list()
 current_stuff_qty=list()
 print("ENTER THE CURRENT STUFF YOU HAVE AT YOUR HOME")
 x=1
 item_number=1
 while x!=0:
   print("Enter 1 to add items Or Enter 0 to exit if you are done")
   t.sleep(1)
   x=int(input("-> : "))
   t.sleep(1)
   if x==0:
      break
   inp=input(f"Item {item_number} : ")
   current_stuff.append(inp)
   inp_qty=int(input("Quantity left : "))
   current_stuff_qty.append(inp_qty)
   item_number+=1
 t.sleep(1)
 print("Recomendation to buy stuff :")
 need_to_recommend=list()
 def check_avaibilty(current,current_qty):
   for i in range(len(current_stuff)):
      if current==current_stuff[i] and current_qty>current_stuff_qty[i]:
         return True
   return False
 for i in range(len(df["stuff"])):
   if check_avaibilty(df.loc[i,"stuff"],df.loc[i,"quantity"])==False:
      need_to_recommend.append(df.loc[i,'stuff']) 
 print(need_to_recommend) 


elif choice==2:
    dishes = {
    "Tea": ['milk', 'tea leaves', 'sugar'],
    "Coffee": ['milk', 'coffee powder', 'sugar'],
    "Pasta": ['pasta', 'olive oil', 'garlic', 'tomato sauce', 'cheese'],
    "Sandwich": ['bread', 'butter', 'cheese', 'vegetables'],
    "Salad": ['lettuce', 'tomato', 'cucumber', 'olive oil', 'lemon juice'],
    "Dal": ['lentils', 'water', 'salt', 'turmeric', 'garlic'],
    "Rice": ['rice','salt'],
    "Chapati": ['wheat flour', 'water', 'salt'],
    "Smoothie": ['banana', 'milk', 'honey', 'nuts'],
    "Maggie": ['instant noodles', 'water', 'spices'],
    "Pizza": ['pizza base', 'tomato sauce', 'cheese', 'vegetables'],
    "Burger": ['burger bun', 'lettuce', 'cheese', 'patty', 'mayonnaise'],
    "Samosa": ['potatoes', 'flour', 'spices', 'oil'],
    "Upma": ['semolina', 'water', 'vegetables', 'spices'],
    "Poha": ['flattened rice', 'onion', 'mustard seeds', 'curry leaves'],
    "Dosa": ['rice', 'urad dal', 'salt', 'water'],
    "Idli": ['rice', 'urad dal', 'salt', 'water'],
    "Pakora": ['gram flour', 'vegetables', 'spices', 'oil'],
    "Chole": ['chickpeas', 'tomato', 'onion', 'spices'],
    "Rajma": ['kidney beans', 'tomato', 'onion', 'spices'],
    "Pulao": ['rice', 'vegetables', 'spices', 'oil'],
    "Kheer": ['milk', 'rice', 'sugar', 'cardamom'],
    "Halwa": ['semolina', 'sugar', 'ghee', 'dry fruits'],
    "Paratha": ['wheat flour', 'water', 'salt', 'oil'],
    "Biryani": ['rice', 'vegetables', 'spices', 'yogurt'],
    "Spring Rolls": ['spring roll sheets', 'vegetables', 'soy sauce', 'oil'],
    "Manchurian": ['cabbage', 'corn flour', 'soy sauce', 'garlic'],
    "Pancakes": ['flour', 'milk', 'sugar', 'baking powder'],
    "Omelette": ['egg', 'salt', 'pepper', 'onion'],
    "Gulab Jamun": ['milk powder', 'sugar', 'cardamom', 'ghee'],
    "Sheera": ['semolina', 'ghee', 'sugar', 'cardamom'],
    "Khichdi": ['rice', 'lentils', 'turmeric', 'salt', 'ghee'],
    "Lassi": ['curd', 'sugar', 'cardamom'],
    }
    t.sleep(0.5)
    current_items=list()
    print("Enter the current stuff you have at your home ")
    while True:
        rooter=int(input("Enter 1 to add the item , if finished then Enter 0\n-> "))
        if rooter==0:
            break
        else :
            items=input("Item : ")
            current_items.append(items)
    def check_2(particular_item):
       for i in current_items:
          if i==particular_item:
             return True
       return False
    def check(particular_dish):
       for i in particular_dish:
          if check_2(i)==False:
             return False
       return True
    key=dishes.keys()
    recom=list()
    for i in dishes.keys():
       if check(dishes[i])==True:
         recom.append(i)
    print("According to availability you can make ")
    for i in recom:
       print('-',i)

else:
   no_of_member=int(input('Enter the number of family memeber \nMaximum number :10 : '))
   names=list()
   for i in range(no_of_member):
      name=input('Enter the name or role of the family member : ')
      names.append(name)
   work_time_start=list()
   work_time_end=list()
   work_list=list()
   work_list_time_start=list()
   work_list_time_end=list()
   for j in range(no_of_member): # working time of family member .
     a1=int(input(f'Enter the start of work time of {names[j]}: '))
     work_time_start.append(a1);
     a2=int(input(f'Enter the end of work time of {names[j]}: '))
   work_time_end.append(a2)
   no_of_work=int(input("Enter the number of work you have : "))
   for k in range(no_of_work):
     work=input('Enter the work : ')
     work_list.append(work)
     start_work=int(input(f'Enter the start of the work {work_list[k]} : '))
     work_list_time_start.append(start_work)
     end_work=int(input(f'Enter the end of the work {work_list[k]} : '))
     work_list_time_end.append(end_work)
   
   def compare(end,str):
      recom=list()
      recom.clear()
      for m in range(no_of_member):
         if end<work_time_start[m] or str>work_time_start[m]:
             recom.append(names[m])
      return recom
   for n in range(no_of_work):
      print(f"The task {work_list[n]} can be done by : ")
      for i in compare(work_list_time_end[n],work_list_time_start[n]):
         print('-',i)
