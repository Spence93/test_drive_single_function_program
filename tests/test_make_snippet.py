from lib.make_snippit import make_snippit
import pytest # pyright: ignore[reportMissingImports]


"""
Check function returns string with 5 words and no dots
"""
def test_snippit_is_first_5_words_with_no_dots():
    actual = make_snippit("hello world here are more")
    expected = "hello world here are more"

    assert actual == expected



"""
given a string with length 5 or less, the string is returned
"""
def test_snippit_returns_string_correctly_5_chars_or_less():
    actual = make_snippit("hello")
    expected = "hello"

    assert actual == expected



"""
given a string with more than 5 words, 5 words are returns with ...
"""
def test_string_returns_more_than_5_words_with_elipses():
    actual = make_snippit("one two three four five six")
    expected = "one two three four five..."

    assert actual == expected




"""
Checks string is in arguemnt, and that an exception is raises
"""
def test_input_is_a_string_with_exception_raised():
    with pytest.raises(Exception) as err:
        make_snippit(5)
    error_message = str(err.value)
    assert error_message == "Error raised, arguemnt only takes string input"   