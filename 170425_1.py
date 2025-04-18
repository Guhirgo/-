numbers = int(input("Введіть число з 5 цифр: ") )

numbers1 = numbers % 10
numbers2 = (numbers // 10) % 10
numbers3 =(numbers // 100) % 10
numbers4 = (numbers // 1000 ) % 10
numbers5 = numbers // 10000

reversed_number = numbers1 * 10000 + numbers2 * 1000 + numbers3 * 100 + numbers4 * 10 + numbers5
print("Перевернуте число: ", reversed_number)