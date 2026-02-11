from lib.grammar_class import GrammarStats
import pytest
"""
Given a sentence with capital start letter and suitable 
punctuation, return "no grammar problenms"
"""

def test_check_grammar_returns_correct():
    check_grammar = GrammarStats()

    actual = check_grammar.check("Hello world.")
    expected = True

    assert actual == expected


"""
given string with no capital letter and correct punctuation
return: "No capital letter detected"
"""

def test_grammar_returns_wrong_with_no_capital_with_punct():
    check_grammar = GrammarStats()
    actual = check_grammar.check("hello world.") 

    assert actual == False

"""
given a non string arguemnt, an exception is caught correctly

"""    
def test_grammar_catches_exception():
    check_grammar = GrammarStats()

    with pytest.raises(Exception) as err:
        check_grammar.check(5)

    err_message = str(err.value)
    assert err_message == "Not a string!"

"""
given a number of passed and failed grammar checks.
Ensure return value is a correct percentage of passed grammar checks.
"""
def test_grammar_percentage_good_func_returns_correct_80():
    grammar = GrammarStats()
    grammar.check("Hello world.")
    grammar.check("Hi world.")
    grammar.check("Hello!")
    grammar.check("Hi!")
    grammar.check("hello world")
    actual = grammar.percentage_good()
    assert actual == 80

"""
given a number of passed and failed grammar checks.
Ensure return value is a correct percentage of passed grammar checks.
"""
def test_grammar_percentage_good_func_returns_correct_100():
    grammar = GrammarStats()
    grammar.check("Hello world.")
    grammar.check("Hi world.")
    grammar.check("Hello!")
    actual = grammar.percentage_good()
    assert actual == 100    

"""
given a number of passed and failed grammar checks.
Ensure return value is a correct percentage of passed grammar checks.
"""
def test_grammar_percentage_good_func_returns_correct_20():
    grammar = GrammarStats()
    grammar.check("Hello world")
    grammar.check("Hi world")
    grammar.check("Hello")
    grammar.check("Hi!")
    grammar.check("hello world")
    actual = grammar.percentage_good()
    assert actual == 20


"""
given a number of passed and failed grammar checks.
Ensure return value is a correct percentage of passed grammar checks.
"""
def test_grammar_percentage_good_func_returns_correct_0():
    grammar = GrammarStats()
    grammar.check("hello world")
    actual = grammar.percentage_good()
    assert actual == 0