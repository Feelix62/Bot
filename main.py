import telebot
import urllib.parse
import time

TOKEN = '8518125593:AAE8PtooHglYAqJDrqx_wmBIlrNSBO139Ek'
bot = telebot.TeleBot(TOKEN)

# Diese Tags sorgen jetzt für echtes Aussehen
HIDDEN_STYLE = (
    # Realismus-Tags
    "ultra photorealistic, candid photo, kodak portra 400 film, direct flash, 35mm lens, grainy, "
    # Foto-Details
    "natural skin texture, raw photo, realistic, cinematic lighting, ultra-detailed skin, soft light, "
    # Zensur-Sperren
    "nsfw, naked, uncensored, explicit, unfiltered, no logo"
)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "🔥 Unfiltered Flux Online (Realism Mod)! Sende mir einen Prompt.")

@bot.message_handler(func=lambda message: True)
def handle_generation(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "⚙️ Generiere (Photorism)...")
    
    full_prompt = f"{message.text}, {HIDDEN_STYLE}"
    encoded = urllib.parse.quote(full_prompt)
    
    # Der unzensierte Link mit festen Realismus-Werten
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=1024&height=1280&nologo=true&model=flux&safe=false&seed={int(time.time())}"
    
    try:
        bot.send_document(chat_id, url, caption="✅ Fertig (Realism Mod)!")
        bot.delete_message(chat_id, msg.message_id) # "Generiere" löschen
    except:
        bot.edit_message_text("❌ Fehler beim Senden. (KI busy?)", chat_id, msg.message_id)

bot.infinity_polling()
