 # დავალება 1


# nums = [2,4,1,5,6,9,10]

# biggest = nums[0]

# second_biggest = 0

# for i in nums:
#     if i > biggest:
#         second_biggest = biggest
#         biggest = i
# print(second_biggest)



# sentence = input("choose any sentece: ")

# count = 0
# l = 0
# i = 0

# while i < len(sentence):
#     if sentence[i] != " ":
#         l += 1
#     elif sentence[i] ==  " "  and l > 4:
#         count += 1
#         l = 0
#     i += 1
# print(count)

# 3) მომხმარებელს შემოატანინეთ სიტყვა და გაიგეთ ეს სიტყვა არის თუ არა პალინდრომი - ანუ ეს სიტყვა წინიდანაც და უკნიდანაც თუ ზუსტად
#  იგივენაირად იკითხება. თუ კი მაშინ დაპრინტეთ True,  თუ არა დაპრინტეთ False, გამოიყენეთ for ციკლი, არ გამოიყენოთ slicing - [::-1].


# user = input("type any letter: ")

# letter = ""

# for i in user:
#     letter = i + letter

# print(letter == user)


# 4) შექმენით არეული რიცხვებით სავსე გრძელი სია და 2 ცარიელი სია, ერთ სიაში ჩააგდეთ ყველა ის რიცხვი რომელიც არის ლუწი და 
#  დგას კენტ ინდექსზე, ხოლო მეორე სიაში ჩააგდეთ ყველა ის რიცხვირომელიც არის ლუწი და დგას კენტ ინდექსზე, გამოიყენეთ for ციკლი.

# nums = [1,2,3,4,5,6,7,8,9,11,22]

# empty = []

# empty2 = []

# for i in nums:
#     if i % 2 == 0 and nums.index(i) % 2 == 1:
#         empty.append(i)
#     elif i % 2 == 1 and nums.index(i) % 2 == 0:
#         empty2.append(i)

# print("რიცხვები რომელიც დგას კენტს ინდექსზე და არის ლუწი", empty)

# print("რიცხვები რომელიც დგას ლუწ ინდექსზე და არის კენტი", empty2)




# 5) შექმენით ყველანაირი მონაცემთა ტიპების ელემენტებით სავსე სია, ამოშალეთ ყველა დუპლიკატები 
#  ყველაფერი რაც მეორდება 2-ზე მეტჯერ, გამოიყენეთ remove() ფუნქცია და while ციკლი.
# ragacaeebi = [6000, 2.2, 2.2, True, "dachi", "dachi", True]

# i = 0

# while i < len(ragacaeebi):
#     if everything.count(ragacaeebi[i]) > 1:
#         everything.remove(ragacaeebi[i])
#     else:
#         i += 1

# print(ragacaeebi)


# 6)  მომხმარებელს შემოატანინეთ წინადადება და დაპრინტეთ ამ წინადადებაში მყოფი 
# ყველაზე გრძელი სიტყვა, გამოიყენეთ while ციკლი, არ გამოიყენოთ max() ფუნქცია.

# მომხამრებელი = input("type any letter:")
# word = ""
# word2 = ""


# i = 0
# while i < len(მომხამრებელი):
#     if მომხამრებელი[i] != " ":
#         word2 += მომხამრებელი[i]
#     else:
#         if len(word2) > len(word):
#             word = word2
#         word2 = " "
#     i += 1
# print("longest word is:" , word)

        

    

  


        
    
    
    














