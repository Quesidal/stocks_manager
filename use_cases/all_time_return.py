import logging

from repositories.stocks_info import StocksInfoRepository

logger = logging.getLogger('business')


class CalculateAllTimeReturn:
    @classmethod
    def run(cls, stock_ticker: str, count: int, buy_price: float):
        today_price = StocksInfoRepository.get_today_stock_price(stock_ticker)
        time_return_usd = round((today_price - buy_price) * count, 3)
        time_return_percent = round(time_return_usd / (buy_price * count) * 100, 3)
        logger.info(f'{stock_ticker} all time return calculated')
        return time_return_usd, time_return_percent
