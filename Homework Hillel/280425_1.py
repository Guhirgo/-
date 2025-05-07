lst = [0, 1, 0, 12, 3]

# всі ненульові елементи
non_zeros = [x for x in lst if x != 0]

 # кількість нулів
zeros = [0] * (len(lst) - len(non_zeros))


lst = non_zeros + zeros

print(lst)  # [1, 12, 3, 0, 0]
