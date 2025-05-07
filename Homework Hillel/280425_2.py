
examples = [
    [0, 1, 7, 2, 4, 8],
]

for lst in examples:
    if not lst:
        result = 0
    else:
        sum_even_index = sum(lst[::2])
        result = sum_even_index * lst[-1]
    print(result)
