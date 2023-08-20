
print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ").lower()
final_price = 0
if size == "s":
    final_price += 15
elif size == "m":
    final_price += 20
elif size == "l":
    final_price += 25
else:
    print("Not a valid selection. Options are S, M or L.")

add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
if add_pepperoni == "y":
    if size == "s":
        final_price += 2
    elif size == "m" or "l":
        final_price += 3
    else:
        print("Not a valid selection, choose Y or N.")


extra_cheese = input("Do you want extra cheese? Y or N ").lower()
if extra_cheese == "y":
    final_price += 1
elif extra_cheese == "n":
    final_price += 0
else:
    print("Not a valid selection, choose Y or N.")

print(f"Your final bill is ${final_price}.")

