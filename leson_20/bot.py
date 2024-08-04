import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Вставте тут токен вашого бота, який ви отримали від BotFather
TOKEN = '1234567890:ABCdefGhIjKlmnopQRStUVwxYZ'

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Команда `/start`
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт! Я ваш бот.')

# Команда `/help`
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Чим можу допомогти?')

# Функція для відповідей на текстові повідомлення
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Створення бот-апдейтера і диспетчера
    updater = Updater(TOKEN)

    # Отримання диспетчера для регістрації обробників
    dispatcher = updater.dispatcher

    # Регістрація командних обробників
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Регістрація обробника для текстових повідомлень
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Запуск бота
    updater.start_polling()

    # Запуск бота поки не буде натиснуто Ctrl-C або зупинка по іншому сигналу
    updater.idle()

if __name__ == '__main__':
    main()
