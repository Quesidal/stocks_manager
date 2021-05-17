import logging

from repositories.stocks_info import StocksInfoRepository

logger = logging.getLogger('business')


class CalculateLastDayReturn:
    @classmethod
    def run(cls, stock_ticker: str, count: int):
        return_percent, return_usd = StocksInfoRepository.get_last_day_return(stock_ticker)
        return_percent = round(return_percent * 100., 3)
        return_usd = round(return_usd * count, 3)
        logger.info(f'{stock_ticker} last day return calculated {return_percent}% {return_usd}usd')
        return return_usd, return_percent
