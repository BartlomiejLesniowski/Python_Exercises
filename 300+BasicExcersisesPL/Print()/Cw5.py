"""Do zmiennej price przypisz cenę produktu równą 69.99 PLN 
oraz do zmiennej discount przypisz wartość 0.1 (zniżka 10%). 
Następnie policz cenę tego produktu po zastosowaniu podanej 
zniżki. Wynik wydrukuj do konsoli tak jak pokazano poniżej. 
Zwróć uwagę na odpowiednie formatowanie tekstu w funkcji 
print() tak, aby końcowa cena produktu została wyświetlona 
tylko do drugiego miejsca po przecinku."""

price = 69.99
discount = 0.1
deducted_amount = price*discount
new_price = price - deducted_amount

print(deducted_amount)
print(f'The new price is equal to: {new_price:.2f}')
print(f'rounded deducted amount is equal to {deducted_amount:.2f}.')
