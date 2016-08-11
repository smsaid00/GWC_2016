import random

menu_adj1 = ["Gooey", "Spicy", "Mild", "Classic"]
menu_adj2 = ["Smoked", "Homemade", "Deep-fried", "Cream"]
actual_food = ["Guava", "Lamb", "Salmon", "Cinnamon Rolls"]

menu_adj1_length  = len(menu_adj1)
menu_adj2_length = len(menu_adj2)
actual_food_length = len(actual_food)

random_index = random.randint(0, menu_adj1_length)

# print(menu_adj1[random_index])

for i in menu_adj1 and menu_adj2 and actual_food:
    print(i)
