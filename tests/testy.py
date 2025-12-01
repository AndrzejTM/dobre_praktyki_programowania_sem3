"""
Testy jednostkowe dla modułu functions.py
Uruchomienie: pytest tests/test_functions.py
"""
import pytest
from funkcje import (
    is_palindrome,
    fibonacci,
    count_vowels,
    calculate_discount,
    flatten_list,
    word_frequencies,
    is_prime
)


class TestIsPalindrome:
    """Testy dla funkcji is_palindrome"""

    def test_simple_palindrome(self):
        assert is_palindrome("kajak") == True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("Kobyła ma mały bok") == True

    def test_not_palindrome(self):
        assert is_palindrome("python") == False

    def test_empty_string(self):
        assert is_palindrome("") == True

    def test_single_character(self):
        assert is_palindrome("A") == True


class TestFibonacci:
    """Testy dla funkcji fibonacci"""

    def test_fibonacci_zero(self):
        assert fibonacci(0) == 0

    def test_fibonacci_one(self):
        assert fibonacci(1) == 1

    def test_fibonacci_five(self):
        assert fibonacci(5) == 5

    def test_fibonacci_ten(self):
        assert fibonacci(10) == 55

    def test_fibonacci_negative(self):
        with pytest.raises(ValueError):
            fibonacci(-1)


class TestCountVowels:
    """Testy dla funkcji count_vowels"""

    def test_count_vowels_python(self):
        assert count_vowels("Python") == 1

    def test_count_vowels_all(self):
        assert count_vowels("AEIOUY") == 6

    def test_count_vowels_none(self):
        assert count_vowels("bcd") == 0

    def test_count_vowels_empty(self):
        assert count_vowels("") == 0

    def test_count_vowels_polish(self):
        assert count_vowels("Próba żółwia") == 4


class TestCalculateDiscount:
    """Testy dla funkcji calculate_discount"""

    def test_discount_20_percent(self):
        assert calculate_discount(100, 0.2) == 80.0

    def test_discount_zero(self):
        assert calculate_discount(50, 0) == 50.0

    def test_discount_100_percent(self):
        assert calculate_discount(200, 1) == 0.0

    def test_discount_negative(self):
        with pytest.raises(ValueError):
            calculate_discount(100, -0.1)

    def test_discount_above_one(self):
        with pytest.raises(ValueError):
            calculate_discount(100, 1.5)


class TestFlattenList:
    """Testy dla funkcji flatten_list"""

    def test_flatten_simple_list(self):
        assert flatten_list([1, 2, 3]) == [1, 2, 3]

    def test_flatten_nested_list(self):
        assert flatten_list([1, [2, 3], [4, 5]]) == [1, 2, 3, 4, 5]

    def test_flatten_empty_list(self):
        assert flatten_list([]) == []

    def test_flatten_single_element(self):
        assert flatten_list([1]) == [1]

    def test_flatten_deeply_nested(self):
        assert flatten_list([1, [2, [3]], 4]) == [1, 2, 3, 4]


class TestWordFrequencies:
    """Testy dla funkcji word_frequencies"""

    def test_word_frequencies_simple(self):
        result = word_frequencies("To be or not to be")
        assert result == {"to": 2, "be": 2, "or": 1, "not": 1}

    def test_word_frequencies_case_insensitive(self):
        result = word_frequencies("Hello, hello!")
        assert result == {"hello": 2}

    def test_word_frequencies_empty(self):
        result = word_frequencies("")
        assert result == {}

    def test_word_frequencies_same_word(self):
        result = word_frequencies("Python Python python")
        assert result == {"python": 3}

    def test_word_frequencies_with_punctuation(self):
        result = word_frequencies("Ala ma kota, a kot ma Ale.")
        assert result == {"ala": 1, "ma": 2, "kota": 1, "a": 1, "kot": 1, "ale": 1}


class TestIsPrime:
    """Testy dla funkcji is_prime"""

    def test_is_prime_two(self):
        assert is_prime(2) == True

    def test_is_prime_three(self):
        assert is_prime(3) == True

    def test_is_prime_four(self):
        assert is_prime(4) == False

    def test_is_prime_zero(self):
        assert is_prime(0) == False

    def test_is_prime_one(self):
        assert is_prime(1) == False

    def test_is_prime_five(self):
        assert is_prime(5) == True

    def test_is_prime_large(self):
        assert is_prime(97) == True