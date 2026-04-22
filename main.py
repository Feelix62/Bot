import telebot
import urllib.parse
import time
import random

TOKEN = '8518125593:AAE8PtooHglYAqJDrqx_wmBIlrNSBO139Ek'
bot = telebot.TeleBot(TOKEN)

# Dieser Style erzwingt den "Echt-Look" von spezialisierten NSFW-Modellen
PROMPTCHAN_STYLE = (
    "extremely lifelike, real human skin, high detail, masterpiece, 8k, "
    "shot on iPhone, amateur photography, candid, natural lighting, "
    "detailed eyes, realistic body proportions, skin texture, moles, "
    "depth of field, bokeh, nsfw, naked, uncensored, explicit, no blur"
)

@bot.message_handler(func=lambda message: True)
def handle(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "💎 Generiere High-End Realismus...")
    
    # Wir setzen "Amateur Photo" nach vorne, das ist das Geheimnis für Echtheit
    user_input = message.text
    full_prompt = f"candid amateur photo of {user_input}, {PROMPTCHAN_STYLE}"
    
    encoded = urllib.parse.quote(full_prompt)
    seed = random.randint(1, 999999999)
    
    # Wir nutzen ein etwas schmaleres Format (896x1152), das für Körper oft stabiler ist
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=896&height=1152&nologo=true&model=flux&safe=false&seed={seed}"
    
    try:
        # Als Dokument senden für volle Schärfe ohne Telegram-Matsch
        bot.send_document(chat_id, url, caption="✅ Ultra-Realistic V4")
        bot.delete_message(chat_id, msg.message_id)
    except:
        bot.edit_message_text("❌ Server ausgelastet. Probier es nochmal!", chat_id, msg.message_id)

bot.infinity_polling()
