import random

plants = ["Camellia", "Shrubs", "Maple Tree" ]
# print(random_plants)
print(plants[1])

# for plant in random_plants:
#     print(plant)
#
# for i in random_plants:
#         print (i)

shoe_brands = ["Nike", "Vans", "Keds", "Skechers"]
shoe_brands_length=len(shoe_brands)
randombrand=random.randint(0,shoe_brands_length-1)
print(shoe_brands[randombrand])
