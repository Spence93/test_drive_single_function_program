class GrammarStats:
    def __init__(self):
        self.check_pass = 0
        self.check_fail = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        
        punct_list = [".","!","?"]
        if not isinstance(text,str):
            raise Exception("Not a string!")
        elif text[0].isupper() and text[-1] in punct_list:
            print( "No grammar problems!" )
            self.check_pass += 1
            return True
        elif text[0].isupper():
            print( "Incorrect punctuation detected")
            self.check_fail += 1
            return False
        elif text[-1] in punct_list:
            print( "No capital letter detected")
            self.check_fail += 1
            return False
        
        self.check_fail += 1
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        total_passed = self.check_pass
        total_failed = self.check_fail
        total = total_failed + total_passed

        percentage = (total_passed / total) * 100

        return percentage