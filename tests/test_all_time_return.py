from unittest import TestCase
from unittest.mock import patch

from use_cases.all_time_return import CalculateAllTimeReturn


class IEXStocksProviderTestCase(TestCase):
    @patch('repositories.stocks_info.StocksInfoRepository.get_today_stock_price',
           lambda *args: 315.73)
    def test_a(self):
        return_usd, return_percent = CalculateAllTimeReturn.run(stock_ticker='QQQ',
                                                                count=10,
                                                                buy_price=314.28)

        self.assertEqual(return_usd, 14.5)
        self.assertEqual(return_percent, 0.461)
