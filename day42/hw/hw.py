








# 1) შექმენი სია ხილებზე და დაამატე მასში კიდევ 2 ხილი extend() ფუნქციით.

# names = ["dachi" , "rezi" , "gega"]

# fruits = ["grape" , "banana"]

# names.extend(fruits)
# print(names)


# 2) შექმენი სია numbers და დაამატე მასში [40, 50] extend()-ით.
# numbers =[10 , 20 , 30]
# num = [40 , 50]
# numbers.extend(num)
# print(numbers)

# 3) შექმენი სია names და შეაბრუნე reverse()-ით.

# names = ["dachi" , "rezi" , "gega"]
# names.reverse()
# print(names)


# 4) შექმენი სია სახელად nums და დათვალე რამდენი ცალი 5 არის მასში count()-ით.
# numbers =[10 , 20 , 30 , 90 ,74834 ,768958 ,90909, 1234637454678 , 90 , 90 , 100 , 100 , 7 , 8 , 7 ,8 ,7]
# print(numbers.count(7))


# 5) შექმენი letters = ["a","b","a","c"] და დაბეჭდე რამდენი ცალი "a" არის ჩვენს სიაში.
# letters = ["a","b","a","c"]
# print(letters.count("a"))


# 6) შექმენი სია სახელად names და იპოვე "saba"-ს ინდექსი index()-ით.
# name = ["goga", "givia", "giorgi", "nika", "givia", "nika", "saba", "goga", "givia"]
# print(name.index("saba"))

# 7) შექმენი list = ["red","green","blue"] და იპოვე რომელ ინდექსზე დგას "blue". გამოიყენე შესაბამისი ფუნქცია.
# list = ["red","green","blue"]
# print(name.index("blue"))

# 8) შექმენი სია სახელად nums და დამატე მასში extend()-ით [7, 8, 9].
# numbers =[1 , 2 , 3 , 4 , 5 , 6]
# nums = [7 , 8 , 9]
# numbers.extend(nums)
# print(numbers)

# 9) შექმენი სია სახელად foods და დააბრუნე შებრუნებული სია.
# foods = ["შაურმა" , "ღომი" , "კარგი მწვადი" , "ხინკალი" , " ქათმის ჩახოხბილი" , "ინდაურის ხორცი" , "ქათმის ხორცი"]
# foods.reverse()
# print(foods)

# 10) შექმენი სია cities და იპოვე რომელ ინდექსზე დგას "tbilisi".
# cities = ["თბილისი", "ბათუმი", "ქუთაისი", "რუსთავი", "ფოთი", "გორი", "ზუგდიდი", "გლდანი", "სენაკი", "სენაკი"]
# print(cities.index("თბილისი"))

# 11) შექმენი animals = ["cat","dog","cat","cow"] და დაითვალე ამ სიაში რამდენი "cat" არის.
# animals = ["cat","dog","cat","cow"]
# print(animals.count("cat"))

# 12)შექმენი სია fruits = ["apple", "banana"] და append ფუნქციით დაამატე "grape". დაბეჭდე სია.
# fruits = ["apple", "banana"]
# to_be_added_fruit ="grape"
# fruits.append(to_be_added_fruit)
# print(fruits)

# 13)შექმენი სია numbers = [1, 2, 3] და extend()-ით დაუმატე [4, 5]. დაბეჭდე სია.

# numbers = [1, 2, 3]
# nums = [4 , 5]
# numbers.extend(nums)
# print(numbers)

# 14)შექმენი სია names = ["goga", "saba"] და insert()-ით ჩასვი "luka" პირველ ინდექსზე. დაბეჭდე სია.
# names = ["goga", "saba"]
# names.insert( 2,"luka" )
# print(names)

# 15)შექმენი სია items = ["pen", "pencil", "eraser"] და pop()-ით წაშალე ბოლო ელემენტი; დაბეჭდე განახლებული სია.
# items = ["pen", "pencil", "eraser"]
# items.pop(2)
# print(items)

# 16)შექმენი სია colors = ["red", "green", "blue"] და remove()-ით წაშალე "green". დაბეჭდე შედეგი.
# colors = ["red", "green", "blue"]
# colors.remove("green")
# print(colors)

# 17)შექმენი სია foods = ["bread", "milk"]. შეამოწმე სიაში 2 ელემენტია თუ მეტი — თუ ორია, append()-ით დაამატე "cheese", შემდეგ დაბეჭდე სია, სხვა შემთხვევაში append()-ით დაამატე "meat" და დაბეჭდე სია.
# foods = ["bread", "milk"]
# if len(foods) == 2:
#     foods.append("cheese")
# else:
#     foods.append("meat")
# print(foods)

