from unittest import TestCase, skip

from providers.finance_data.yahoo import YahooFinance


class YahooFinanceProviderTestCase(TestCase):
    @skip("long time")
    def test_get_qqq_info(self):
        data = YahooFinance.get_stock_info('qqq')
        self.assertEqual(data['symbol'], 'QQQ')
