username = input("enter username: ")
password = input("Enter password: ")
Balance_gel = 10
Balance_eur = 0
Balance_usd = 0
# 1 usd = 2.69 gel
# 1 usd = 0.86 eur
# 1 gel = 0.32 eur
if password == "1234" and username == "dachi":
    print("Password is correct")
    question = 4
    while True :
         question = input("What do you want to do? ")
         if question == "log off":
              break
         valute = input("Witch valute do you want (usd gel eur) ")
     
         if valute == "gel":
              print()
                 
             
              if question =="deposit":
                    money = int(input("How much money do you want to deposit(TYPE NUMBERS ONLY)?: "))
              Balance_gel = Balance_gel + money
                 
               
               
         if question == "pay":
              payment = int(input("How much money do you want to pay?"))
              if payment <= Balance:
                   print("Payment succsesful!")
                   Balance = Balance - payment
              else:
                   print("You dont have enough money!(boo hoo)")
         #if question == "conversion":
              
else :
     print("Password or username is incorrect, Try again!")
























































































