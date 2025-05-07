import string

# Отримуємо вхід від користувача
user_input = input("Введіть дві літери через дефіс (наприклад, a-c): ")

# Розбиваємо введення
start, end = user_input.split('-')


all_letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Знаходимо індекси  букв
start_index = all_letters.index(start)
end_index = all_letters.index(end)

# Виводимо символи між ними
result = all_letters[start_index:end_index + 1]
print(result)
