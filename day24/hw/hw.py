# 1)შექმენი სია 7 რიცხვით. 
my_list = [1, 2, 3, 4, 5, 6, 7]
# დაბეჭდე პირველი და ბოლო ელემენტების ნამრავლი ისე, რომ ორივეჯერ უარყოფითი ინდექსი გამოიყენო.
print(my_list[-7])
print(my_list[-1])
# დაბეჭდე მესამე ელემენტი მარცხნიდან და მესამე ელემენტი მარჯვნიდან (უარყოფითიინდექსის გამოყენებით).
print(my_list[2])
print(my_list[-3])


# 2)შექმენი სია "apple", "banana", "cherry", "grape", "kiwi", "orange".
fruits = ["apple", "banana", "cherry", "grape", "kiwi", "orange"]
# დაბეჭდე შუა 2 ელემენტი (ორივე(დადებითი და უარყოფითი)) ინდექსით.
print(fruits[2:4])
print(fruits[-4:-2])



# 3)
# შექმენი [3,4,5,6,7,1,2,9,8,11]
numbers = [3, 4, 5, 6, 7, 1, 2, 9, 8, 11]

# მომხმარებელს შემოატანინე ერთი ინდექსი(რიცხვი) 0 დან 10 მდე.
index = int(input("შეიყვანეთ ინდექსი 0 დან 9 მდე: "))

# თუ მომხმარებლის ინდექსი დადებითია → დაბეჭდე ის ელემენტი
if 0 <= index <= 9:
    print(numbers[index])
else:
    print("you entered negative or more than 10 number")

# 4)შექმენით სია ["dog" ," most" ,"is" ,"angry" ,"running"  , "forest", "fast", "in" , "cat" ,"human", "very"]
words = ["dog", "most", "is", "angry", "running", "forest", "fast", "in", "cat", "human", "very"]
# უარყოფითი ინდექსები

words = ["cat", "is", "very", "angry"]

print(words[0], words[1], words[2], words[3])




sentence = ["dog", "is", "running", "in", "forest", "very", "fast"]

print(sentence[-7], sentence[-6], sentence[-5], sentence[-4], sentence[-3], sentence[-2], sentence[-1])




print(sentence[0], sentence[1], sentence[2], sentence[3], sentence[4], sentence[5], sentence[6])


# 5)
# ცხოველების სია
animals = ["dog", "cat", "horse", "cow", "sheep", "goat"]

# შემოტანა მომხმარებლისგან
index = int(input("შეიყვანე ინდექსი (0-დან 5-მდე): "))

# შემოწმება
if animals[index] == "cat":
    print("შენ აირჩიე კატა")
elif animals[index] == "goat":
    print("შენ აირჩიე თხა")
else:
    print("სხვა ცხოველი აირჩიე")





# 6)
# შექმენი სია 6 ქალაქით.
# მომხმარებელი შემოიტანს ორ ინდექსს(რიცხვს).
cities = ["Tbilisi", "Batumi", "Kutaisi", "Rustavi", "Zugdidi", "Gori"]

first_index = int(input("შეიყვანეთ პირველი ინდექსი 0 დან 5 მდე: "))
second_index = int(input("შეიყვანეთ მეორე ინდექსი 0 დან 5 მდე: "))

if first_index < second_index:
    print(cities[first_index], cities[second_index])

elif first_index > second_index:
    print("შეცვალე ინდექსები ადგილებით")
    print(cities[second_index], cities[first_index])

else:
    print("ორივე ერთია")
    print(cities[first_index])


# 7)მომხმარებელი შემოიტანს სიტყვას.
word = input("შეიყვანეთ სიტყვა: ")

if word[0] == "a":
    print("სიტყვა იწყება a-თი")
elif word[-1] == "z":
    print("სიტყვა მთავრდება z-ით")
else:
    print("სიტყვა არც a-თი იწყება და არც z-ით მთავრდება")


# 8)დავალება 4
word = input("შეიყვანეთ სიტყვა: ")

if word[0] == word[-1]:
    print("პირველი და ბოლო ერთნაირია")
else:
    print("პირველი და ბოლო განსხვავებულია")




# 9)შექმენი ცვლადი სადაც შეინახავთ შემდეგ ასოებს ---> "agivorsbgitr"
letters=("agivorsbgitr")

# "goga"
print(letters[1] + letters[0] + letters[1] + letters[0])

# "saba"
print(letters[6] + letters[0] + letters[1] + letters[0])

# "bativar"
print(letters[7] + letters[0] + letters[4] + letters[1] + letters[9] + letters[1] + letters[4] + letters[5])

# 10
name = 'giorgi'




# შენი დავალებააა რომ for დდა while loop ის დახმარებით გამოიტანო ამ სტრინგის თითეული ასო ცალ ცალკე


name = 'giorgi'

for i in range(6):
    print(name[i])

































































