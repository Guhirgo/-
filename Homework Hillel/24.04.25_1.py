def calculator():
    while True:
        # Запитуємо користувача на введення чисел
        try:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка: введено не число. Спробуйте ще раз.")
            continue

        # Запитуємо користувача на введення операції
        operation = input("Виберіть операцію (+, -, *, /): ")

        # Виконуємо відповідну операцію
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Помилка: Дільник не може бути нулем!")
                continue
            result = num1 / num2
        else:
            print("Невідома операція!")
            continue

        # Виводимо результат
        print(f"Результат: {result}")

        # Перевіряємо, чи користувач хоче продовжити
        cont = input("Бажаєте продовжити (y/yes для продовження)? : ").strip().lower()
        if cont not in ("y", "yes"):
            print("Дякуємо за користування калькулятором!")
            break

# Запуск програми
calculator()