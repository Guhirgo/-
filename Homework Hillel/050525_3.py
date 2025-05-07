#############################################################
def multiply_digits(n):
    while n > 9:
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
    return n
#############################################################
# Отримуємо число від користувача
number = int(input("Введіть ціле число: "))
result = multiply_digits(number)
print("Результат:", result)