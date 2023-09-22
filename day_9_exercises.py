# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
#                           "Function": "A piece of code that you can easily call over and over again.",
#                           "Loop": "The action of doing something over and over again.",
#                           }
#
# # print(programming_dictionary["Bug"])
#
# programming_dictionary["List"] = "A collection of related entries."
#
# # print(programming_dictionary)
#
# empty_dictionary = {}
#
# # # programming_dictionary = {}
# # print(programming_dictionary)
#
# programming_dictionary["Bug"] = "When you make a mistake in code and the interpreter calls you out."
# # print(programming_dictionary)
#
# # loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "visits": 12},
    "Italy": {"cities_visited": ["Rome", "Florence", "Venice"], "visits": 1},
    "Mexico": {"cities_visited": ["Mexico City", "Cancun", "Playa del Carmen", "Isla Mujeres", "Cabo San Lucas"], "visits": 8},
}

# nesting a dictionary in a list

travel_log_2 = [
    {
    "country":"France",
    "cities_visited": ["Paris", "Lille", "Dijon"], "visits": 12},
    {"country":"Italy",
     "cities_visited": ["Rome", "Florence", "Venice"],
     "visits": 1},
    {"country": "Mexico",
    "cities_visited": ["Mexico City", "Cancun", "Playa del Carmen", "Isla Mujeres", "Cabo San Lucas"],
    "visits": 8},
]

print(travel_log_2)