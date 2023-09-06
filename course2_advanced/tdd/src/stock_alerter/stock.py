import bisect
from datetime import timedelta
from enum import Enum

from .timeseries import TimeSeries, MovingAverage
from .event import Event

class StockSignal(Enum):
    buy = 1
    neutral = 0
    sell = -1

class Stock:
    LONG_TERM_TIMESPAN = 10
    SHORT_TERM_TIMESPAN = 5
    def __init__(self, symbol):
        self.symbol = symbol
        self.history = TimeSeries()
        self.updated = Event()

    @property
    def price(self):
        try:
            return self.history[-1].value
        except IndexError:
            return None

    def update(self, timestamp, price):
        if price < 0:
            raise ValueError("price should not be negative")
        self.history.update(timestamp, price)

    def is_increasing_trend(self):
        return self.history[-3].value < self.history[-2].value < self.history[-1].value

    def _is_crossover_below_to_above(self, on_date, ma, reference_ma):
        prev_date = on_date - timedelta(1)
        return (ma.value_on(prev_date) < reference_ma.value_on(prev_date) and ma.value_on(on_date) > reference_ma.value_on(on_date))

    def get_crossover_signal(self, on_date):
        long_term_ma = MovingAverage(self.history, self.LONG_TERM_TIMESPAN)
        short_term_ma = MovingAverage(self.history, self.SHORT_TERM_TIMESPAN)

        if self._is_crossover_below_to_above(on_date, short_term_ma, long_term_ma):
            return StockSignal.buy
        
        if self._is_crossover_below_to_above(on_date, long_term_ma, short_term_ma):
            return StockSignal.sell
        
        return StockSignal.neutral
    

def price(self):
    """Returns the current price of the Stock
    >>> from datetime import datetime
    >>> stock = Stock("GOOG")
    >>> stock.update(datetime(2011, 10, 3), 10)
    >>> stock.price
    The method will return the latest price by timestamp, so even
    if updates are out of order, it will return the latest one
    >>> stock = Stock("GOOG")
    >>> stock.update(datetime(2011, 10, 3), 10)
    Now, let us do an update with a date that is earlier than the
    previous one
    >>> stock.update(datetime(2011, 10, 2), 5)
    And the method still returns the latest price
    >>> stock.price
    10
    If there are no updates, then the method returns None
    >>> stock = Stock("GOOG")
    >>> print(stock.price)
    None
    """
    try:
        return self.history[-1].value
    except IndexError:
        return None
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
