from glob import glob
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, MessageHandler, CommandHandler
from telegram.ext import Filters
from text import text


def main_keyboard():
    return ReplyKeyboardMarkup([['ПОЛУЧИТЬ БЕСПЛАТНУЮ ПСИХОЛОГИЧЕСКУЮ ПОМОЩЬ']], resize_keyboard=True)


def great_user(update: Update, callback: CallbackContext):
    update.message.reply_text(text='Привет! Мы оказываем профессиональную психологическую помощь людям, '
                                   'которые оказались заложниками ситуации, в связи с военными действиями на'
                                   ' территории Украины.', reply_markup=main_keyboard())


def get_help(update, context):
    for filename in glob(".\photo\*.jpg"):
        url = filename
        context.bot.send_photo(
            chat_id=update.message.chat_id, 
            photo=open(url, 'rb'), 
            caption=filename[8:-4]
            )


def main():
    updater = Updater(
        token="5175856451:AAFGLAsGtmIYfMeO1ODbnyV1NfUXUsCmPr8",
        use_context=True
    )
    updater.dispatcher.add_handler(CommandHandler('start', great_user))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('^(ПОЛУЧИТЬ БЕСПЛАТНУЮ ПСИХОЛОГИЧЕСКУЮ ПОМОЩЬ)$'), get_help))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()