import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from forbot.bot.main_bot import bot

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Запускаем бота"

    def handle(self, *args, **options):
        try:
            bot.infinity_polling(logger_level=settings.LOG_LEVEL)
        except Exception as err:
            logging.error(f"Ошибка: {err}")
