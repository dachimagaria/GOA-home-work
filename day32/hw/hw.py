# 1
for i in range(1, 51):
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")

# 2
for i in range(21):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "იყოფა 3-ზე და 5-ზე")
    elif i % 3 == 0:
        print(i, "იყოფა 3-ზე")
    elif i % 5 == 0:
        print(i, "იყოფა 5-ზე")
    else:
        print(i, "არ იყოფა არცერთზე")

# 3
num = int(input("შეიყვანე რიცხვი: "))
even = 0
odd = 0
for i in range(num + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print("ლუწი რიცხვების რაოდენობა:", even)
print("კენტი რიცხვების რაოდენობა:", odd)

# 4
numbers = [10, 25, 33, 47, 80, 99]
for i in range(len(numbers)):
    if numbers[i] > 50:
        print(numbers[i], "მეტი 50-ზე")
    else:
        print(numbers[i], "ნაკლები 50-ზე")

# 5
total = 0
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
        total += i
print("ლუწი რიცხვების ჯამია:", total)

# 6
words = ["apple", "banana", "avocado", "cherry", "apricot"]
for i in range(len(words)):
    if words[i].startswith("a"):
        print(words[i])

# 7
for i in range(21):
    if i == 0:
        print(i, "ნულია")
    elif i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")

# 8
numbers = [5, 15, 25, 35, 45, 55]
for i in range(len(numbers)):
    if numbers[i] % 5 == 0:
        print(numbers[i])

# 9
word = input("შეიყვანე სიტყვა: ")

for i in range(len(word)):
    print(word[i])

# 10
total = 0
for i in range(1, 11):
    total += i
print("ჯამი არის:", total)