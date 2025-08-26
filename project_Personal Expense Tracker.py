import os
import datetime
import time
import emoji
import tabulate
z = emoji.emojize(":watch:")

print (f"Welcome to Personal Expense Tracker!{z} ")
print(f"Today's date: {datetime.date.today()}\n")
def chos():
   print(" 1. Add new expense \n 2. View expenses\n 3. Exit")
chos()
dict = {"food" : 0   ,
        "travel" : 0 ,
        "shopping" : 0,
        "health"  : 0,
        "rent"  : 0,
        "bills" :0}

def choices():         
        enter_saving = float(input("Enter your expenditure 💸:  "))        
        Enter_category =  input("Food, Travel,food,rent ,bills,etc : ").strip().lower()
        a = dict.get(Enter_category)
        b = int(a)
        dict.update({Enter_category:enter_saving + b })
        print("Saved")
          

def play():   
   enter = int(input("choose number to corresponding task : "))     
   if enter == 1:
    choices()
    users =int(input("press 1 to exit")) 
    if users == 1:
        chos()
        play()
   elif enter == 2:
       print(f"Your expenditures are : {dict}")
       users =int(input("press 1 to exit")) 
       if users == 1:
        chos()
        play()
   elif enter == 3:
      print("Thank you for using")
   else:
      print("invalid")
      
play()