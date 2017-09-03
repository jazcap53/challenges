from data import DICTIONARY, LETTER_SCORES
import nose

def load_words(dictionary=DICTIONARY):
    """Load dictionary into a list and return list"""
    with open(dictionary) as infile:
        return [line.strip() for line in infile]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    ttl = 0
    for letr in word:
        try:
            ttl += LETTER_SCORES[letr.upper()]
        except KeyError:
            continue
    return ttl

def max_word_value(words_arg=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    words = words_arg if words_arg else load_words()
    max_ttl = 0
    max_word = ''
    for word in words:
        val = calc_word_value(word)
        if val > max_ttl:
            max_ttl = val
            max_word = word
    # print('max word is {} with value {}'.format(max_word, max_ttl))
    return max_word

if __name__ == "__main__":
    nose.run() # run unittests to validate
