
# 1) 
names = ["Luka", "dachi", "Giorgi", "nika", "Saba", "dato"]
Upper_name = []

for name in names:
    if name[0].isupper():
        Upper_name.append(name)

print(Upper_name)



# 2) 
name_list = ["luka", "saba", "Nika", "dato"]
surname_list = ["BERIDZE", "GOGOLADZE", "KAPANADZE", "MAMALADZE"]

for i in range(len(name_list)):
    name_list[i] = name_list[i].upper()

for i in range(len(surname_list)):
    surname_list[i] = surname_list[i].lower()

full_list = name_list + surname_list
print(full_list)



# 3) სიიდან ამოშლა ის სიტყვები, რომლებიც:
words = ["Hello", "WORLD", "python", "Banana", "Hi", "GamE", "School"]

for w in words[:]:
    if len(w) < 6 or w[-1].isupper():
        words.remove(w)

print(words)



# 4)
floats = [3.5, 12.4, 55.2, 100.1, 9.9, 87.6, 43.3, 7.7, 150.5, 29.9]
filtered = []

for num in floats:
    if 10 < num < 100:
        filtered.append(num)

print(filtered)



# 5) 
cities = ["Tbilisi", "Kutaisi", "Batumi", "Rustavi", "Zugdidi"]
countries = ["Georgia", "France", "Italy", "Spain", "Germany",  "China", "Japan", "India", "Brazil", "Argentina"]
        
index = 1
for city in cities:
    if index <= 4:
        countries.insert(index, city)
        index += 1

print(countries)

