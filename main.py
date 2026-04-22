import telebot
import urllib.parse
import time
import random

TOKEN = '8518125593:AAE8PtooHglYAqJDrqx_wmBIlrNSBO139Ek'
bot = telebot.TeleBot(TOKEN)

# Dieser Style entfernt den "Puppen-Look" und macht es menschlich
REAL_STYLE = (
    "raw photo, extreme photorealistic, 8k uhd, dslr, soft lighting, "
    "natural skin texture, skin pores, imperfections, hyper-detailed, "
    "shot on 35mm lens, depth of field, high contrast, authentic, "
    "nsfw, naked, uncensored, explicit"
)

@bot.message_handler(func=lambda message: True)
def handle(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "📸 Generiere Real-Life Foto...")
    
    # Wir mischen den Prompt so, dass Realismus an erster Stelle steht
    prompt = f"authentic photography of {message.text}, {REAL_STYLE}"
    encoded = urllib.parse.quote(prompt)
    seed = random.randint(1, 9999999)
    
    # Wir nutzen 1024x1280 (Portrait), das ist das beste Format für Körperdetails
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1280&nologo=true&model=flux&safe=false&seed={seed}"
    
    try:
        # Versand als Dokument verhindert Qualitätsverlust durch Telegram-Kompression
        bot.send_document(chat_id, url, caption="✅ Realism Mod Active")
        bot.delete_message(chat_id, msg.message_id)
    except:
        bot.edit_message_text("❌ Fehler. Versuch es gleich nochmal.", chat_id, msg.message_id)

bot.infinity_polling()
