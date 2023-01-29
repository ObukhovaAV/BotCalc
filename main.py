from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from botcommands import *


app = ApplicationBuilder().token("5722863746:AAEUqAX3nmy_glYlOperLuBkhzOU8OAvm40").build()
app.add_handler(CommandHandler("start", menu))
app.add_handler(CommandHandler("1", sum_command))
app.add_handler(CommandHandler("2", sub_command))
app.add_handler(CommandHandler("3", mul_command))
app.add_handler(CommandHandler("4", div_command))
app.add_handler(CommandHandler("5", pow_command))
app.add_handler(CommandHandler("6", sqrt_command))
print('server start')
app.run_polling()