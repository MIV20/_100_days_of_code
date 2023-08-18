# print("***WELCOME TO THE TIP CALCULATOR***")
# bill_total = int(input("How much is the total bill? $"))
# people_total = int(input("How many people are paying the bill? "))
# input("Is tip already included? Yes or No")

print("***WELCOME TO THE TIP CALCULATOR***")
bill_total = int(input("How much is the total bill? $"))
people_total = int(input("How many people are paying the bill? "))
<<<<<<< HEAD
tip = int(input("What tip percentage do you want to leave 18 ,20 or 25? %"))
percent_tip = tip/100
per_person_check = round((bill_total/people_total) * (percent_tip+1), 2)
print(f"Each person should pay ${per_person_check}.")
=======
tip = int(input("What tip percentage do you want to leave 10 ,12 or 15? %"))
percent_tip = tip/100
per_person_check = round((bill_total/people_total) * (percent_tip+1), 2)
print(f"Each person should pay ${per_person_check}.")
>>>>>>> origin/master
