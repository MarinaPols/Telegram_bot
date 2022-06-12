import telebot
from config_keys import keys
from exceptions import ConvertionsException, CryptoConverter

bot = telebot.TeleBot('5350807864:AAGvzL-eAg8DoU3q81AKQEiPR9OasUICMJ0')

quote = 'USD'
base = 'RUB'
amount = 100
import telebot.types

@bot.message_handler(commands=['start', 'help', 'command1', 'command2', 'command3'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите комманду в строку в следующем формате: \n<имя валюты> ' \
'\n<в какую валюту перевести> ' \
'\n<количество валюты>\nУвидеть список доступных валют: /values'
    bot.reply_to(message, text)
#обработчик доступных валют
import telebot.types
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys:
        text = '\n'.join((text,key, ))
    bot.reply_to(message, text)
@bot.message_handler(content_types=['text', ])
def converter(message: telebot.types.Message):
    try:

        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionsException('Слишком много параметров')
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionsException as e:
        bot.reply_to(message, f'Ты ошибся во вводе, дорогой пользователь\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {round(total_base,2)}'
        bot.reply_to(message, text)
#start bot on a permanent basis
bot.polling()
