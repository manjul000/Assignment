#18} eligibility for voting

age = int(input("Please enter your age : "))

while True:
    if age > 0 and age < 125:
        break
    elif age < 0 or age > 125:
        age = int(input("Please enter a valid age : "))
    elif age == 0:
        age = int(input("Please enter a valid age : "))

if age < 18:
    print("You aren't eligible to vote.")
elif age > 18:
    print("You are elgible to vote.")
elif age == 18:
    print("You are eligible to vote.")