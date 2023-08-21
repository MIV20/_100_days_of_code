# import random
#
# random_integer = random.randint(1, 10)
# print(random_integer)
#
# random_float = random.random() * 5
# print(random_float)

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲

#Write the rest of your code below this line 👇

import random

def coin_flip():
    flip = random.randint(0,1)
    if flip == 0:
        print("Heads")
    else: print("Tails")
    return random.randint(0,1)

flips = int(input("Amount of flips: "))

total_heads = 0
total_tails = 0

for i in range(flips):
    if (coin_flip() == 0):
        total_heads += 1
    else:
        total_tails += 1

print(f"Total of heads is {total_heads}, while the total of tails is {total_tails}.")

