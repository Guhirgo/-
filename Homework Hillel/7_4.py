def common_elements():
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}
    return multiples_of_3 & multiples_of_5  # перетин множин


assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print('ОК')