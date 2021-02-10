from sentence_exercise.src.longest_word_task import LongestWord

SENTENCE = "The cow jumped over the moon."


"""this test method is going to test the longest word in sentence"""


def test_longest_word():
    longest_word = LongestWord.find_longest_word(SENTENCE)
    assert "jumped" == longest_word, f"Longest word is: {longest_word}"


"""this test method is going to test the length of the word in sentence"""


def test_length_of_word():
    longest_word = LongestWord.find_longest_word(SENTENCE)
    length = len(longest_word)
    assert length == 6, f"Length is: {length}"