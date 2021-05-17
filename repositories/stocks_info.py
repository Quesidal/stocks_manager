from typing import Tuple

from providers.finance_data.yahoo import YahooFinance


class StocksInfoRepository:
    @classmethod
    def get_today_stock_price(cls, stock_ticker: str) -> float:
        data = YahooFinance.get_history_data(stock_ticker)
        return data.tail(1)['Close'].iloc[0]

    @classmethod
    def get_last_day_return(cls, stock_ticker: str) -> Tuple[float, float]:
        data = YahooFinance.get_history_data(stock_ticker)
        start = data.tail(3)['Close'].iloc[0]
        end = data.tail(3)['Close'].iloc[1]
        return (end - start) / start, end - start
