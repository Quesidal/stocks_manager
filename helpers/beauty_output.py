class TelegramPortfolioMessage:

    @classmethod
    def create_message(cls, portfolio_info: dict, summarize_info: dict) -> str:
        output = f'Portfolio info \n'

        for ticker, stock_info in portfolio_info.items():
            output += f'{ticker} ' \
                      f'{stock_info["last_day_return_usd"]} ' \
                      f'{stock_info["last_day_return_percent"]} ' \
                      f'{stock_info["all_time_return_usd"]} ' \
                      f'{stock_info["all_time_return_percent"]}' \
                      f'\n'

        output += f'\n*Summarize*\n' \
                  f'{summarize_info["summary_return_usd"]}usd {summarize_info["summary_return_percent"]}% '

        return output

    @classmethod
    def create_message_html(cls, portfolio_info: dict, summarize_info: dict) -> str:
        output = f'Portfolio info \n'

        output += "<pre>"
        tmp = "|{:<7}" * 5
        output += tmp.format(*('Ticker', 'rd, usd', 'rd, %', 'ra, usd', 'ra, %'))
        output += '\n'

        for ticker, stock_info in portfolio_info.items():
            tmp = "|{:<7}" * 5
            tmp += '\n'
            output += tmp.format(ticker, *stock_info.values())
        output += "</pre>"

        output += f'\n<b>Summarize</b>\n' \
                  f'All time return:  ' \
                  f'{summarize_info["summary_return_usd"]}usd ' \
                  f'{summarize_info["summary_return_percent"]}% '

        return output
