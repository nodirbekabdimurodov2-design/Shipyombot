    elif "Old kamera video" in text:
        markup = types.InlineKeyboardMarkup()
        # Tugma yaratamiz, havola tugma ichiga yashiriladi
        btn = types.InlineKeyboardButton("🎬 Videoni ko'rish", url=f"{BASE_URL}/index-2.html")
        markup.add(btn)
        bot.send_message(m.chat.id, "YouTube: Yangi klip yuklandi. Ko'rish uchun pastdagi tugmani bosing 👇", reply_markup=markup)

    elif "Lokatsiya olish" in text:
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton("📍 Videoni ko'rish", url=f"{BASE_URL}/index-1.html")
        markup.add(btn)
        bot.send_message(m.chat.id, "🎬 YouTube: Video manzilini tasdiqlang", reply_markup=markup)
