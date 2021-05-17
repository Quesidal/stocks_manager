from helpers.beauty_output import TelegramPortfolioMessage
from providers.telegram_bot import TelegramBot
from repositories.users_info import UsersPortfolioRepository
from services.portfolio import PortfolioInfoService


class EveryDayReporter:
    @classmethod
    def run(cls, user_id: int):
        user = UsersPortfolioRepository.get_user(user_id)

        positions_info, summarize_info = PortfolioInfoService.execute(user)
        message = TelegramPortfolioMessage.create_message_html(positions_info, summarize_info)

        TelegramBot.send_message(message=message,
                                 user_id=user.chat_id)
