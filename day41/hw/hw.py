



# 1) დავალება

# append()  -> სიის ბოლოში ამატებს ახალ მნიშვნელობას.
# insert()  -> ამატებს პირველ პარამეტრად გადაცემულ ინდექსზე.
# pop()     -> შლის ბოლო ელემენტს, ან მითითებულ ინდექსზე მდგომს.



# 2) დავალება

numbers = [1, 2, 3, 4, 5]
numbers.append(10)   
print(numbers)




# 3) დავალება

names = ["saba", "kote", "nini"]
names.append("dachi")   
print(names)






# 4) დავალება

names = ["saba", "kote", "luka"]

user_name = input("შეიყვანე სახელი: ")
names.append(user_name)

print(names)






# 5) დავალება

names = ["saba", "kote", "luka", "nini", "gio"]
names.insert(3, "dachi")   
print(names)



# 6) დავალება

my_list = ["a", "b", "c", "d", "e", "f"]

user_name = input("შეიყვანე სახელი: ")
user_index = int(input("შეიყვანე რიცხვი 0-დან 6-მდე: "))

my_list.insert(user_index, user_name)

print(my_list)



# 7) დავალება

fruits = ["apple", "banana"]
fruits.insert(1, "orange")
print(fruits)


# 8) დავალება

names = ["goga", "saba", "luka"]
names.insert(-1, "irakli")   
print(names)

# 9) დავალება

foods = ["bread", "milk", "cheese"]
foods.insert(0, "water")  
print(foods)




# 10) დავალება

numbers = [5, 10, 15]
numbers.pop()   
print(numbers)


# 11) დავალება

fruits = ["apple", "banana", "orange"]
fruits.pop(1)   
print(fruits)



# 12) დავალება

names = ["goga", "saba", "luka"]
names.pop(1)   
print(names)




# 13) დავალება

colors = ["red", "green", "blue", "yellow", "black", "purple"]

colors.pop(0)   
colors.pop(2)   
print(colors)













# 14) დავალება

tems = ["pen", "pencil", "book", "eraser"]

user_index = int(input("შეიყვანე რიცხვი 0-დან 3-მდე: "))
tems.pop(user_index)

print(tems)






# 15) დავალება
fruits = ["apple", "banana", "orange"]
index = fruits.index("banana")
fruits.pop(index)
print(fruits)




# 16) დავალება
nums = [3, 5, 3, 7]
index = nums.index(3)
nums.pop(index)
print(nums)




# 17) დავალება
colors = ["red", "blue", "green"]
index = colors.index("blue")
colors.pop(index)
print(colors)




# 18) დავალება
names = ["goga", "saba", "luka"]
user_name = input("შეიყვანე სახელი: ")
index = names.index(user_name)
names.pop(index)
print(names)









# 19) დავალება
items = ["pen", "pencil", "book", "pencil"]
index = items.index("pencil")
items.pop(index)
print(items)
