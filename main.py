import requests
import time
import search

# Ваш токен и ID канала
TOKEN = "7418415442:AAETsDSMOtR4_l8NfJr6igu8fWDec4kebng"
CHANNEL_ID = "-1002622142869"  # Например, -1001234567890 для приватного канала


def send_advice():
    # Выбор случайного совета
    advice = search.get_daily_advice()

    # Формирование URL для запроса
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    # Параметры запроса
    payload = {
        'chat_id': CHANNEL_ID,
        'text': advice,
        'parse_mode': 'Markdown'  # Можно использовать HTML также
    }

    # Отправка POST-запроса
    response = requests.post(url, data=payload)

    # Проверка ответа
    if response.status_code == 200:
        print("Совет отправлен!")
    else:
        print("Ошибка при отправке совета:", response.text)


while True:
    current_time = time.localtime()
    if current_time.tm_hour == 6 and current_time.tm_min == 30:
        while True:
            send_advice()
            time.sleep(7200)
            if current_time.tm_hour >= 18:
                break
    time.sleep(30)  # Проверяем время каждые 30 секунд
