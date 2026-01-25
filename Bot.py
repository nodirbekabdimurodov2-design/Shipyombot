import telebot
from telebot import types
import os
from flask import Flask
from threading import Thread

# Render port xatosi (Timed out) bermasligi uchun server
app = Flask('')
@app.route('/')
def home():
    return "Bot is running!"

def run():
    # Render avtomatik beradigan portni olamiz yoki 8080 ishlatamiz
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# BOT SOZLAMALARI
TOKEN = '8541185973:AAFhTLOGzfi5FQpMrnLKtKVzzWeUr6SL2rI'
ADMIN_ID = 8275787221 
URL = "https://nodirbekabdimurodov2-design.github.io/Shipyombot"

bot = telebot.TeleBot(TOKEN)

# Menyu va funksiyalar
def main_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add(types.KeyboardButton("🔐 Xizmatlar"), types.KeyboardButton("💼 Mening hisobim"))
    kb.add(types.KeyboardButton("❓ Qoidalar"), types.KeyboardButton("📞 Bog'lanish"))
    kb.add(types.KeyboardButton("💳 To'lov qilish"))
    return kb

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "✅ Bot doimiy rejimda ishga tushdi!", reply_markup=main_menu())

# ... (boshqa tugmalar kodi shu yerda davom etadi)

if __name__ == "__main__":
    keep_alive() # Serverni botdan oldin ishga tushirish
    bot.polling(none_stop=True)
 
