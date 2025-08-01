



#დავალება 1
#შედარების ოპერატორები --> როცა რაიმე რიცხვს ვადარებთ ერთმანეთს
#მინიჭების ოპერატორები = ანიჭებს მნიშვნელობას მაგალითად num = 20 ცვლადებს ვანიჭებთ მნიშვნელობას



#დავალება 2

num1=int (input())
num2=int (input())

print(num1==num2)
print(num1>num2)
print(num1<num2)


#დავალება 3
#სტრინგების დამატებას კონკატინაცია ეწოდება
name="dachi"
surname="arqania"
car_brand="BMW"
basketball_player="kobi briant"
programing_language="python"
print(name + surname + car_brand + basketball_player + programing_language)



#დავალება 4

name="dachi"
num=140
float_number=17.0
boolean= True and False

print(type(name))
print(type(num))
print(type(float))
print(type(boolean))



#დავალება 5
num1 = float(input("write first number: "))
num2 = float(input("write second number: "))
num3 = float(input("write third number: "))
num4 = float(input("write forth number: "))
num5 = float(input("write fifth number: "))

# საშუალო არითმეტიკულის გამოთვლა
average = (num1 + num2 + num3 + num4 + num5) / 5


#დავალება 6

name1="dachi"
name2="giorgi"

print(name1 == name2)


#დავალება 7

num1 = "40"
num2 = "25"
num3 = "15"
num4 = "20"

int1 = int(num1)
int2 = int(num2)
int3 = int(num3)
int4 = int(num4)
print("რიცხვების ჯამი არის:",int1 + int2 + int3 + int4 )


num1 = 30
num2 = 40
num3 = 50

# რიცხვების სტრინგად გადაყვანა
str1 = str(num1)
str2 = str(num2)
str3 = str(num3)

# ერთ წინადადებაში გამოტანა
result = str1 + str2 + str3
print("შედეგი არის:", result)