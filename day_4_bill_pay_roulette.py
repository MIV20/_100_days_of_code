names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

buyer_number = random.randint(0, len(names)-1)
name_of_buyer = names[buyer_number]

print(f"{name_of_buyer} is going to buy the meal today!")


