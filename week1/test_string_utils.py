# week1/test_string_utils.py
import pytest
from string_utils import *

# 1-3: reverse_string tests
def test_reverse_string_standard(): assert reverse_string("abc") == "cba"
def test_reverse_string_empty(): assert reverse_string("") == ""
def test_reverse_string_none(): 
    with pytest.raises(TypeError): reverse_string(None)

# 4-6: count_vowels tests
def test_count_vowels_standard(): assert count_vowels("Hello") == 2
def test_count_vowels_all_caps(): assert count_vowels("AEIOU") == 5
def test_count_vowels_none_input():
    with pytest.raises(TypeError): count_vowels(None)

# 7-9: is_palindrome tests
def test_is_palindrome_simple(): assert is_palindrome("racecar") is True
def test_is_palindrome_sentence(): assert is_palindrome("A man a plan a canal Panama") is True
def test_is_palindrome_false(): assert is_palindrome("hello") is False

# 10-12: word_count tests
def test_word_count_standard(): assert word_count("Hello World") == 2
def test_word_count_extra_spaces(): assert word_count("  spaces  ") == 1
def test_word_count_empty(): assert word_count("") == 0

# 13-15: capitalise_words tests
def test_capitalise_words_standard(): assert capitalise_words("hello world") == "Hello World"
def test_capitalise_words_already_caps(): assert capitalise_words("HELLO") == "Hello"
def test_capitalise_words_single(): assert capitalise_words("a") == "A"

# 16-18: remove_duplicates tests
def test_remove_duplicates_consecutive(): assert remove_duplicates("aaabbbcc") == "abc"
def test_remove_duplicates_long(): assert remove_duplicates("aaaaa") == "a"
def test_remove_duplicates_none_consecutive(): assert remove_duplicates("abc") == "abc"