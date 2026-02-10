# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

<!-- exercise 1 -->
user wants to verify that start letter of text has a capital letter
and ends with suitable sentence ending punctuation mark


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

# def extract_uppercase(mixed_words):
#     """Extracts uppercase words from a string

    # Parameters: (list all parameters and their types)
#         mixed_words: a string containing words (e.g. "hello WORLD")

#     Returns: (state the return value and its type)
#         a list of strings, each one a word (e.g. ["WORLD"])

#     Side effects: (state any side effects)
#         This function doesn't print anything or have any other side-effects
#     """
#     pass # Test-driving means _not_ writing any code here yet.

def check_grammar(text):
    """ Verifys first lettter in text is capitalized
    and end letter has suitable punctuation mark
    """

    Paramters: 
        text as a string
    Returns:
        a string confirming checks have been made, including result
        and error 

    Side effects: None

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a sentence with capital start letter and suitable 
punctuation, return "no grammar problenms"
"""
check_grammar("Hello world.") => "No grammar problems"

"""
Given string with no uppercase letter and no punctation
return: "Grammar error, no capital letter and punctuation detected"
"""
check_grammar("hello world") => "Grammar error, no capital letter and punctuation detected"

"""
Given string with capitalised letter and no punctuation
return: "Incorrect punctuation detected"
"""
check_grammar("Hello world") => "Incorrect punctuation detected"


"""
given string with no capital letter and correct punctuation
return: "No capital letter detected"
"""
check_grammar("hello world.") => "No capital letter detected"
```









_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
