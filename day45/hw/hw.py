# 1)
names = ["dachi" , "rezi" , "gega"]
fruits = ["grape" , "banana"]
names.extend(fruits)
print(names)


# 2) 
numbers = [10, 20, 30]
num = [40, 50]
numbers.extend(num)
print(numbers)


# 3) 
names = ["dachi" , "rezi" , "gega"]
names.reverse()
print(names)


# 4) 
numbers = [10, 20, 30, 90, 74834, 768958, 90909, 1234637454678, 90, 90, 100, 100, 7, 8, 7, 8, 7]
print(numbers.count(7))


# 5)
letters = ["a","b","a","c"]
print(letters.count("a"))


# 6) 
name = ["goga", "givia", "giorgi", "nika", "givia", "nika", "saba", "goga", "givia"]
print(name.index("saba"))


# 7)
lst = ["red","green","blue"]
print(lst.index("blue"))


# 8) 
numbers = [1, 2, 3, 4, 5, 6]
nums = [7, 8, 9]
numbers.extend(nums)
print(numbers)


# 9)
foods = ["შაურმა", "ღომი", "კარგი მწვადი", "ხინკალი", "ქათმის ჩახოხბილი", "ინდაურის ხორცი", "ქათმის ხორცი"]
foods.reverse()
print(foods)


# 10)
cities = ["თბილისი", "ბათუმი", "ქუთაისი", " rusTavi", "ფოთი", "გორი", "ზუგდიდი", "გლდანი", "სენაკი", "სენაკი"]
print(cities.index("თბილისი"))


# 11) 
animals = ["cat","dog","cat","cow"]
print(animals.count("cat"))


# 12) 
fruits = ["apple", "banana"]
to_be_added_fruit = "grape"
fruits.append(to_be_added_fruit)
print(fruits)


# 13) 
numbers = [1, 2, 3]
nums = [4, 5]
numbers.extend(nums)
print(numbers)


# 14) 
names = ["goga", "saba"]
names.insert(2, "luka")
print(names)


# 15) 
items = ["pen", "pencil", "eraser"]
items.pop(2)
print(items)


# 16) 
colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)


# 17) 
foods = ["bread", "milk"]
if len(foods) == 2:
    foods.append("cheese")
else:
    foods.append("meat")
print(foods)


# 18) 
nums = [10, 20, 30]
num = int(input("Enter a number: "))
if num in nums:
    print("Already in list")
else:
    nums.append(40)
print(nums)


# 19) 
letters = ["a", "b", "c"]
letter = input("Enter a letter: ")
mid_index = len(letters)
letters.insert(mid_index, letter)
print(letters)


# 20) 
values = [1, 2, 3, 4]
index = int(input("Enter an index: "))
if 0 <= index < len(values):
    values.pop(index)
else:
    print("Index out of range")
print(values)


# 21) 
pets = ["cat", "dog", "hamster"]
pet_name = input("Enter a pet name: ")
if pet_name in pets:
    pets.remove(pet_name)
    print("Removed")
else:
    print("Not found")
print(pets)


# 22) 
a = [5, 5, 7, 7, 8, 9, 9, 9, 9, 1, 1, 1, 7, 8]
num = int(input("Enter a number: "))
if num in a:
    print("Count:", a.count(num))
else:
    a.append(num)
print(a)


# 23) 
queue = ["first", "second"]
new_item = input("Enter a new item: ")
queue.insert(0, new_item)

if len(queue) > 5:
    queue.pop()
    print(queue)
else:
    print(queue)


# 24) 
nums = [2, 4, 6]
num = int(input("Enter a number: "))
if num > 0:
    nums.append(num)
else:
    print("Only positive allowed")
print(nums)


















