class LongestWord:

    def __int__(self):
        pass

    """This method will take a sentence as an argument and find the longest word 
    out of it and return its length and the word
    """
    @staticmethod
    def find_longest_word(sentence):
        if not sentence:
            raise Exception("Sentence should not be empty")
        else:
            longest = max(sentence.split(), key=len)

        return longest