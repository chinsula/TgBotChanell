import requests
from bs4 import BeautifulSoup
import random
import re

def get_daily_advice():
    # URL сайта, с которого будем получать советы
    url = "https://singularity-app.ru/blog/motiviruyushchie-tsitaty"  # Замените на нужный вам сайт

    try:
        # Получаем страницу
        response = requests.get(url)
        response.raise_for_status()  # проверяем, что запрос успешен
    except requests.RequestException as e:
        print(f"Ошибка при запросе к сайту: {e}")
        return None

    # Парсим HTML-код страницы с помощью BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Найдите элемент на странице, который содержит нужный совет
    # Этот селектор нужно изменить в зависимости от структуры HTML целевого сайта
    advice_elements = soup.select('p')  # замените на актуальный CSS-селектор

    if not advice_elements:
        print("Не удалось найти советы.")
        return None

    # Выбираем случайный совет
    random_advice = random.choice(advice_elements)
    text = str(random_advice.get_text(strip=True))
    cleaned_text = re.sub(r'^\d+\.', '', text)
    return cleaned_text.strip()

if __name__ == "__main__":
    advice = get_daily_advice()
    if advice:
        print("Совет на день:")
        print(advice)
