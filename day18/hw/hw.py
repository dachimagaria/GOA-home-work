


# 1)მომხმარებელს შემოატანინეთ ორი რიცხვი,
# შეამოწმეთ თუ პირველი რიცხვი მეტია მეორე რიცხვზე დაპრინტე რომ 
# ‘first is more than second’,
# ასევე შეამოწმე თუ პირველი რიცხვი ნაკლებია მეორე რიცხვზე დაპრინტე რომ ‘first is less than second’ და 
# სხვა დანარჩენ შემთხვევაში დაპტინტე რომ ‘first number equal to second number’




num1= int(input("enter first number"))
num2= int(input("enter second number"))


if num1 > num2:
    print("first number in more than second number")
elif num1 < num2:
    print("first number is less than second number")
else:
    print("first number equal to second number")
    



# 2)მომხმარებელს შემოატანინე რაიმე სტრინგი,ასევე შექმენი ცვლადი სადაც შეინახავთ თქვენს სახელს,შემდეგ შეამოწმე თუ მომხმარებლის შემოყვანილი სტრინგი უდრის შენა სახელს დაუპრინტე რომ ‘სეხნიები ვართ’ სხვა შემთხვევაში დაუპრინტეთ რომ ‘სხვადასხვა სახელები გავქვს’

my_name = "dachi"

user = input("enter your name")

if user == my_name:
    print("we have same name")
else:
    print("we have different names")








# 3)შექმენი ორი ცვლადი სადაც შეინახავთ ინტეჯერ ტიპოს მონაცემებს,თქვენი დავალებაა შეამოწმოთ,თუ პირველი რიცხვი მეტია 0 ზე და და მეორე რიცხვიც მეტია 0 ზე დაუპრინტე რომ ‘ორივე რიცხვი დადებითია, ასევე შეამოწმე თუ პირველი რიცხვი ნაკლებია 0 ზე და მეორე რიცხვიც ნაკლებია 0 ზე დაპურინტე რომ  ‘ორივე რიცხვი არის უარყოფით’,სხვა დანარჩენ შემთხვევაში დაუპრინტე რომ ‘ეს რა ჯანდაბაა’


number_1 = int(input("enter first number"))
number_2 = int(input("enter second number"))


if number_1 or number_2 > 0:
    print("first and second number is positive")
elif number_1 or number_2 < 0:
    print("first number and second number is negative")
else:
    print("what a hell is this")





# 4)დაატრიალეთ ფორ ლუპი 50 დან 100 მდე 2 ის გამოტივებით
for i in range(50, 101, 2):
    print(i)



# 5)ვაილ ლუპის გამოყენებით 20 დან 40 მდე გამოიტანეთ ყველა რიცხვი

i = 20
while i <=40:
    print(i)
    i+= 1






# 6)სოლოლერნი შეასრულეთ Modil 4 quiz ის ჩათვლით
# გავაკეთე











