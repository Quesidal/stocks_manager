import logging
from typing import Union

import yfinance as yf
from pandas import DataFrame, Series

logger = logging.getLogger('provider')


class YahooFinance:
    @classmethod
    def get_stock_info(cls, stock_ticker: str) -> dict:
        logger.info(f'Start downloading stock: {stock_ticker} info')
        stock = yf.Ticker(stock_ticker)
        stock_info = stock.info
        logger.info(f'Downloaded stock: {stock_ticker} info. Stock price: {stock_info["navPrice"]}')
        return stock_info

    @classmethod
    def get_history_data(cls, stock_ticker: str) -> Union[DataFrame, Series]:
        logger.info(f'Start downloading stock: {stock_ticker} info')
        stock = yf.Ticker(stock_ticker)
        data = stock.history()
        return data
