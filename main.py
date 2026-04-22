import telebot
import urllib.parse
import time
import random

TOKEN = '8518125593:AAE8PtooHglYAqJDrqx_wmBIlrNSBO139Ek'
bot = telebot.TeleBot(TOKEN)

# Maximale HQ-Tags für den "Echt-Look"
HQ_STYLE = (
    "hyper-realistic, 8k uhd, Fujifilm XT4, highly detailed skin texture, "
    "sharp focus, cinematic rim lighting, subsurface scattering, grainy film, "
    "intricate details, masterpiece, raw photo, realistic proportions, "
    "nsfw, naked, uncensored, explicit"
)

@bot.message_handler(func=lambda message: True)
def handle_generation(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "📸 Generiere in 8K Ultra-HQ...")
    
    # Wir fügen noch mehr Qualitäts-Keywords hinzu
    full_prompt = f"{message.text}, {HQ_STYLE}"
    encoded = urllib.parse.quote(full_prompt)
    
    seed = random.randint(1, 1000000)
    
    # Der Trick: Wir schrauben die Breite/Höhe hoch und nutzen den Seed
    # Flux reagiert besser auf 1024x1024 für Details
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1024&nologo=true&model=flux&safe=false&seed={seed}"
    
    try:
        # Wir senden es als Dokument, damit Telegram die Qualität nicht komprimiert!
        bot.send_document(chat_id, url, caption="✅ 8K Ultra-Realistic Render")
        bot.delete_message(chat_id, msg.message_id)
    except:
        bot.edit_message_text("❌ Server-Limit erreicht. Später nochmal versuchen.", chat_id, msg.message_id)

bot.infinity_polling()
