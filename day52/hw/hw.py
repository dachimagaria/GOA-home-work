
words = ["rezi", "dachi", "gega", "basketball"]

i = 0

while i < len(words):
    if words[i] != words[i].lower():
        words.pop(i)
        i += 1
    else:
        words[i] = words[i].upper()

print(words)



text = "DaChiaRKaNia"
list1 = []

i = 0
while i < len(text):
    if text[i] == text[i].upper():
        list1.append(text[i].lower())
    else:
        list1.append(text[i].upper())
    i += 1

print(list1)


names = ["rezi", "GEGA", "nika", "DACHI", "saba"]

list2 = []

for i in names:
    if i == i.lower():
        list2.insert(0, i.upper())
    elif i == i.upper():
        list2.append(i.lower())

print(list2)



cities = ["Tbilisi", "BATUMI", "kutaisi", "rustavi"]

i = 0

while i < len(cities):
    if cities[i] == cities[i].upper():
        cities.pop(i)
    else:
        cities[i] = cities[i].upper()
        i += 1

print(cities)


surnames = ["rezesidze", "ARKANIA", "gabunia", "SAGLIANI"]

i = 0
while i < len(surnames):
    arr = surnames[i]
    if arr == arr.lower():
        surnames.pop(i)
        surnames.insert(i + 1, arr.upper())
        i += 1
    else:
        surnames.pop(i)
        surnames.insert(i - 1, arr.lower())
        i += 1

print(surnames)


text = "HELLOworld"

idk = []

for i in text:
    if i == i.lower():
        idk.append("+")
    elif i == i.upper():
        idk.append("-")


minus = idk.count("-")
i = 0

while i < len(idk):
    if minus % 2 == 0:
        if idk[i] == "+":
            idk.pop(i)
        else:
            i += 1
    else:
        if idk[i] == "-":
            idk.pop(i)
        else:
            i += 1

print(idk)



sentence = "hello world my name is rezi"
words = []

current_word = ""

for i in sentence:
    if i != " ":
        current_word += i
    else:
        words.append(current_word)
        current_word = ""

if current_word != "":
    words.append(current_word)

print(words)
