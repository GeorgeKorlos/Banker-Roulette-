names = input().split(", ")

import random

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
pay = names[random_choice]
print(f"{pay} is going to buy the meal today.")
