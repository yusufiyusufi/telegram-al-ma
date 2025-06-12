from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.environ.get("TOKEN")

# Site isimleri ve linkleri
SITES = {
    "BETTİLT": "https://btt-tr.tueyw.com/tr/casino?partner=p5470p22977pa1c9#registration-bonus",
    "TARAFBET": "https://cutt.ly/irvobxsk",
    "BAHİS.COM": "https://cutt.ly/urvobtB1",
    "MARİOBET": "https://cutt.ly/IrvoW1rJ",
    "BANKOBET": "https://cutt.ly/hrvoQPCO",
    "BETEWİN": "https://cutt.ly/rrvoOk5e",
    "BETKOM": "https://cutt.ly/4rvonQaC",
    "VAYCASİNO": "https://t2m.io/2413138",
}

async def send_sites(update: Update, context: ContextTypes.DEFAULT_TYPE, keys):
    photo_url = "https://i.imgur.com/Y2U2Gve.png"  # Fotoğraf URL'si
    keyboard = []
    for key in keys:
        if key in SITES:
            keyboard.append([InlineKeyboardButton(key.capitalize(), url=SITES[key])])

    if not keyboard:
        await update.message.reply_text("Maalesef bu site bulunamadı.")
        return

    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=photo_url,
        caption="İşte istediğiniz site(ler):",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()
    if not text.startswith("!"):
        return

    cmd = text[1:]  # ! işaretinden sonrası

    if cmd == "site":
        # Tüm site butonları
        await send_sites(update, context, SITES.keys())
    else:
        # Tekil site komutu
        await send_sites(update, context, [cmd])

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
