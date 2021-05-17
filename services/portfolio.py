from repositories.entity.users import User, Positions
from use_cases.all_time_return import CalculateAllTimeReturn
from use_cases.last_day_return import CalculateLastDayReturn


class PortfolioInfoService:
    @classmethod
    def execute(cls, user: User) -> dict:
        positions_info = {stock.ticker: cls._build_stock_info(stock) for stock in user.positions}
        summarize_info = cls._build_portfolio_summarize(positions_info)
        return positions_info, summarize_info

    @staticmethod
    def _build_stock_info(stock: Positions):
        last_usd, last_percent = CalculateLastDayReturn.run(stock_ticker=stock.ticker,
                                                            count=stock.count)
        all_usd, all_percent = CalculateAllTimeReturn.run(stock_ticker=stock.ticker,
                                                          count=stock.count,
                                                          buy_price=stock.buy_price)
        return {'last_day_return_usd': last_usd,
                'last_day_return_percent': last_percent,
                'all_time_return_usd': all_usd,
                'all_time_return_percent': all_percent}

    @staticmethod
    def _build_portfolio_summarize(positions_info: dict):
        summary_return_usd = 0
        summary_return_percent = 0

        for stock_info in positions_info.values():
            summary_return_usd += stock_info['all_time_return_usd']
            summary_return_percent += stock_info['all_time_return_percent']

        summary_return_percent = round(summary_return_percent / len(positions_info), 3)
        return {'summary_return_percent': summary_return_percent,
                'summary_return_usd': summary_return_usd}
