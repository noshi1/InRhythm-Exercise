from sentence_exercise.src.longest_word_task import LongestWord
import logging as logger

SENTENCE = "The cow# jumped1 1!@ over the moon 09[]noshee"
print(logger.info("Testing a sentence for longest word."))

"""this test method is going to test the longest word in sentence"""


def test_longest_word_01():
    longest_word = LongestWord.find_longest_word(SENTENCE)
    assert "jumped" == longest_word, f"Longest word is: {longest_word}"


"""this test method is going to test the length of the word in sentence"""


def test_length_of_word_02():
    longest_word = LongestWord.find_longest_word(SENTENCE)
    length = len(longest_word)
    assert length == 6, f"Length is: {length}"


"""This test method test if sentence have any numbers."""


def test_numbers_in_sentence_03():
    longest_word = LongestWord.find_longest_word(SENTENCE)
    assert f"Sentence should not have numbers: {longest_word}"


"""This test method will check it sentence contains any special characters."""


def test_special_char_in_sentence_04():
    longest_word = LongestWord.find_longest_word(SENTENCE)
    assert f"Sentence should not contain special characters: {longest_word}"


"""This test method will check if sentence if empty."""


def test_null_sentence_05():
    LongestWord.find_longest_word(SENTENCE)
    assert f"There must be a sentence of words"
