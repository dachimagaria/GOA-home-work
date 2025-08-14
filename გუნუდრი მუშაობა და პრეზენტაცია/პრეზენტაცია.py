username = input("enter username: ")
password = input("Enter password: ")
Balance = 10
valute = 0
#valute = 0 იგულისხმება ლარი
#valute = 1 იგულისხმება დოლარი
#valute = 2 იგულისხმება ევრო
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
         if question == "deposit":
              money = int(input("How much money do you want to deposit(TYPE NUMBERS ONLY)?: "))
              Balance = Balance + money
              
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






























































































