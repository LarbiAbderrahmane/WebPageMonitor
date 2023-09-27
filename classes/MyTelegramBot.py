import requests


class MyTelegramBot:
    def __init__(self):
        self.API_KEY = "6494270692:AAGpZfQo9dT-Dmq5ofk6TNxxhprGJVn_gSQ"
        self.CHAT_ID = "6618995400"
        self.sendMessageURL = f'https://api.telegram.org/bot{self.API_KEY}/sendMessage'

    def sendMessage(self, msg):
        requests.post(self.sendMessageURL, json={"chat_id": self.CHAT_ID, "text": msg})
