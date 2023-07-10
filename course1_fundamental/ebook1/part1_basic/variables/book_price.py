book_price = 24.95
discount = 40/100
shipping_cost_first_copy = 3
shipping_cost_additional_copy = 0.75

book_price_after_discount = book_price - (book_price * discount)

total_cost = (book_price_after_discount * 60) + (59 * shipping_cost_additional_copy) + shipping_cost_first_copy

print(total_cost)