numbers = int(input("Введіть чотиризначне число: "))

numbers1 = numbers // 1000
numbers2 = (numbers // 100) % 10
numbers3 = (numbers // 10 ) % 10
numbers4 = numbers % 10

print(numbers1)
print(numbers2)
print(numbers3)
print(numbers4)