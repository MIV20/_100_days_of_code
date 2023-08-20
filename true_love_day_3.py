# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = name1 + name2

# for letter in combined_name:
t_count = combined_name.count("t")
r_count = combined_name.count("r")
u_count = combined_name.count("u")
e_count = combined_name.count("e")
tr_count = t_count + r_count + u_count + e_count

l_count = combined_name.count("l")
o_count = combined_name.count("o")
v_count = combined_name.count("v")
el_count = combined_name.count("e")
lv_count = l_count + o_count + v_count + el_count

score= int(str(tr_count) + str(lv_count))


if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
