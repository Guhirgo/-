import keyword
import string

def is_valid_variable_name(name):
    #  лише одне нижнє підкреслення допускається
    if name.count('_') > 1:
        return False

    #  Не повинно бути великої літери
    if any(char.isupper() for char in name):
        return False

    # е повинно містити пробілів або заборонених символів, окрім "_"
    allowed_chars = string.ascii_lowercase + string.digits + "_"
    if any(char not in allowed_chars for char in name):
        return False

    # Не може починатися з цифри
    if name and name[0].isdigit():
        return False

    #  Не може бути зареєстрованим словом
    if name in keyword.kwlist:
        return False

    # Якщо всі перевірки пройдені — ім'я дійсне.
    return True


user_input = input("Введіть ім'я змінної: ")
print(is_valid_variable_name(user_input))