"""
You are building the e-commerce platform and you need to display a daily deal to a user. 
Write a program that defines the following variables for the deal:

store_name - Bookstore
product_name - Book "Learn Python now!"
product_price - 29.99
product_discount - 0.2

The program should then calculate the item's reduced price by the specified discount 
and print a message to the console containing this information. 
The message should be formatted as follows:

    Welcome to Bookstore!
    ----------------------------------------
    Today's special offer is the Book "Learn Python now!", which normally costs $ 29.99.
    But for a limited time, you can get it for $23.99 (20% off)!
    ----------------------------------------

Remember to round price to the second decimal place.
The boundary lines consist of 40 '-' characters.
"""

store_name = 'Bookstore'
product_name = 'Book "Learn Python now!"'
product_price = 29.99
product_discount = 0.2
line = 40 * '-'
new_price = product_price - (product_price * product_discount)

print(f'Welcome to {store_name}')
print(line)
print(f'Today\'s special offer is the {product_name}, which normally costs $ {product_price}.')
print(f'But for a limited time, you can get it for $ {new_price:.2f} ({product_discount * 100}% off)!')
print(line)