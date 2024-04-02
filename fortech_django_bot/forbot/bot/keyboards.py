from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


class MyButtonRespond(InlineKeyboardButton):
    def __init__(
        self,
        title: str,
        text="Откликнуться",
        url=None,
        callback_data=None,
        web_app=None,
        switch_inline_query=None,
        switch_inline_query_current_chat=None,
        switch_inline_query_chosen_chat=None,
        callback_game=None,
        pay=None,
        login_url=None,
        **kwargs,
    ):
        super().__init__(
            text,
            url,
            callback_data,
            web_app,
            switch_inline_query,
            switch_inline_query_current_chat,
            switch_inline_query_chosen_chat,
            callback_game,
            pay,
            login_url,
            **kwargs,
        )
        self.title = title
        self.callback_data = f"respond_{self.title}"


def markup(title: str):
    button = MyButtonRespond(title=title)
    return InlineKeyboardMarkup().add(button)


button_career = InlineKeyboardButton("Центр карьеры", callback_data="career")
button_vacancies = InlineKeyboardButton("Вакансии", callback_data="vacancies")
button_respond = MyButtonRespond(title="")

markup_welcome = (
    InlineKeyboardMarkup().add(button_respond, button_vacancies).row(button_career)
)
