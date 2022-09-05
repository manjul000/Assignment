# Filter odd number from a list
import random

num_list = []

for i in range (0, 100, 1):
    random_num = random.randint(0, 100)
    num_list.append(random_num)

filtered_list = []
length = len(num_list)

for num in range (0, length, 1):
    val = int(num_list[num])
    if val % 2 == 0:
        filtered_list.append(val)

print(filtered_list)