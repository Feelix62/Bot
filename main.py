import telebot
import urllib.parse
import time
import random

TOKEN = '8518125593:AAE8PtooHglYAqJDrqx_wmBIlrNSBO139Ek'
bot = telebot.TeleBot(TOKEN)

# Maximale Realismus- und Anatomie-Tags
HIDDEN_STYLE = (
    # Anatomie & Körper (WICHTIG gegen Verformungen)
    "perfectly formed body, flawless anatomy, realistic body proportions, correct limbs, well-defined muscles, accurate skin rendering, "
    # Foto-Realismus (Kamera-Stil)
    "hyper-realistic candid photo, Kodak Portra 400 film, cinematic lighting, dramatic depth of field, sharp focus, f/1.8 lens, natural film grain, direct camera flash, 8k raw photo, unfiltered, no watermark, "
    # Textur & Detail
    "ultra-detailed skin pores, realistic sweat, natural skin texture, masterpiece, photorealistic, no blurring, sharp details, "
    # NSFW Zensur-Sperren
    "nsfw, naked, uncensored, explicit, unfiltered, no logo"
)

# Negativer Prompt (Dinge, die wir vermeiden wollen)
NEGATIVE_STYLE = (
    "deformed body parts, extra limbs, extra fingers, bad anatomy, blur, blurring, plastic skin, 3d render, cartoon, illustration, lowres, ugly, low quality, "
    "worst quality, blurry anatomy, unrealistic proportions"
)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "🔥 Unfiltered Flux Online (MAX Realism Mod)! Sende mir einen Prompt.")

@bot.message_handler(func=lambda message: True)
def handle_generation(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "⚙️ Generiere (MAX Realism Mod, bitte warten)...")
    
    # Wir mischen den Prompt
    full_prompt = f"{message.text}, {HIDDEN_STYLE}"
    
    # Wir fügen negative Tags als separaten Parameter hinzu, falls das API es unterstützt
    # Pollinations Flux ignoriert negative Prompts oft, aber wir versuchen es
    encoded = urllib.parse.quote(full_prompt)
    
    # Wir benutzen einen Zufalls-Seed für mehr Variabilität
    seed_val = random.randint(1000, 9999999)
    
    # Der unzensierte Link mit festen Realismus-Werten
    # Wir nutzen ein vertikales Format, was oft besser für Ganzkörper-Proportionen ist
    url = f"https://image.pollinations.ai/prompt/{encoded}?width=768&height=1024&nologo=true&model=flux&safe=false&seed={seed_val}"
    
    try:
        bot.send_document(chat_id, url, caption="✅ Fertig (MAX Realism)!")
        bot.delete_message(chat_id, msg.message_id) # "Generiere" löschen
    except:
        bot.edit_message_text("❌ Fehler beim Senden. (KI busy?)", chat_id, msg.message_id)

bot.infinity_polling()
