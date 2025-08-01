
 #Input (შეყვანა) ნიშნავს იმას, რომ მომხმარებელი ან სხვა წყარო აწვდის მონაცემებს პროგრამას.
# მაგალითად, მომხმარებელი აწერს რიცხვს და პროგრამა ამ რიცხვს იყენებს შემდეგ მოქმედებებში.
num = input("enter number: ")
num = int(num)



#Output (გამოყვანა) ნიშნავს იმას, რომ პროგრამა რაღაც შედეგს გვიჩვენებს – ეკრანზე გამოჰყავს.
# ეს შეიძლება იყოს ტექსტი, რიცხვი ან სხვა ტიპის ინფორმაცია, რომელიც მომხმარებელმა უნდა იხილოს.
name = input("what your name?"  )  
print("hello, ", "dachi")





number = input("13000: ")
print("The type of the entered value is integer:", type(number))


# ეს ცვლადები ინახავენ string ტიპის მონაცემებს
name="dachi" 
tech="samsung"
carbrand="BMW"
book="sherlok holmse"
surname="arqania"

#ეს ცვლადები ინახავენ integer ტიპის მონაცემებს
age=13
kelometers=200
meters=700
suntimeters=90
milimeters=1000


#ეს ცვლადები ინახავენ float ტიპის მონაცემებს
height=1.79
width=2.80
length=10.90
weight=40
number=12.5

text_var = "Hello, world!"
int_var = 42              
float_var = 3.14 


print(type(text_var))   # <class 'str'>
print(type(int_var))    # <class 'int'>
print(type(float_var))  # <class 'float'>


word1 = input("write first letter:" "hello" )
word2 = input("write second letter:" "friend")
print(word1+word2)#hellofriend გამოიტანს ტერმინალზე




num1 = float(input("შეიყვანე პირველი რიცხვი: "))
num2 = float(input("შეიყვანე მეორე რიცხვი: "))
num3 = float(input("შეიყვანე მესამე რიცხვი: "))
num4 = float(input("შეიყვანე მეოთხე რიცხვი: "))
num5 = float(input("შეიყვანე მეხუთე რიცხვი: "))

# საშუალო არითმეტიკულის გამოთვლა
average = (num1 + num2 + num3 + num4 + num5) / 5

# შედეგის დაბეჭდვა
print("შეყვანილი რიცხვების საშუალო არითმეტიკული არის:", average)


name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")
height = input("შეიყვანეთ თქვენი სიმაღლე (სმ): ")
weight = input("შეიყვანეთ თქვენი წონა (კგ): ")

# ერთი დიდი წინადადების დაბეჭდვა
print(f"{name} (surname) არის {age} წლის, მისი სიმაღლეა {height} სანტიმეტრი და წონა — {weight} კილოგრამი.")

