def count_words(string_input):
    if not isinstance(string_input, str):
        raise Exception("Only a string can be called as the argument")


    string_list = string_input.split(" ")
    word_count = len(string_list)
    return word_count

