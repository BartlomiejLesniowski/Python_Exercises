"""Ćwiczenie 7

Załóżmy, że budujesz program do obliczania rachunku za energię 
elektryczną dla gospodarstwa domowego. Napisz program, 
który obliczy całkowity koszt energii elektrycznej na podstawie 
liczby zużytych jednostek oraz kosztu jednostkowego 
i wyświetli wynik na ekranie tak jak poniżej.


Zdefiniuj w tym celu poniższe zmienne:
    units_used - służy do przechowywania liczby zużytych 
                 jednostek energii elektrycznej
    cost_per_unit - służy do przechowywania kosztu za 
                    jednostkę energii elektrycznej

Do podanych zmiennych przypisz odpowiednio poniższe wartości:

    150
    0.15

Oblicz całkowity koszt energii elektrycznej, który jest obliczany 
przez pomnożenie liczby zużytych jednostek przez koszt jednostkowy 
i przypisz do zmiennej o nazwie total_cost. 
Wynik wydrukuj do konsoli tak jak poniżej.

Oczekiwany wynik:

    units used: 150
    cost per unit: $ 0.15
    total cost: $ 22.5"""

units_used = 150
cost_per_unit = 0.15
total_cost = units_used * cost_per_unit

print('units used:', units_used)
print('cost per unit: $', cost_per_unit)
print('total cost: $', total_cost)
