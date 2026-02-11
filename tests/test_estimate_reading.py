# from lib.estimate_reading_time import estimate_reading_time

# """
# given a text of 200 words
# It will return a reading time of 1
# """
# two_hundred = "one " * 199 
# def test_estimate_reading_time_200():
#     actual = estimate_reading_time(two_hundred) 
#     expected = 1.0

#     assert actual == expected

# """
# given 100 words
# retunrs reading time of 0.5
# """
# one_hundred = "one " * 99
# def test_estimate_reading_time_100():
#     actual = estimate_reading_time(one_hundred) 
#     expected = 0.5

#     assert actual == expected

# """
# given 400 words
# returns 2
# """
# def test_estimate_reading_time_400():
#     actual = estimate_reading_time("one " * 399)
#     expected = 2

#     assert actual == expected


# """
# given 300 words
# returns 2
# """
# def test_estimate_reading_time_300():
#     actual = estimate_reading_time("one " * 299)
#     expected = 1.5

#     assert actual == expected



# """
# given an empty string
# should return 0
# """
# def test_estimate_reading_time_empty_string_Return_0():
#     actual = estimate_reading_time("")
#     expected = 0

#     assert actual == expected
