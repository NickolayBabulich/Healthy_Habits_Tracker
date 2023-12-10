from django.conf import settings
import requests


class MessageToTelegram:
    def send(self, message):
        URL = 'https://api.telegram.org/bot'
        TOKEN = settings.TELEGRAM_TOKEN
        TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID

        requests.post(
            url=f'{URL}{TOKEN}/sendMessage',
            data={
                'chat_id': TELEGRAM_CHAT_ID,
                'text': message
            }
        )
