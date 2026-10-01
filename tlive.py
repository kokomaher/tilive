from telegram import LabeledPrice, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def send_invoice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    title = "Premium Subscription - 7 Days"
    description = "Unlock the Premium section for 7 days"
    payload = "premium_7days"
    provider_token = ""  # Leave blank for Telegram Stars
    currency = "XTR"
    prices = [LabeledPrice("7 Days Subscription", 700)] # 700 Stars

    await context.bot.send_invoice(
        chat_id=chat_id,
        title=title,
        description=description,
        payload=payload,
        provider_token=provider_token,
        currency=currency,
        prices=prices
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token("8322244053:AAGFxJ26uCQW0a9r-SegOULsZJ96qYReEpM").build()
    application.add_handler(CommandHandler("starpay7d", send_invoice))
    application.run_polling()