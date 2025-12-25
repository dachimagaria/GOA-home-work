
# 1) შექმენით რიცხვებით სავსე სია და ახალ სიაში ჩააგდეთ ყველა რიცხვი გამრავლებული 2-ზე. დაპრინტეთ ახალი სია.


# numbers = [1, 2, 3, 4, 5, 6]

# new_numbers = []

# for num in numbers:
#     new_numbers.append(num * 2)

# print(new_numbers)

    


# 2) შექმენით სახელებით სავსე სია, მომხმარებელს შემოატანინეთ რაიმე რიცხვი, და ამ რიცხვის ინდექსზე ჩაამატეთ სახელი "ნიკა" თქვენს სიაში.


# names = ["გეგა", "დაჩი", "ლუკა", "რეზი"]


# index = int(input("შეიყვანე რიცხვი (ინდექსი): "))


# names.insert(index, "ნიკა")


# print(names)


# 3) შექმენით string წინადადების ცვლადი, ამ წინადადებიდან დაპრინტეთ მხოლოდ ხმოვანი ასოები.
# sentence = "Programming is awesome"

# vowels = "aeiouAEIOU"


# for char in sentence:
#     if char in vowels:
#         print(char)


# 4) შექმენით სტრინგებით სავსე სია, წაშალეთ ის სტრინგ მონაცემთა ტიპის ელემენტები რომლებიც არიან 4-ზე მეტი სიგრძეში ან დგანან კენტ ინდექსზე. გამოიყენეთ remove() ფუნქცია.

my_list = ["rezi", "dachi", "gega", "luka"]
for i in range(len(my_list)-1, -1, -1):
    if len(my_list[i]) > 4 or i % 2 != 0:
        my_list.remove(my_list[i])
print(my_list)


# 5) შექმენით რიცხვებით სავსე სია, გამოითვალეთ რიცხვების საშუალო არითმეტიკული - რიცხვების ჯამი გაყოფილი რიცხვების რაოდენობაზე

# numbers = [10, 20, 30, 40, 50]


# total = 0
# for number in numbers:
#     total += number


# count = len(numbers)


# average = total / count

# print("ჯამი:", total)
# print("საშუალო არითმეტიკული:", average)
