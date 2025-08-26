# ---------------- 1 ----------------
num = float(input("Enter a number: "))

if num > 0:
    print("This number is positive")
elif num < 0:
    print("This number is negative")
else:
    print("This number is zero")


# ---------------- 2 ----------------
age = int(input("\nEnter your age: "))

if age < 0:
    print("Invalid info")
elif 0 <= age <= 12:
    print("You are a child")
elif 13 <= age <= 19:
    print("You are a teenager")
elif 20 <= age <= 64:
    print("You are an adult")
elif 65 <= age <= 120:
    print("You are elderly")
else:
    print("You are a guru or a wizard")


# ---------------- 3 ----------------
correct_password = "1234"   # You can put your own password here
tries = 0

while True:
    guess = input("\nGuess the password (or type 'nah strong password' to quit): ")
    tries += 1

    if guess == correct_password:
        print(f"Congratulations! Password is correct. Number of tries: {tries}")
        break
    elif guess == "nah strong password":
        print(f"You quit the game. Number of tries: {tries}")
        break
    else:
        print("Wrong password, try again.")


# ---------------- 4 ----------------
a = float(input("\nEnter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

print("The largest number is:", max(a, b, c))


# ---------------- 5 ----------------
day_num = int(input("\nEnter a number between 1 and 7: "))

if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("I don’t know what day that is")


# :regional_indicator_n: :regional_indicator_i: :regional_indicator_g: :regional_indicator_a: 






















