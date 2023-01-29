from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')  

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text('Калькулятор приветствует вас!')
    await update.message.reply_text('Выберите операцию, введите 2 числа через пробел \n'
                    '1 -  "сложение"\n'
                    '2 - "вычитание"\n'
                    '3 - "умножение"\n'
                    '4 - "деление"\n'
                    '5 - "возведение в степень"\n'
                    '6 - "квадратный корень - введите 1 число"\n')
                   
        
async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')  

async def mul_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}') 

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    if y == 0:
        await update.message.reply_text('Error')
    else:
        await update.message.reply_text(f'{x} / {y} = {x / y}')
      

async def pow_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} ^ {y} = {x ** y}') 

async def sqrt_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    msg = update.message.text
    item = msg.split()
    x = int(item[1])
    await update.message.reply_text(f'квадратный корень {x} = {x**0.5}')      
