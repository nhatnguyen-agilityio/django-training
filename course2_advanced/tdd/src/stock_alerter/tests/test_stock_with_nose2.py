from nose2.tools.params import params
from datetime import datetime

from ..stock import Stock

def setup_test():
    global goog
    goog = Stock("GOOG")

def teardown_test():
    global goog
    goog = None

def test_price_of_a_new_stock_class_should_be_None():
    assert goog.price is None, "Price of a new stock should be None"
    
test_price_of_a_new_stock_class_should_be_None.setup = setup_test
test_price_of_a_new_stock_class_should_be_None.teardown = teardown_test

def given_a_series_of_prices(stock, prices):
    timestamps = [datetime(2014, 2, 10), datetime(2014, 2, 11), datetime(2014, 2, 12), datetime(2014, 2, 13)]
    for timestamp, price in zip(timestamps, prices):
        stock.update(timestamp, price)

@params(
([8, 10, 12], True),
([8, 12, 10], False),
([8, 10, 10], False)
)
def test_stock_trends(prices, expected_output):
    goog = Stock("GOOG")
    given_a_series_of_prices(goog, prices)
    assert goog.is_increasing_trend() == expected_output