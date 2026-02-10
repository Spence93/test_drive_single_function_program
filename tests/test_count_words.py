from lib.count_words import count_words
import pytest
"""
check that the string argument is returned as expected
"""
def test_count_with_only_one_word():
    actual = count_words("hello")
    expected = 1

    assert actual == expected


"""
Check correct result with multiple words in a string
"""
def test_count_with_multiple_words():
    actual = count_words("hello there this is a string")
    expected = 6

    assert actual == expected


"""
check that exception is raised when non string argument called
"""
def test_count_words_catches_non_string_error():
    with pytest.raises(Exception) as err:
        count_words(5)
    error_message = str(err.value)    

    assert error_message == "Only a string can be called as the argument"