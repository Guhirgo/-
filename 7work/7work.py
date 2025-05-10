from enum import unique

some_list = [55,54,5554,45,"lol"]
some_list2 = [55,54,5554,455554,"lol"]

some_iterable = "sdfncbxvzs123124314"

target_dict = {}

for elem in some_list:
    target_dict[elem] = None
print(target_dict.keys())

unique_elem = set(some_list)

print(unique_elem)