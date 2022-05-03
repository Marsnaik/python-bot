from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import telebot

owm = OWM('ff0e0d825ae8a04d3e1f29ec889bf50e')
mgr = owm.weather_manager()
bot = telebot.TeleBot('5194181175:AAFnWIGdMnKcm5AZFnWy7ltqldEWPUYPql4')

from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place('Krasnodar')
    w = observation.weather
    p = w.temperature('celsius')["temp"]
    o = w.rain

    answer = "♥ Привет зайка! ♥" + "\n\n"
    answer += "(\(\ " + "\n"
    answer += "( .  .) ♥" + "\n"
    answer += "c('')('')" + "\n\n"
    answer += "   ---------------------------------" + "\n"
    answer += "♥ Сейчаc " + str(w.detailed_status) + " ♥" + "\n"
    answer += "   ---------------------------------" + "\n"
    answer += "♥ Температура " + str(p) + " ♥" + "\n"
    answer += "   ---------------------------------" + "\n"

    if o == {}:
        answer += "♥ Дождя нет ♥" + "\n"
        answer += "   ----------------------------------------------------" + "\n"
    else:
        answer += "♥ Идёт дождь ♥" + "\n"
        answer += "   ----------------------------------------------------" + "\n"

    if int(p) < 10:
        answer += "♥ На улице очень холодно, надень шерстяные трусы ♥" + "\n"
        answer += "   ----------------------------------------------------"
    elif int(p) < 20:
        answer += "♥ Прохладно, оденься потеплее ♥" + "\n"
        answer += "   ----------------------------------------------------"
    else:
        answer += "♥ Температура норм, одейвай что угодно, хоть страпон ♥" + "\n"
        answer += "   ----------------------------------------------------" + "\n"

    bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True)
