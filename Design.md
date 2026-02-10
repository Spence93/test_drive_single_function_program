<!-- <!-- Design

A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.
 -->
<!-- 

Design

A function called count_words that takes a string as an argument and returns the number of words in that string. -->
<!-- ------------------------------------------------------------------------------------------ -->


# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
<!-- exercise 1 -->
The user wishes to see an estimate of their reading time for a text, 
this assumes they can read 200 words per minute


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```
<!-- exercise 1 -->
'''python

estimate_reading_time(WPM, text):
""" calculates users estimated reading time for current text

    Parameters: the text they are currently reading
        text = str
    Returns: Reading time estimatation = Float e.g 60.5 minutes

    Side effects: No side effects
    pass
"""

'''

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._
<!-- Exerise 1 -->

"""
given a text of 200 words
It will return a reading time of 1
"""
estimate_reading_time("200words) 
## => 1.0


'''
give a text oof 100 words
returns 0.5
'''
estimate_reading_time(1000words) 
=> 0.5


"""
given an empty string
should return 0
"""
estimate_reading_time("")
=> 0 








```python
# EXAMPLE
"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
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

Ensure all test function names are unique, otherwise pytest will ignore them! -->


# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
<!-- exercise 2 -->
user wants to verify that a text starts with a capital letter
and ends with suitable sendtence ending punctuation mark


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def extract_uppercase(mixed_words):
    """Extracts uppercase words from a string

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello WORLD")

    Returns: (state the return value and its type)
        a list of strings, each one a word (e.g. ["WORLD"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```
<!-- exercise 1 -->
'''python

estimate_reading_time(WPM, text):
""" calculates users estimated reading time for current text

    Parameters: the text they are currently reading
        text = str
    Returns: Reading time estimatation = Float e.g 60.5 minutes

    Side effects: No side effects
    pass
"""

'''

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._
<!-- Exerise 1 -->

"""
given a text of 200 words
It will return a reading time of 1
"""
estimate_reading_time("200words) 
## => 1.0


'''
give a text oof 100 words
returns 0.5
'''
estimate_reading_time(1000words) 
=> 0.5


"""
given an empty string
should return 0
"""
estimate_reading_time("")
=> 0 








```python
# EXAMPLE
"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

"""
Given two lowercase words
It returns an empty list
"""
extract_uppercase("hello world") => []

"""
Given a lower and a mixed case word
It returns an empty list
"""
extract_uppercase("hello WoRLD") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
extract_uppercase("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
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
