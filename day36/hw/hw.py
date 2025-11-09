














# 1)
# word = input("შეიყვანე სიტყვა: ")
# for i in range(len(word)):
#     if word[i] == "e" or word[i] == "e":
#         break
#     print(word[i])



# 2) 
# sentence = input("შეიყვანე წინადადება: ")
# if "bad" in sentence:
#     print("აკრძალული სიტყვა!")
# else:
#     print("ყველაფერი რიგზეა")


# 3) 
text = input("შეიყვანე წინადადება: ")
for i in range(len(text)):
    if text[i] == "":
        continue
    print(text[i])



# # 4) 
# text2 = input("შეიყვანე წინადადება: ")
# vowels = 'aeiouAEIOU'
# for i in range(len(text2)):
#     if text2[i] in vowels:
#         continue
#     print(text2[i])

# 
# # 5) 
# start = int(input("შეიყვანე პირველი რიცხვი: "))
# end = int(input("შეიყვანე მეორე რიცხვი: "))
# for i in range(start, end + 1):
#     if i % 15 == 0:
#         print(i)
#         break



# # 6) უსასრულო while loop
# while True:
#     answer = input("გაიწერე რაღაც: ")
#     if answer == "python is best":
#         break
#     print("you should learn python")

# 

# # 7) 
# start2 = int(input("შეიყვანე პირველი რიცხვი: "))
# end2 = int(input("შეიყვანე მეორე რიცხვი: "))
# count = 0
# for i in range(start2, end2 + 1):
#     if i % 3 == 0:
#         count += 1
#         if count == 3:
#             print(i)
#             break