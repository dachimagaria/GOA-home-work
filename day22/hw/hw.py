# დავალება 1
# Index არის ელემენტის მდებარეობის ნომერი სიაში, სტრინგში ან სხვა მონაცემთა სტრუქტურაში.
# ინდექსირება იწყება 0-დან. მაგ: list = [10,20,30] → list[0] = 10, list[1] = 20.
# მას ვიყენებთ კონკრეტული ელემენტის მისაღებად ან შესაცვლელად.



#დავალება 2
nums = [4,6,1,5,9,8,4]

print(nums[0] + nums[1])  
print(nums[1] - nums[0])   
print(nums[4] + nums[2])   
print(nums[5] + nums[1] + nums[0]) 
print(nums[6] - nums[2])   
print(nums[5] - nums[4])   
print(nums[3] + nums[4] + nums[6])





#დავალება 3
names = ["Nika","Luka","Ana","Gio","Saba","Mari","Dato","Nino","Lile","Sandro"]

print(names[5])  
print(names[9])  
print(names[3])  
print(names[7])  
print(names[1])  


#დავალება 4
fruits = ["ვაშლი", "ბანანი", "ატამი", "საზამთრო", "მსხალი"]


for f in fruits:
    print(f)


i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# დავალება 5
data = [1, "hello", 3.5, "test", 7, True, "bye"]

data[3] = "vashli"   
data[6] = "msxali"   
data[4] = "atami"    
print(data)


#დავალება 6



result = True and False or False and True or False and False or True
print(result)  








#დავალება 7
animals = ["dog", "cat", "tiger", "lion", "cow"]

if animals[3] == "lion":
    print("there is lion on index 3")
else:
    print("there is no lion on index 3")





















#დავალება 8

basket = ["ვაშლი", "ბანანი", "საზამთრო", "ატამი", "ყურძენი"]


print(basket[0])


print(basket[2])


basket[1] = "ფორთოხალი"


print(basket[0])
print(basket[1])
print(basket[2])
print(basket[3])
print(basket[4])
























#დავალება 9

letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

print(letters[2])              
print(letters[4], letters[5])  
print(letters[-1])             

print(letters[6] + letters[7] + letters[6] + letters[7])  
print(letters[2] + letters[3] + letters[4] + letters[5])  
print(letters[2] + letters[3] + letters[2] + letters[0])  



#დავალება 10

letters = ["ა", "ბ", "გ", "ო", "ლ", "ა", "მ", "ა", "ტ", "ე"]

letter = letters[4]
if letter == "ლ":
    print("სწორია! ასო ლ ა")
else:
    print("არასწორია, სცადე თავიდან")


last = letters[-1]
if last == "ე":
    print("საიდუმლო სიტყვა იწყება სწორად")
else:
    print("საიდუმლო სიტყვა არასწორია")


word = letters[2] + letters[-1] + letters[4] + letters[5]
if word == "გელა":
    print("გაარტყი სახელი!")
else:
    print("შტერი ხარ!დ")












#დავალება 11

words = ["სახლი", "მზიანი", "კომპიუტერი", "სკოლა", "სათამაშო", "ქარი"]

n = int(input("შეიყვანე ინდექსი: "))
print("შენ აირჩიე:", words[n])















