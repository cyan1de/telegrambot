from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

answers = { 
        "привет": "И тебе привет!Меня зовут Learn Python Bot, меня создал какой то айтишник который учит программирование, но пока он говнокодер и живет на stackoverflow", 
        "как дела?": "Норм! А твои как?",
        "плохо": "Хреново тебе",
        "отлично": "Ну и чудненько!Давай общаться?",
        "пока": "Ну вот, только начали,а ты уходишь!Ну и уходи :( Редиска",
}

def main():
    updater = Updater("238681148:AAFlDtiwCszpFFVVWr0Ce8qvofpsin5W2TQ")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()

def start(bot, update):
    print('Вызван /start')
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')
def talk_to_me(bot, update):
    print('Пришло сообщение: %s' % update.message.text)

    def get_answers(key, answers):
        return answers.get(key, 'Пишешь какую-то фигню, я не пониамю.Спроси что-нибудь нормальное!')
    user_input = update.message.text.lower().strip()
    answer = get_answers(user_input, answers)
    bot.sendMessage(update.message.chat_id, text = answer)
    bot.sendMessage(update.message.chat_id, update.message.text.encode('utf-8'))

if __name__ == '__main__':
    main()