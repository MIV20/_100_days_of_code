# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
final_price = 0
if size == "s":
    final_price += 15
elif size == "m":
    final_price += 20
elif size == "l":
    final_price += 25
else:
    print("Not a valid selection. Options are S, M or L.")

if add_pepperoni == "y":
    if size == "s":
        final_price += 2
    else:
        final_price += 3

if extra_cheese == "y":
    final_price += 1

print(f"Your final bill is ${final_price}.")

