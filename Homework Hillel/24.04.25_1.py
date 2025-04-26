def calculator():
    # Запитуємо користувача на введення чисел
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))

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
        # Перевірка на ділення на нуль
        if num2 == 0:
            print("Помилка: Дільник не може бути нулем!")
            return  # Завершуємо виконання програми, якщо ділення на нуль
        else:
            result = num1 / num2
    else:
        print("Невідома операція!")
        return  # Завершуємо виконання програми, якщо операція некоректна

    # Виводимо результат
    print(f"Результат: {result}")


# Викликаємо функцію калькулятора
calculator()