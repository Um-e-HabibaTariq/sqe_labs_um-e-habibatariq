# week1/string_utils.py

def count_vowels(text: str) -> int:
    """Returns the count of vowel characters (case-insensitive)."""
    if text is None: raise TypeError("Input cannot be None") # Requirement for Exception Handling 
    return sum(1 for char in text.lower() if char in 'aeiou')

def reverse_string(text: str) -> str:
    """Returns the string in reversed order."""
    if text is None: raise TypeError("Input cannot be None")
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """Returns True if text reads the same forwards and backwards."""
    if text is None: raise TypeError("Input cannot be None")
    cleaned = "".join(text.split()).lower()
    return cleaned == cleaned[::-1]

def word_count(text: str) -> int:
    """Returns the number of words separated by whitespace."""
    if text is None: raise TypeError("Input cannot be None")
    return len(text.split())

def capitalise_words(text: str) -> str:
    """Capitalises the first letter of each word."""
    if text is None: raise TypeError("Input cannot be None")
    return text.title()

def remove_duplicates(text: str) -> str:
    """Removes consecutive duplicate characters."""
    if text is None: raise TypeError("Input cannot be None")
    if not text: return ""
    result = [text[0]]
    for char in text[1:]:
        if char != result[-1]:
            result.append(char)
    return "".join(result)