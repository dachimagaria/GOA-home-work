
# 1) 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in nums[:]:
    if num % 2 == 0 or nums.index(num) % 2 == 1:
        nums.remove(num)

print(nums)


# 2) 
words = ["apple", "banana", "cat"]

for w in words[:]:
    words.append(w)

print(words)


# 3) 
text_list = ["hello", "world"]
num_list = [10, 25, 35, 50, 60, 49]

for n in num_list:
    if 20 < n < 50:
        text_list.append(n)

print(text_list)


# 4) 
words = ["apple", "Banana", "car", "Dog", "egg"]

for i in range(len(words)):
    if words[i][0].islower():
        words[i] = words[i].capitalize()

print(words)


# 5) 


# append(x) — ამატებს ერთ ახალ ელემენტს სიის ბოლოში.
# extend(list) — ამატებს სხვა სიის ყველა ელემენტს.
# insert(i, x) — ამატებს ელემენტს კონკრეტულ ინდექსზე.
# remove(x) — შლის სიიდან პირველივე ისეთი ელემენტს რომელიც უდრის x-ს.
# pop(i) — შლის ელემენტს მოცემული ინდექსიდან (ან ბოლოს, თუ ინდექსს არ მივუთითებთ).
# reverse() — შებრუნებს სიას.
# count(x) — ითვლის რამდენჯერ გვხვდება x სიაში.
# index(x) — გვიბრუნებს, რომელი ინდექსზე დგას x.

# სტრინგის ფუნქციები:
# lower() — აქცევს სიტყვას პატარა ასოებად.
# upper() — აქცევს სიტყვას დიდი ასოებად.
# capitalize() — სიტყვას პირველი ასო დიდად, დანარჩენი პატარა.
# startswith(x) — ამოწმებს იწყება თუ არა სიტყვა x-ით.

# for ციკლი:
# გამოიყენება სიის გადასავლელად, ელემენტების შესამოწმებლად,
# ცვლილებების გასაკეთებლად და სხვა ბევრ ქმედებისთვის.

