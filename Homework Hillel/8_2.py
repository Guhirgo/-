import re

def is_palindrome(text):
    # Видаляємо все, що не є буквою чи цифрою, та переводимо в нижній регістр
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    # Перевіряємо, чи рядок однаково читається в обидва боки
    return cleaned == cleaned[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")
