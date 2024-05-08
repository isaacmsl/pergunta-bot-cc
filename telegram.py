import telebot
from ai import answer_query

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# handler to all messages
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    query = message.text
    try:
        answer = answer_query(query)
        bot.reply_to(message, answer)
    except Exception as e:
        bot.reply_to(message, "Desculpa, algo inesperado aconteceu :(")

bot.polling()