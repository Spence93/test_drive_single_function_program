# from lib.check_grammar import check_grammar
# import pytest

# """
# Given a sentence with capital start letter and suitable 
# punctuation, return "no grammar problenms"
# """

# def test_check_grammar_returns_correct():
#     actual = check_grammar("Hello world.")
#     expected = "No grammar problems!"

#     assert actual == expected


# """
# Given string with no uppercase letter and no punctation
# return: "Grammar error, no capital letter and punctuation detected"
# """
# def test_check_grammar_returns_wrong_captial_and_punctuation():
#     actual = check_grammar("hello world") 
#     expected = "Grammar error, no capital letter and punctuation detected"    

#     assert actual == expected


# """
# Given string with capitalised letter and no punctuation
# return: "Incorrect punctuation detected"
# """
# def test_grammar_returns_wrong_with_capital_no_punctuiation():
#     actual = check_grammar("Hello world")
    
#     assert actual == "Incorrect punctuation detected"        

# """
# given string with no capital letter and correct punctuation
# return: "No capital letter detected"
# """

# def test_grammar_returns_wrong_with_no_capital_with_punct():
#     actual = check_grammar("hello world.") 

#     assert actual == "No capital letter detected" 


# """
# given a non string, check exeption is raised
# return exception
# """    
# def test_input_is_a_string():
#     with pytest.raises(Exception) as err:
#         check_grammar(5)
#     error_message = str(err.value)
#     assert error_message == "Not a string!"
