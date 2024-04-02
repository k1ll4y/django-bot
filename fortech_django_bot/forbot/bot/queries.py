from forbot.bot.models import Offer, Requirement, TemplateText, User, Vacancy


def get_user(external_id: int) -> User:
    """Получить пользователя по его id в телеграмме"""
    return User.objects.filter(external_id=external_id)


def add_user(external_id: int) -> None:
    """Добавляет пользователя в бд по его id в телеграмме"""
    user = User(external_id=external_id)
    user.save()


def update_template(name: str, new_text: str) -> None:
    """
    Обновляет шаблонный текст, передавая в качестве аргумента,
    его название и новый текст
    """
    name = name.lower()
    TemplateText.objects.filter(name=name).update(text=new_text)


def get_template(name: str) -> str:
    """Получить шаблонный текст по его названию"""
    name = name.lower()
    result = TemplateText.objects.filter(name=name).values("text")
    if result:
        return result[0]["text"]
    return "Отсутствует текст"


def get_all_vacancies():
    """Получить все вакансии"""
    return Vacancy.objects.all()


def get_requirements(vacancy_id: int):
    """
    Получить все тексты требований, связанные с одной вакансией и
    преобразует их в одну строку.
    Аргументом является id вакансии.
    """
    requirements = Requirement.objects.filter(vacancy__id=vacancy_id).values(
        "description"
    )
    requirements_list = [requirement["description"] for requirement in requirements]
    return ";\n- ".join(map(str, requirements_list))


def get_offers(vacancy_id: int):
    """
    Получить все тексты предложений, связанные с одной вакансией и
    преобразует их в одну строку.
    Аргументом является id вакансии.
    """
    offers = Offer.objects.filter(vacancy__id=vacancy_id).values("description")
    offers_list = [offer["description"] for offer in offers]
    return ";\n- ".join(map(str, offers_list))


def format_text(title, text_requirements, text_offers):
    """
    Приводит требования и предложения в один красивый текст
    """
    return (
        f"<b>{title}</b>\n"
        "\n<b>Что от тебя требуется</b>:"
        f"\n- {text_requirements}.\n"
        f"\n<b>Что мы предлагаем:</b>:"
        f"\n- {text_offers}.\n"
    )
