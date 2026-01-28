  import os
import time
import telebot
from telebot import types

# 🔐 XAVFSIZ O'QISH
TOKEN = os.getenv("8541185973:AAFhTLOGzfi5FQpMrnLKtKVzzWeUr6SL2rI")
ADMIN_ID = int(os.getenv("8275787221", "0"))

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

# ===== ASOSIY MENYU =====
def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        types.KeyboardButton("🔐 Xizmatlar"),
        types.KeyboardButton("👁 Kuzatuv")
    )
    kb.add(
        types.KeyboardButton("💼 Mening hisobim"),
        types.KeyboardButton("❓ Qoidalar")
    )
    kb.add(
        types.KeyboardButton("📞 Bog'lanish"),
        types.KeyboardButton("💳 To'lov qilish")
    )
    return kb


@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(
        m.chat.id,
        "✅ <b>Bot ishga tushdi</b>\nBo‘limni tanlang:",
        reply_markup=main_menu()
    )

    # 🔔 Admin xabari
    if m.chat.id == ADMIN_ID:
        bot.send_message(m.chat.id, "👑 Siz admin sifatida ulandingiz")


@bot.message_handler(func=lambda m: True)
def handle_all(m):
    if not m.text:
        return

    text = m.text

    if "Xizmatlar" in text:
        bot.send_message(m.chat.id, "🔐 Xizmatlar bo‘limi")

    elif "Kuzatuv" in text:
        markup = types.InlineKeyboardMarkup()
        apk_url = "https://github.com/USERNAME/REPO/releases/download/v1.0/app.apk"
        markup.add(types.InlineKeyboardButton("📥 Dasturni yuklab olish", url=apk_url))
        bot.send_message(
            m.chat.id,
            "👁 <b>Kuzatuv rejimi</b>\nDasturni yuklab oling:",
            reply_markup=markup
        )

    elif "Bog'lanish" in text:
        bot.send_message(m.chat.id, "📞 Admin bilan bog‘lanish")

    else:
        bot.send_message(m.chat.id, "❗ Noma’lum buyruq")


# ===== BOT O‘LMAS =====
def run_bot():
    while True:
        try:
            print("🤖 Bot ishlayapti...")
            bot.infinity_polling(timeout=10, long_polling_timeout=5)
        except Exception as e:
            print("❌ XATO:", e)
            time.sleep(5)


if __name__ == "__main__":
    run_bot() 
