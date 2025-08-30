



num1 = int(input("enter first number"))
num2 = int(input("enter second number"))
num3 = int(input("enter third number"))


if num1== num2 ==num3:
    print("all number equal")
elif num1==num2:
    print("num1 and num2 is equal")
elif num1==num3:
    print("num1 and num3 is equal")
elif num2==num3:
    print("num2 and num3 is equal")
else:
    print("all number is not equal")




month = int(input("Enter a number from 1 to 12: "))

if month in (12, 1, 2):
    print("Winter")
elif month in (3, 4, 5):
    print("Spring")
elif month in (6, 7, 8):
    print("Summer")
elif month in (9, 10, 11):
    print("Fall")
else:
    print("Invalid number!")



name = input("enter your name")

if name =="admin":
    password = input ("enter admin password pls")
    if password == "adminpassword123":
        print("hello admin")
    else:
        print("Access denied")
else:
    print("hello, user")




















