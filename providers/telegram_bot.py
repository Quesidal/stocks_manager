import logging

from telegram import Bot

from config import TELEGRAM_BOT_TOKEN

logger = logging.getLogger('provider')


class TelegramBot:
    _bot = None

    @classmethod
    def bot(cls):
        if cls._bot is None:
            cls._bot = Bot(token=TELEGRAM_BOT_TOKEN)
            logger.info(f'Telegram bot was initialized with id: {cls._bot.id}')
        return cls._bot

    @classmethod
    def send_message(cls, message: str, user_id: int):
        cls.bot().send_message(chat_id=user_id, text=message, parse_mode="HTML")
        logger.info(f'Telegram message was sent to chat: {user_id}')
