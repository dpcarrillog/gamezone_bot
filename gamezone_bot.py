from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = '7562653492:AAFdNSJHwCPPCm_Q_d7MvEgu2TnUzucWhR0'  # Reemplaza con tu token de BotFather

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Bienvenido a GameZone Bot!")

# Configurar la aplicación
application = Application.builder().token(TOKEN).build()

# Añadir manejadores de comandos
application.add_handler(CommandHandler("start", start))

# Iniciar el bot
application.run_polling()