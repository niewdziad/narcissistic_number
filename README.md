# narcissistic_number

def narcissistic(test_number):
Definiuje funkcję narcissistic, która przyjmuje jeden argument test_number, reprezentujący liczbę do sprawdzenia, czy jest liczbą narcystyczną.
#
    num_str = str(test_number)
Konwertuje podaną liczbę na ciąg znaków za pomocą funkcji str(). To umożliwia iterację po cyfrach tej liczby.
#
    num_digits = len(num_str)
Oblicza liczbę cyfr w podanej liczbie, korzystając z funkcji len() na ciągu znaków reprezentującym tę liczbę.
#
    narcissistic_sum = sum(int(digit) ** num_digits for digit in num_str)
Oblicza sumę narcystyczną, podnosząc każdą cyfrę liczby do potęgi liczby cyfr i sumując wyniki. Wykorzystuje tutaj listę składaną.
#
    return narcissistic_sum == test_number
Zwraca True, jeśli obliczona suma narcystyczna jest równa podanej liczbie, a w przeciwnym przypadku zwraca False.
#
print(narcissistic(7))     # True
print(narcissistic(371))   # True
print(narcissistic(122))   # False
print(narcissistic(4887))  # False
Wywołuje funkcję narcissistic dla różnych liczb i drukuje wynik, aby zweryfikować poprawność działania funkcji.