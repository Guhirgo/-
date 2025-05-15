import requests

def get_url() -> str:
    """
    Повертає URL-адресу для отримання постів.
    """
    return "https://dummyjson.com/posts"

def get_data(endpoint: str = "posts") -> list[dict]:
    """
    Отримує список постів з API.
    """
    response = requests.get(get_url())
    data = response.json()
    return data['posts']  # повертаємо список постів

def get_username() -> str:
    """
    Запитує ім’я користувача.
    """
    name = input("👤 Введіть ваше ім'я: ")
    return name

def get_user_search_text() -> str:
    """
    Запитує слово для пошуку у постах.
    """
    word = input("🔍 Введіть слово для пошуку: ")
    return word.strip()

def main():
    """
    Основна функція: отримує ім’я, слово для пошуку і показує результати.
    """
    username = get_username()
    search_word = get_user_search_text()
    posts = get_data()

    print(f"\nПривіт, {username}! Шукаємо слово: '{search_word}'...\n")

    found = False
    for post in posts:
        if search_word.lower() in post['title'].lower() or search_word.lower() in post['body'].lower():
            print(f"📝 ID: {post['id']}, Title: {post['title']}")
            found = True

    if not found:
        print("😢 Нічого не знайдено за цим словом.")

if __name__ == "__main__":
    main()
