
# 14)while ციკლის დახმარებით გამოიტანეთ რიცხვები 50 დან 100 მდე 5 ის გამოტოვებით --> 50 55 60            

i=50
while i <=100:
    print(i)
    i += 5



# 15)for ციკლის დახმარებით გამოიტანეთ რიცხვები 40 დან 90 მდე 3 ის გამოტოვებით -- > 40 43 46 ...

for i in range(40 ,90 ,3 ):
    print(i)






# 16)გამოიტანე შენი სახელი და გვარი 15 ჯერ,გააკეთე ორივე ვარიანტით როგორც for ასევე while loop ის დახმარებით

i = 0
while i < 15:
    print("dachi arkania")
    i+=1



# 17)
# შექმენი ცვლადი სადაც შეინახავ შენს სახელს
# შექმენი ცვლადი სადაც შეინახავ შენს გვარს
# მომხმარებელს შემოატანინეთ სახელი
# თუ მომხმარებელმა შემოიტანა იგივე სახელი რაც შენ გქვია მაშინ:
#       მომხმარებელს შემოატანინე გვარი
#       თუ მომხმარებლის შემოტანილი გვარი დაემთხვა შენს გვარს
#             დაპრინტე --> same name and surname
#       სხვა შემთხვევაში
#             დაპრინტე -- > same name but different surname
# სხვა შემთხვევაშში(ანუ თუ მომხმარებელი თავიდანვე შემოიყვანს არასწორ სახელს)
#     დაპრინტე --> aqedan moshordi





my_name = "dachi"
my_surname = "arkania"

user_name = input("enter your name ")

if user_name == my_name:
    user_surname = input("enter your surname ")
    if user_surname == my_surname:
        print("same name and surname ")
    else:
        print("same name but different surname ")
else:
    print("aqedan moshordi")


# 18)
# შექმენი ცვლადი სადაც შეინახავ პაროლს
# მომხმარებელს შემოატანინე პაროლი
# სანამ პირობა არის ჭეშმარიტი(True)
#       თუ მომხმარებლის პაროლი დაემთხვა შენს პაროლს:
#             დაპრინტე --> გამოიცანი
#              break
#       სხვა შემთხვევაში:
#           თავიდან გაუმეორე რომ შემოიყვანოს პაროლი

password = "1234"

while True:
    user_password = input("შეიყვანე პაროლი: ")
    if user_password == password:
        print("გამოიცანი")
        break




