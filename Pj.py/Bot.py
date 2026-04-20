import telebot 

bot = telebot.TeleBot('TOKEN AQUI')

@bot.message_handler(['start' , 'help'])  
def start(msg:telebot.types.Message):
    bot.reply_to(msg, 'Ola, mundo!')

@bot.message_handler(['bom_dia'])
def bom_dia(msg:telebot.types.Message):
    bot.reply_to(msg, 'Bom dia seu Moreno!')

@bot.message_handler(['boa_tarde'])
def bom_dia(msg:telebot.types.Message):
    bot.reply_to(msg, 'Boa tarde seu lindo')

bot.infinity_polling()
