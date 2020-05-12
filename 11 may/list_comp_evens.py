import random

a_list = []
list_length = random.randint(0,10)

while len(a_list) < list_length:
    a_list.append(random.randint(1,75))

even_num = [number for number in a_list if number % 2 == 0]

print(a_list)
print(even_num)
