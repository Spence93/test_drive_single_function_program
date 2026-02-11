# from lib.diary_entry_class import DiaryEntry
# import pytest


# # Class Init
# """
# check that class inits correctly with both arguments passed in 
# """
# def test_diary_entry_inits():
#     diary = DiaryEntry("Lord of the rings", "book1")
#     title = diary.title
#     contents = diary.contents

#     assert title == "Lord of the rings"
#     assert contents == "book1"


# # Format()
# """
# given the correct title and contents, check the correctly formatted
# diary entry is created within format function
# """
# def test_diary_format_is_correct():
#     diary = DiaryEntry("Lord of the rings", "book1")
#     actual = diary.format()
#     expected = "Lord of the rings: book1"

#     assert actual == expected


# # count_words()
# """
# given the correct inputs, check that the correct output is given
# from the count_words function
# """    
# def test_diary_count_words_returns_correct():
#     diary = DiaryEntry("Book1", "This is the contents of a book")
#     actual = diary.count_words()
#     expected = 7

#     assert actual == expected

# """
# give the wrong aruments when the class is instantiated, check that
# an exception is raised
# """
# def test_diary_count_words_exception_raised_with_wrong_args():

#     with pytest.raises(Exception) as err:
#         diary = DiaryEntry( "book1" , 5)
#         diary.count_words()    
#     error_message = "Only a string can be called as the argument"
    
#     assert error_message == "Only a string can be called as the argument"



# # reading_time
# """
# given the correct arguemnts, ensure correct result is returned
# using reading_time function
# """    
# def test_diary_reading_time_function_returns_correct():
#     diary = DiaryEntry("Book1", "This is the contents of a book")
#     actual = diary.reading_time(7)
#     expected = 1

#     assert actual == expected




# # reading_chunk
# """
# given the correct arguements, for wpm and minutes
# test that correct portions of the contents are returnd based off
# of the calculation and acts as intended
# """
# def test_reading_chunk_returns_correct_values_one_call():
#     diary = DiaryEntry("Book1", "This is the contents of a book yes")
#     # book1_words = diary.count_words()
#     # book1_read_time = diary.reading_time(2)

#     actual = diary.reading_chunk(1, 4)
#     expected = "This is the contents"

#     assert actual == expected

# """
# given correct arguemnts, check correct values are returned after calling 
# function twice
# """

# def test_diary_reading_chunk_returns_correct_two_calls():
#     diary = DiaryEntry("Book1", "This is the contents of a book yes")
#     # book1_words = diary.count_words()
#     # book1_read_time = diary.reading_time(2)

#     first = diary.reading_chunk(2, 2)
#     seccond = diary.reading_chunk(2, 2)
#     expected = "of a book yes"

#     assert seccond == expected