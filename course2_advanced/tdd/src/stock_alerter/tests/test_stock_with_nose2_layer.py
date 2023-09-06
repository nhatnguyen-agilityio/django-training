from datetime import datetime
from nose2.tools import such

from ..stock import Stock

# define the top topmost layer using the such.A method
# such.A takes a string as a parameter
# The output of such.A is assigned to a variable
with such.A("Stock class") as it:

    # create the setup function for the layer
    # mark it as the setup function by decorating it with the has_setup decorator
    # This decorator is a method of the it object, hence we write @it.has_setup
    @it.has_setup
    # The name of the function can be anything
    def setup():
        # we can store any stateful information as attributes of the it object
        it.goog = Stock("GOOG")

    # create a test case
    # The "should" decorator takes a description string which explains the test
    @it.should("return the price")
    def test(case):
        assert it.goog.price == 10

    @it.should("return the latest price")
    def test(case):
        it.goog.update(datetime(2014, 2, 11), price=15)
        assert it.goog.price == 10

with it.having("a trend method"):
    @it.should("return True if last three updates were increasing")
    def test(case):
        it.goog.update(datetime(2014, 2, 11), price=12)
        it.goog.update(datetime(2014, 2, 12), price=13)
        it.goog.update(datetime(2014, 2, 13), price=14)
        assert it.goog.is_increasing_trend()

# we call the createTests method to convert all this code into test cases
# The createTests method should be called at the end of the topmost layer. It takes a single parameter of the current globals.
it.createTests(globals())