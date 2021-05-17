import logging

import environ

env = environ.Env()

TELEGRAM_BOT_TOKEN = env.str('TELEGRAM_BOT_TOKEN')
INFORMATION_TIME = env.str('INFORMATION_TIME')  # when bot send msg to you
USER_ID = env.int('USER_ID')
PATH_TO_USERS_PORTFOLIO_INFO = env.str('PATH_TO_USERS_PORTFOLIO_INFO')

for logger_name in ('provider', 'business', 'controller', 'schedule'):
    logger = logging.getLogger(logger_name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel('INFO')
