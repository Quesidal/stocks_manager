from providers.users_storage import JsonUserStorage
from repositories.entity.users import User


class UsersPortfolioRepository:
    @classmethod
    def get_user(cls, user_id) -> User:
        return JsonUserStorage.load(user_id)
