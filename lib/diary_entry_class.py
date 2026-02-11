class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.index_counter = 0

    def format(self):
        return f"{self.title}: {self.contents}"


    def count_words(self):
        if not isinstance(self.contents, str) or not isinstance(self.title, str):
            raise Exception("Only a string can be called as the argument")

        string_list = self.contents.split(" ")
        word_count = len(string_list)
        return word_count


    def reading_time(self, wpm):
        book_length = len(self.contents.split())
        time = wpm / book_length
        return time

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.

        word_count = self.count_words()
        words_read = int(wpm * minutes)
        string_list = self.contents.split(" ")

        return_string = " ".join(string_list[self.index_counter: words_read + self.index_counter])
        self.index_counter += words_read
        
        if self.index_counter >= word_count:
            self.index_counter = 0
        
        return return_string

diary = DiaryEntry("Book1", "This is the contents of a book yes")
diary.reading_chunk(2,2)
print(diary.reading_chunk(2,2))