# 18)შექმენი სია nums = [10, 20, 30]. მომხმარებელს შემოატანინე მთელი რიცხვი. თუ რიცხვი nums სიაშია, დაბეჭდე "Already in list", თუ არა — append()-ით დაამატე 40 და დაბეჭდე სია.
# nums = [10, 20, 30]
# num = int(input("Enter a number: "))
# if num in nums:
#     print("Already in list")
# else:
#     nums.append(40)
# print(nums)

# 19)შექმენი სია letters = ["a", "b", "c"]. მომხმარებელს შემოატანინე ასო, შემდეგ insert()-ით ჩასვი ის სიის შუაში (ცენტრალურ ინდექსზე). დაბეჭდე სია.
# letters = ["a", "b", "c"]
# letter = input("Enter a letter: ")
# mid_index = len(letters)
# letters.insert(mid_index, letter)
# print(letters)


# 20)შექმენი სია values = [1, 2, 3, 4]. მომხმარებელს შემოატანინე ინდექსი. თუ ინდექსი სიის ფარგლებშია, pop()-ით ამოშალე შესაბამისი ელემენტი; თუ არა, დაბეჭდე "Index out of range". ბოლოს დაბეჭდე სია.

# values = [1, 2, 3, 4]
# index = int(input("Enter an index: "))
# if 0 <= index < len(values):
#     values.pop(index)
# else:
#     print("Index out of range")
# print(values)


# 21)შექმენი სია pets = ["cat", "dog", "hamster"].  მომხმარებელს შემოატანინე შინაური ცხოველის სახელი. თუ იგი არის სიის შიგნით, remove()-ით ამოშალე და დაბეჭდე "Removed", თუ არა — დაბეჭდე "Not found" და სია უცვლელი დატოვე; საბოლოოდ დაბეჭდე სია.

# pets = ["cat", "dog", "hamster"]
# pet_name = input("Enter a pet name: ")
# if pet_name in pets:
#     pets.remove(pet_name)
#     print("Removed")
# else:
#     print("Not found")
# print(pets)

# 22)შექმენი სია a = [5, 5, 7]. მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი არის სიის ელემენტი, დაბეჭდე რამდენჯერ არის სიაში - count() ფუნქციის გამოყენებით. სხვა შემთხვევაში append()-ით ჩასვი ის სიაში და დაბეჭდე სია.
# a = [5, 5, 7 , 7 , 8 , 9 , 9 , 9 , 9 ,1 , 1 , 1 , 7 , 8]
# num = int(input("Enter a number: "))
# if num in a:
#     print("Count:", a.count(num))
# else:
#     a.append(num)
# print(a)


# 23)შექმენი სია queue = ["first", "second"].  მომხმარებელს შემოატანინე ახალი ელემენტი და insert()-ით ჩასვი სიის დასაწყისში. შემდეგ if-ით შეამოწმე სიის სიგრძე — თუ უფრო დიდია 5-ზე, pop()-ით ამოშალე ბოლო ელემენტი; ბოლოს დაბეჭდე სია, თუ არ არის 5-ზე მეტი დაბეჭდე შებრუნებული სია.
# queue = ["first", "second"]
# new_item = input("Enter a new item: ")
# queue.insert(0, new_item)
# if len(queue) > 5:
#     queue.pop()
#     print(queue)
# else:
#     print(queue)


# 24)შექმენი სია nums = [2, 4, 6].  მომხმარებელს შემოატანინე რიცხვი. თუ რიცხვი დადებულია, append()-ით დაამატე; თუ 0-ია ან ნაკლებია ნულზე, დაბეჭდე "Only positive allowed". ბოლოს დაბეჭდე სია.
# nums = [2, 4, 6]
# num = int(input("Enter a number: "))
# if num > 0:
#     nums.append(num)
# else:
#     print("Only positive allowed")
# print(nums)


# 25) შექმენი სია mix = ["x", "y", "z"]. extend()-ით დაუმატე [1, 2, 3]. შემდეგ მომხმარებელს შემოატანინე ასო; თუ ეს ასო არის სიაში, remove()-ით წაშალე პირველად როცა შეგხვდება და დაბეჭდე "Removed", თუ არა — დაბეჭდე "No such element". ბოლოს დაბეჭდე სია.
# mix = ["x", "y", "z"]
# mix.extend([1, 2, 3])
# char = input("Enter a letter: ")
# if char in mix:
#     mix.remove(char)
#     print("Removed")
# else:
#     print("No such element")
# print(mix)





