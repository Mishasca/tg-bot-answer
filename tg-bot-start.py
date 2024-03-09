from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Функция-обработчик команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот. Как дела?')

# Функция-обработчик текстовых сообщений
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Создаем объект Updater и передаем в него токен вашего бота
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
