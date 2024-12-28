import telebot

API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! Touch the button below to download and play the game!")

@bot.message_handler(func=lambda message: True)
def send_game(message):
    with open('path_to_your_executable/your_game_script.exe', 'rb') as game_file:
        bot.send_document(message.chat.id, game_file)

bot.polling()