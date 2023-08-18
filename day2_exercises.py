# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

digit1 = two_digit_number[0]
digit2 = two_digit_number[1]

sum = int(digit1)+int(digit2)


print(sum)

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = (float(weight)) / (float(height)**2)
print(round(bmi))

print(round(8/3))

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
target_age = 90
age_int = int(age)
days_to_90 = (target_age*365)-(age_int*365)
weeks_to_90 = (target_age*52) - (age_int*52)
months_to_90 = (target_age*12) - (age_int*12)
print(f"You have {days_to_90} days, {weeks_to_90} weeks, and {months_to_90} months left.")



