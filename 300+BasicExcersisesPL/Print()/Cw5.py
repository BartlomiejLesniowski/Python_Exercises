"""
Create two variables price and discount (10%) that will store the following strings, respectively:
    69.99
    0.1
Then print the following message to the console.

    The new price is equal to 62.99.
    
Remember to round price to the second decimal place.
"""

price = 69.99
discount = 0.1
deducted_amount = price*discount
new_price = price - deducted_amount


print(f'The new price is equal to: {new_price:.2f}.')
