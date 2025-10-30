momxmarebeli = input("choose any word: ")

print(len(momxmarebeli))

for i in range(len(momxmarebeli)):
    print(momxmarebeli[i])

words = ["apple", "banana", "kiwi", "grape", "melon"]

for i in range(len(words)):
    print("სიტყვა:", words[i])
    print("სიმბოლოების რაოდენობა:", len(words[i]))
    
    if len(words[i]) % 2 == 0:
        print("ლუწია")
    else:
        print("კენტია")
    print()