import random


lst = [random.randint(1, 100) for _ in range(random.randint(3, 10))]


new_list = [lst[0], lst[2], lst[-2]]

# Вивід результату
print("Початковий список:", lst)
print("Новий список:", new_list)