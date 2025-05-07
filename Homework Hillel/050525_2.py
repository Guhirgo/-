# число від користувача
seconds_input = int(input("Введіть кількість секунд (0 ≤ сек < 8640000): "))

if 0 <= seconds_input < 8640000:
    #     секунд у добі
    SECONDS_IN_DAY = 86400

    # Розраховуємо дні
    days, remaining_seconds = divmod(seconds_input, SECONDS_IN_DAY)

    # Розраховуємо години
    hours, remaining_seconds = divmod(remaining_seconds, 3600)

    # Розраховуємо хвилини
    minutes, seconds = divmod(remaining_seconds, 60)

    # Форматуємо години, хвилини, секунди з нулями
    time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

    # Вибір правильного слова для "день/дні/днів"
    if days == 1:
        day_word = "день"
    elif 2 <= days <= 4:
        day_word = "дні"
    else:
        day_word = "днів"

    # Виводимо результат!!!!!
    print(f"{days} {day_word}, {time_str}")

else:
    print("Число повинно бути від 0 до 8639999 включно.")
