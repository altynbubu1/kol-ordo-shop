import requests

TELEGRAM_BOT_TOKEN = '7573975708:AAF1o5lOP1iPLYly4hRG82xb3J9suvoFTZw'  # ← Вставь свой токен
TELEGRAM_CHAT_ID = '1858442800'  # ← Вставь свой Telegram user ID

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML',
    }
    response = requests.post(url, data=data)
    return response.json()
