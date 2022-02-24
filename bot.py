from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, MessageHandler, CommandHandler
from telegram.ext import Filters
from text import text


def main_keyboard():
    return ReplyKeyboardMarkup([['Получить бесплатную психологическую помощь']], resize_keyboard=True)


def great_user(update: Update, callback: CallbackContext):
    update.message.reply_text(text='Привет! Мы оказываем профессиональную психологическую помощь людям, '
                                   'которые оказались заложниками ситуации в связи с военными действиями на'
                                   ' территории Украины.', reply_markup=main_keyboard())


def get_help(update, context):
   # update.message.reply_text()
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-27-54.jpg", 'rb'),
        caption='Виктория Лебедева, психосоматика @Victoriya_lebedeva_psy'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-27-46.jpg", 'rb'),
        caption='Ольга Николенко, психолог @nik_olyashka'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-27-48.jpg", 'rb'),
        caption='Oksana Bilenko, Специалист по психосоматике PSY 2.0 @oksanabilenko'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-27-50.jpg", 'rb'),
            caption='Анастасия Сехина, психолог @sekhina'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-27-52.jpg", 'rb'),
            caption='Екатерина, психолог @eliseeva_psy'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-27-53.jpg", 'rb'),
            caption='Алена, психолог @elena_tkachen'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-49-39.jpg", 'rb'),
            caption='Olya Iv, психолог @oli_iordan'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-49-41.jpg", 'rb'),
            caption='Mariia Sineokova, психолог @tripmasha'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-49-42.jpg", 'rb'),
            caption='Karina, психолог @Karina9876'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-49-44.jpg", 'rb'),
            caption='Камила, Психология ~ Психосоматика @kamila_sokolova'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_14-19-57.jpg", 'rb'),
            caption='Evgenia Ushakova, психолог @Victoriya_lebedeva_psy'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"C:\Users\user\PycharmProjects\PsyUaBot\photo\photo_2022-02-24_13-27-54.jpg", 'rb'),
            caption='Виктория Лебедева, психосоматика @Victoriya_lebedeva_psy'
        )


def main():
    updater = Updater(
        token="5175856451:AAFGLAsGtmIYfMeO1ODbnyV1NfUXUsCmPr8",
        use_context=True
    )
    updater.dispatcher.add_handler(CommandHandler('start', great_user))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('^(Получить бесплатную психологическую помощь)$'), get_help))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()