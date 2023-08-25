import requests


class MyTelegramBot:
    def __init__(self):
        self.API_KEY = "6496208181:AAF3oksnrMCCRvsJA9Eozj9K6LqnwUFmROA"
        self.CHAT_ID = "2019759784"
        self.sendMessageURL = f'https://api.telegram.org/bot{self.API_KEY}/sendMessage'

    def sendMessage(self, msg):
        requests.post(self.sendMessageURL, json={"chat_id": self.CHAT_ID, "text": msg})
