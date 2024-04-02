import telebot
from django.conf import settings
from forbot.bot.queries import (
    add_user,
    format_text,
    get_all_vacancies,
    get_offers,
    get_requirements,
    get_template,
    get_user,
)

from .keyboards import markup, markup_welcome

telebot.logger.setLevel(settings.LOG_LEVEL)
bot = telebot.TeleBot(settings.TOKEN)


@bot.message_handler(commands=["help", "start"])
def send_welcome(message):
    """
    Функция, которая активируется при команде '/start'.
    Проверяет: есть ли этот пользователь в бд или нет,
    если нет, то записывает в бд.
    Затем отправляет соответствующее сообщение с кнопками
    под самим сообщением.
    """
    chat_id = message.chat.id
    user = get_user(chat_id)
    if user:
        old_user_text = get_template("старый пользователь")
        bot.send_message(
            chat_id,
            text=old_user_text,
            reply_markup=markup_welcome,
        )
    else:
        new_user_text = get_template("новый пользователь")
        add_user(chat_id)
        bot.send_message(
            chat_id,
            text=new_user_text,
            reply_markup=markup_welcome,
        )


@bot.callback_query_handler(func=lambda call: call.data.startswith("respond_"))
def callback_query(call):
    """
    Функция, которая срабатывает
    при нажатии кнопки button_respond('Откликнуться').
    Читает переменную title в аргументе callback_data и передает ее в текст для
    обозначения на что откликнулись.
    Отправляет этот тексту в определенный чат,
    а пользователю отправляет сообщение,
    что все отправилось и передает стартовые кнопки - markup_welcome.
    """
    text_for_user = "Отлично! Мы вас услышали, скоро с вами свяжемся!"

    title = call.data.split("_", 1)[1]
    username = call.message.chat.username

    contact_text = f"Пришел отклик!\n\nUsername: @{username}"
    if title != "":
        contact_text += f",\nВакансия: {title}"

    if call.message.chat.first_name:
        name = call.message.chat.first_name
        contact_text += f",\nИмя: {name}"

    bot.send_message(chat_id=settings.ADMIN_ID, text=contact_text)
    bot.send_message(
        call.message.chat.id,
        text=text_for_user,
        reply_markup=markup_welcome,
    )


@bot.callback_query_handler(func=lambda call: call.data == "career")
def callback_center_career(call):
    """
    Функция, которая срабатывает
    при нажатии кнопки button_career('Центр карьеры').
    Отправляет описание центра карьеры и кнопку button_respond.
    """
    center_career_text = get_template("центр карьеры")
    text = center_career_text
    title = "Центр карьеры"
    bot.send_message(
        call.message.chat.id,
        text=text,
        reply_markup=markup(title),
    )


@bot.callback_query_handler(func=lambda call: call.data == "vacancies")
def callback_vacancies(call):
    """
    Функция, которая срабатывает
    при нажатии кнопки button_vacancies('Ваканасии').
    Отправляет по сообщению с каждой вакансией и кнопкой button_respond.
    """
    vacancies = get_all_vacancies()
    if len(vacancies) <= 0:
        bot.send_message(
            call.message.chat.id,
            text="Доступных вакансий нету :(",
            reply_markup=markup_welcome,
        )
    else:
        bot.send_message(
            call.message.chat.id,
            text="Вот список доступных вакансий",
        )

        for current_vacancy in vacancies:
            title = current_vacancy.title
            text_requirements = get_requirements(current_vacancy.id)
            text_offers = get_offers(current_vacancy.id)
            text = format_text(title, text_requirements, text_offers)
            bot.send_message(
                call.message.chat.id,
                text=text,
                parse_mode="HTML",
                reply_markup=markup(title=title),
            )
