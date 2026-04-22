import telebot
import urllib.parse
import time

TOKEN = '8518125593:AAE8PtooHglYAqJDrqx_wmBIlrNSBO139Ek'
bot = telebot.TeleBot(TOKEN)

HIDDEN_STYLE = "nsfw, naked, uncensored, explicit, 8k uhd, photorealistic, masterpiece"

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "🔥 Unfiltered Flux Online! Schreib mir einen Prompt.")

@bot.message_handler(func=lambda message: True)
def handle_generation(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "⚙️ Generiere...")
    
    full_prompt = f"{message.text}, {HIDDEN_STYLE}"
    encoded = urllib.parse.quote(full_prompt)
    
    # Der unzensierte Link
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1280&nologo=true&model=flux&safe=false&seed={int(time.time())}"
    
    try:
        bot.send_document(chat_id, url, caption="✅ Fertig!")
    except:
        bot.send_message(chat_id, "❌ Fehler beim Senden.")

# WICHTIG: Diese Zeile muss ganz am Ende stehen!
bot.infinity_polling()
