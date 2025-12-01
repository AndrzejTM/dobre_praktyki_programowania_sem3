"""
Moduł zawierający implementacje funkcji do testowania jednostkowego.
"""
import re
from typing import List, Dict


def is_palindrome(text: str) -> bool:
    """
    Sprawdza, czy dany ciąg znaków jest palindromem (ignorując wielkość liter i spacje).

    Args:
        text: Ciąg znaków do sprawdzenia

    Returns:
        True jeśli tekst jest palindromem, False w przeciwnym razie
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    """
    Zwraca n-ty element ciągu Fibonacciego.
    fibonacci(0) = 0, fibonacci(1) = 1

    Args:
        n: Indeks elementu ciągu Fibonacciego

    Returns:
        n-ty element ciągu Fibonacciego

    Raises:
        ValueError: Jeśli n < 0
    """
    if n < 0:
        raise ValueError("n musi być nieujemne")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(text: str) -> int:
    """
    Zlicza liczbę samogłosek w podanym ciągu (a, e, i, o, u, y).
    Wielkość liter bez znaczenia.

    Args:
        text: Tekst do przeanalizowania

    Returns:
        Liczba samogłosek w tekście
    """
    vowels = "aeiouyąęó"  # polskie samogłoski też uwzględnione
    return sum(1 for char in text.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    """
    Zwraca cenę po uwzględnieniu zniżki.

    Args:
        price: Cena początkowa
        discount: Zniżka jako wartość z zakresu [0, 1]

    Returns:
        Cena po zastosowaniu zniżki

    Raises:
        ValueError: Jeśli discount jest spoza zakresu [0, 1]
    """
    if discount < 0 or discount > 1:
        raise ValueError("Zniżka musi być w zakresie [0, 1]")

    return price * (1 - discount)


def flatten_list(nested_list: list) -> list:
    """
    Przyjmuje listę (mogącą zawierać zagnieżdżone listy) i zwraca ją spłaszczoną.

    Args:
        nested_list: Lista potencjalnie zawierająca zagnieżdżone listy

    Returns:
        Spłaszczona lista
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result


def word_frequencies(text: str) -> dict:
    """
    Zwraca słownik z częstością występowania słów w tekście
    (ignorując wielkość liter i interpunkcję).

    Args:
        text: Tekst do przeanalizowania

    Returns:
        Słownik z częstością występowania słów
    """
    if not text:
        return {}

    # Usuwamy interpunkcję i dzielimy na słowa
    words = re.findall(r'\b\w+\b', text.lower())

    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies


def is_prime(n: int) -> bool:
    """
    Sprawdza, czy liczba jest pierwsza.

    Args:
        n: Liczba do sprawdzenia

    Returns:
        True jeśli liczba jest pierwsza, False w przeciwnym razie
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # Sprawdzamy dzielniki do sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True