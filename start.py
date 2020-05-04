from lib.db_manager import db_manager
from lib.settings import *
import telebot

__URL = "https://api.covid19api.com/summary"

db_object = db_manager(host, user, passwd, __URL)

covid_19_data = db_object.get_all_data()
covid_19_save = db_object.save_all_data(covid_19_data)

bot = telebot.TeleBot(token)

covid_19_data
covid_19_save


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    bot.send_sticker(
        message.chat.id, 'CAACAgIAAxkBAAJHnV6XFGmleFAuqbkOCpPyOb1AWAODAAILAANuM_gRBymXN2LhKucYBA')
    keyboard.row('Симптоми COVID-19')
    keyboard.row('Як користуватись ботом?')
    bot.send_message(
        message.chat.id, '1️⃣Щоб переглянути статистику, напишіть назву країни. Наприклад: 𝐔𝐤𝐫𝐚𝐢𝐧𝐞, 𝐈𝐭𝐚𝐥𝐲, 𝐂𝐡𝐢𝐧𝐚, 𝐑𝐮𝐬𝐬𝐢𝐚𝐧 𝐅𝐞𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧, або по коду 𝐔𝐀, 𝐈𝐓, 𝐂𝐍, 𝐑𝐔', reply_markup=keyboard)
    bot.send_voice(message.chat.id, "http://d.zaix.ru/iK2U.mp3")


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Симптоми COVID-19')
    keyboard.row('Як користуватись ботом?')
    countr = message.text
    countrycode = message.text
    coron = db_object.show_country(countr, countrycode)
    if message.text == countr or message.text == countrycode:
        for item in coron:
            bot.send_message(message.from_user.id, "Оперативна інформація про поширення коронавірусної інфекції 🌏 [𝐂𝐎𝐕𝐈𝐃-19] 🌏\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯"+"\n✈️ Країна ✈️ → " + str(item[1]) + "\n🤧 Кількість захворювань 🤧 → " + str(item[5]) + "\n🤧 Кількість захворювань за добу 🤧 → " + str(
                item[6]) + "\n☠️ Кількість смертей ☠️ → " + str(item[7]) + "\n☠️ Кількість смертей за добу ☠️ → " + str(item[6]) + "\n💊 Кількість вилікуваних 💊 → " + str(item[9]) + "\n💊 Кількість вилікуваних за добу 💊 → " + str(item[8]), reply_markup=keyboard)

    if message.text == "Симптоми COVID-19":
        bot.send_photo(message.chat.id, "http://i.piccy.info/i9/7333fbd68a014010173ed8f1a74969f0/1587472373/401901/1374142/43_Algorytm_d_1110_i_za_p_1110_dozry_COVID_19.jpg", reply_markup=keyboard)
    elif message.text == "Як користуватись ботом?":
        bot.send_message(
            message.chat.id, "1️⃣Щоб переглянути статистику, напишіть назву країни. Наприклад: 𝐔𝐤𝐫𝐚𝐢𝐧𝐞, 𝐈𝐭𝐚𝐥𝐲, 𝐂𝐡𝐢𝐧𝐚, 𝐑𝐮𝐬𝐬𝐢𝐚𝐧 𝐅𝐞𝐝𝐞𝐫𝐚𝐭𝐢𝐨𝐧, або по коду 𝐔𝐀, 𝐈𝐓, 𝐂𝐍, 𝐑𝐔", reply_markup=keyboard)


bot.polling(none_stop=True)
