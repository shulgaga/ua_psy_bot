from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, MessageHandler, CommandHandler
from telegram.ext import Filters


def main_keyboard():
    return ReplyKeyboardMarkup([['Получить бесплатную психологическую помощь']], resize_keyboard=True)


def great_user(update: Update, callback: CallbackContext):
    update.message.reply_text(text='Привет! Мы оказываем профессиональную психологическую помощь людям, '
                                   'которые оказались заложниками ситуации в связи с военными действиями на'
                                   ' территории Украины.', reply_markup=main_keyboard())


def get_help(update, context):
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_13-27-54.jpg", 'rb'),
        caption='Виктория Лебедева, психосоматика @Victoriya_lebedeva_psy'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_13-27-46.jpg", 'rb'),
        caption='Ольга Николенко, психолог @nik_olyashka'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_13-27-48.jpg", 'rb'),
        caption='Oksana Bilenko, Специалист по психосоматике PSY 2.0 @oksanabilenko'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_13-27-50.jpg", 'rb'),
            caption='Анастасия Сехина, психолог @sekhina'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_13-27-52.jpg", 'rb'),
            caption='Екатерина, психолог @eliseeva_psy'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_13-27-53.jpg", 'rb'),
            caption='Алена, психолог @elena_tkachen'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_13-49-39.jpg", 'rb'),
            caption='Olya Iv, психолог @oli_iordan'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_13-49-41.jpg", 'rb'),
            caption='Mariia Sineokova, психолог @tripmasha'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_13-49-42.jpg", 'rb'),
            caption='Karina, психолог @Karina9876'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_13-49-44.jpg", 'rb'),
            caption='Камила, Психология ~ Психосоматика @kamila_sokolova'
        )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-24.jpg", 'rb'),
        caption='Evgenia Ushakova, психолог @Evgenia_Ushakova_psy'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-24 (2).jpg", 'rb'),
        caption='Diana Bazukevich, йога, медитация, гвозди, психосоматика @DiankaBazz'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-25.jpg", 'rb'),
        caption='Maria, Работаю через тело, в воде и на суше. @mariapavlova_kh'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-26.jpg", 'rb'),
        caption='Cerchez Aliona, психолог '
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-26 (2).jpg", 'rb'),
        caption='𝘚𝘷𝘦𝘵𝘭𝘢𝘯𝘢 𝘌𝘳𝘮𝘪𝘭𝘪𝘯𝘢, Психолог-терапевт ТВУ, специалист по психосоматике для активных людей @ermilinalight'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-27.jpg", 'rb'),
        caption='Svitlana 7878, психолог @Svitlana7878'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-27 (2).jpg", 'rb'),
        caption='Elena Belgium, психолог по методу PSY 2.0 @Elena_peace'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-28.jpg", 'rb'),
        caption='Майя Головенко, психолог @MayaGolovenko'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-28 (2).jpg", 'rb'),
        caption='Svetlana Galetin, ПСИХОСОМАТИКА, метод PSY2.0 @Svetlana_Galetin'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-29.jpg", 'rb'),
        caption='Татьяна, Кундалини-йога, психосоматика psy2.0 @Tatian202'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-29 (2).jpg", 'rb'),
        caption="Варвара Муравьева, психолог @Varenik21"
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-30.jpg", 'rb'),
        caption='Оля Федоренко, психолог @fedorenko_olya'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-30 (2).jpg", 'rb'),
        caption='Любовь Звонкова, неНумеролог, психосоматика, psy 2.0.  @LyubovZvonkova'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-31.jpg", 'rb'),
        caption='Oksana Polivina, Психолог|Специалист по психосоматике, методом Антона Антонова|,НЛП.  @oksanapolivina'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-31 (2).jpg", 'rb'),
        caption='Инна Angelovskaya, Психосоматика 🌱 PSY 2.0 🌱 ГНМ    @angelovskaya_psy'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-32.jpg", 'rb'),
        caption='Angelina, Помогаю наладить связь с реальностью). Психология/психосоматика.  @adpsy20'
    )
    context.bot.send_photo(
        chat_id=update.message.chat_id,
        photo=open(r"photo/photo_2022-02-24_18-34-32 (2).jpg", 'rb'),
        caption='Lena Ru, психолог.  @elena_rul'
    )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_18-34-33.jpg", 'rb'),
            caption='Ludmila L, психолог. @Ludmila_psy'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_18-34-34.jpg", 'rb'),
            caption='Елена, Консультант по Психосоматике и Рейки.  @Elena_way_light'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_18-34-34 (2).jpg", 'rb'),
            caption='Merry Am, PRO чувства | Психосоматика | NLP.   @MerryAm'
        )
    context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=open(r"photo/photo_2022-02-24_18-34-35.jpg", 'rb'),
            caption='Ольга, психолог.  @ola_aprill'
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