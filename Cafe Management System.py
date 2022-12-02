
dict = {'ColdCoffie': 90, 'sandwich': 70,
    'Tea': 20, 'cake': 400, 'soups': 40}
b = int(input("ENTERED SYSTEM PASSWORD:"))
if(b == 1234):
  print("YOU SUCCESSFULLY LOGIN!")
else:
  print("WRONG PASSWORD,TRY AGAIN!")
  exit()
print("**********WELCOME TO TINKU'S CAFE******")
print("***********TINKU'S CAFE MENU*************")
def display():
 print("AVAILABLE MENU:")
 x = dict.items()
 print(x)
 print("***************************")
def order():
    global sum
    sum = 0
    lst = list(dict.keys())
    while True:
      print(dict)
      print("PRESS E FOR EXIT")
      order = input("enter your order:")
      if order in lst:
         sum = sum+dict[order]
      elif order == 'E':
         break
      else:
         print("Enter right item")
    print("YOUR TOTAL BILL IS:", sum)
    print("**************************")
def add():
    x = str(input("enter the new item:"))
    y = int(input("enter the price of new item:"))
    dict[x] = y
    print(dict)
    print("**************************")


def remove():
    x = str(input("Enter the item you want to remove:"))
    del dict[x]
    print(dict)
    print("**************************")


def update():
    x = str(input("enter the new or remove the item:"))
    y = int(input("enter the price of new item:"))
    dict.update({x: y})
    print(dict)
    print("****************************")
def bill():
        a1 = int(input("YOUR CUSTOMER ID: "))
        a3 = str(input("BILL NAME:"))
        a4 = input("DATE:")
        global a5
        a5 = (input("YOUR MOBILE NUMBER:"))
        a5="+91"+a5
        print("**************************")
        print("**********TINKU'S CAFE**********")
        print("**********BILL GENERATE***********")
        print("YOUR CUSTOMER ID:", a1)
        print("BILL NAME :", a3)
        print("DATE:", a4)
        print("MOBILE NUMBER:", a5)
        print("TOTAL AMOUNT:", sum)
        print("YOUR ORDER IS PLACED!")
        print("THANKING YOU")
        print("VISIT AGAIN!🙂")
        print("*************************")
def U():
     print("1.DISPLAY MENU:")
     print("2.ORDER ITEM:")
     print("3.BILL GENERATE:")
     print("4.ENTER IN ADMIN MODE:")
     num2=int(input("enter your choice:"))
     while True:
       if(num2==1):
        display()
        U()
       elif(num2==2):
        order()
        U()
       elif(num2==3):
        bill()
        U()
       elif(num2==4):
          num3=int(input("**ENTER ADMIN PASSWORD:**\n"))
          if(num3==456):
           print("YOU ARE SUCCESSFULLY LOGGED IN!")
           admin()
          else:
           print("INCORRECT PASSWORD,TRY AGAIN!")
           exit()
           
       else:
        print("INVALID CHOICE:")
def A():
     print("1.ADD ITEM IN MENU:")
     print("2.REMOVE ITEM IN MENU:")
     print("3.UPDATE THE MENU:")
     print("4.ENTER IN USER MODE:")
     num1=int(input("Enter your choice:"))
     while True:
       if(num1==1):
         add()
         A()
       elif(num1==2):
         remove()
         A()
       elif(num1==3):
         update()
         A()
       elif(num1==4):
           user()
           U()
       else:
         print("Invalid choice:")
def user():
     U()
def admin():
     A()
def system():
   print("1.FOR USER")
   print("2.FOR ADMIN")
   num1=int(input("ENTER YOUR CHOICE:"))
   while True:
      if(num1==1):
          user()
      elif(num1==2):
          num3=int(input("**ENTER ADMIN PASSWORD:***\n"))
          if(num3==1234):
           print("YOU ARE SUCCESSFULLY LOGGED IN!")
          else:
           print("INCORRECT PASSWORD,TRY AGAIN!")
           exit()
          admin()
      else:
        #  print("Invalid choice:")   
        print("invalid")
system()
