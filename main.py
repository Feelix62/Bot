import telebot
import urllib.parse
import time

# Dein Bot-Token
TOKEN = '8518125593:AAE8PtooHglYAqJDrqx_wmBIlrNSBO139Ek'
bot = telebot.TeleBot(TOKEN)

# Diese Tags werden bei JEDEM Bild im Hintergrund hinzugefügt
# Sie sorgen für den "Promptchan"-Look (Realismus + NSFW)
HIDDEN_STYLE = (
    "nsfw, naked, uncensored, explicit, 8k uhd, photorealistic, "
    "highly detailed skin, masterpiece, cinematic lighting"
)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "🔥 **Unfiltered Flux Engine Online**\nSende mir einen Prompt (z.B. 'Young woman in kitchen').")

@bot.message_handler(func=lambda message: True)
def handle_generation(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "⚙️ **Generiere... (Flux Model)**")
    
    # Prompt zusammenbauen
    full_prompt = f"{message.text}, {HIDDEN_STYLE}"
    encoded = urllib.parse.quote(full_prompt)
    
    # Der technische "Trick": safe=false deaktiviert den Filter auf dem Server
    # width=1024 & height=1280 für das beste Portrait-Format
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1280&nologo=true&model=flux&safe=false&seed={int(time.time())}"
    
    try:
        # Versand als Dokument, um die volle 4K-Schärfe zu behalten
        bot.send_document(chat_id, url, caption="✅ Bild erfolgreich generiert.")
    except Exception as e:
        bot.send_message(chat_id, "❌ API-Fehler. Versuche es mit einem kürzeren Prompt.")

bot.infinity_polling()
