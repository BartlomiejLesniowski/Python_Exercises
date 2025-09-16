"""Ćwiczenie 6

Załóżmy, że budujesz witrynę e-commerce i musisz wyświetlić użytkownikowi szczegóły produktu.
Napisz program, który wyświetla na ekranie nazwę produktu, cenę i stan dostępności.


Zdefiniuj w tym celu poniższe zmienne:

    product_name
    price
    in_stock


Do podanych zmiennych przypisz odpowiednio poniższe wartości:

    'Shoe'
    49.99
    True

Następnie wykorzystując zdefiniowane zmienne wydrukuj do konsoli szczegóły produktu tak jak poniżej.

Oczekiwany wynik:

    Product Name: Shoe
    Price: $ 49.99
    Is Available: True

"""

product_name = 'Shoe'
price = 49.99
in_stock = True

# %%
print(f' Product Name: {product_name}\n Price $ {price}\n Is Available: {in_stock}')

# OR
#%%

print('Product Name:', product_name)
print('Price: $', price)
print('Is Available:', in_stock)
