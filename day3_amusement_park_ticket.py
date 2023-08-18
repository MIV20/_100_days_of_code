print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height > 120:
    print("You are tall enough to ride!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $7.")
    elif age <= 18:
        print("Please pay $12.")
    else:
        print("Please pay $17.")
else:
    print("Sorry, you are not tall enough to ride.")