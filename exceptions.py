import requests
import json
import telebot.types
from config_keys import keys

class ConvertionsException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionsException(f'Вы пытаетесь перевести одинковые валют {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionsException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionsException(f'Не удалось обработать валюту {base}')
        if float(amount) <= 0:
            raise ConvertionsException(f'Введите колчиество валюты больше 0')
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * float(amount)

        return total_base
