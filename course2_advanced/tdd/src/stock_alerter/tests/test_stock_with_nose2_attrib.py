from datetime import datetime

def test_stock_update(self):
    self.goog.update(datetime(2014, 2, 12), price=10)
    self.assertEqual(10, self.goog.price)
    
test_stock_update.slow = True
test_stock_update.integration = True
test_stock_update.python = ["2.6", "3.4"]