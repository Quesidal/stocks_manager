import json
from typing import Dict

from config import PATH_TO_USERS_PORTFOLIO_INFO
from repositories.entity.users import User


class JsonUserStorage:
    DB_FPATH = PATH_TO_USERS_PORTFOLIO_INFO

    @classmethod
    def load(cls, user_id: int) -> User:
        return cls._load_all_users()[user_id]

    @classmethod
    def _load_all_users(cls) -> Dict[int, User]:
        with open(cls.DB_FPATH, 'r') as db:
            raw_data = json.load(db)
        return {int(user_id): User.from_dict(user) for user_id, user in raw_data.items()}
