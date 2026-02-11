
def greet(name):
    print("გამარჯობა,", name + "!")

greet("Dachi")
greet("Giorgi")
greet("Nino")


def sum_numbers(num1, num2):
    print(num1 + num2)

sum_numbers(5, 3)
sum_numbers(10, 20)
sum_numbers(7, 8)



def square(num):
    print(num * num)

square(4)
square(6)
square(9)



def check_age(age):
    if age >= 18:
        print("სრულწლოვანი ხარ")
    else:
        print("არ ხარ სრულწლოვანი")

check_age(20)
check_age(15)
check_age(18)



def string_length(text):
    print(len(text))

string_length("Hello")
string_length("Dachi")
string_length("Python")



def multiply(num1, num2):
    print(num1 * num2)

multiply(3, 4)
multiply(5, 6)
multiply(7, 2)



def check_score(score):
    if score >= 90:
        print("შესანიშნავი ქულა")
    elif score >= 70:
        print("კარგი ქულა")
    elif score >= 50:
        print("დამაკმაყოფილებელი ქულა")
    else:
        print("ჩაჭრილი")

check_score(95)
check_score(75)
check_score(60)
check_score(40)



def even_or_odd(number):
    if number % 2 == 0:
        print("ლუწი")
    else:
        print("კენტი")

even_or_odd(4)
even_or_odd(7)
even_or_odd(10)



def first_letter(name):
    print(name[0])

first_letter("Giorgi")
first_letter("Dachi")
first_letter("Nino")



def average(num1, num2, num3):
    print((num1 + num2 + num3) / 3)

average(10, 20, 30)
average(5, 15, 25)
average(7, 8, 9)
