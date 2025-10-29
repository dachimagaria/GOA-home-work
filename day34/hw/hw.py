
cities = ["Tbilisi", "Batumi", "London", "NewYork", "Paris", "Amsterdam"]
for i in range(len(cities)):
    if len(cities[i]) > 6:
        print(cities[i])


words = ["internationalization", "responsibility", "friendship", "communication", "mathematics"]
for i in range(len(words)):
    if len(words[i]) % 15 == 0:
        print(words[i])


numbers = [5, 10, 15, 20, 25, 30]
count = 0
for i in range(0, len(numbers)):   
    count += 1
print("რიცხვების რაოდენობა სიაშია:", count)


words2 = ["apple", "mango", "grape", "banana", "pear"]
for i in range(len(words2)):
    if len(words2[i]) == 5:
        print(words2[i])


sentence = input("შეიყვანე წინადადება: ")
print("სიმბოლოების რაოდენობა:", len(sentence))
count_a = 0
for i in range(len(sentence)):
    if sentence[i] == "a" or sentence[i] == "A":
        count_a += 1
print("წინადადებაში არის", count_a, "'a' ასო.")


strings = ["sun", "elephant", "programming", "AI", "extraordinary"]
longest = ""
for i in range(len(strings)):
    if len(strings[i]) > len(longest):
        longest = strings[i]
print("ყველაზე გრძელი სტრინგია:", longest)
