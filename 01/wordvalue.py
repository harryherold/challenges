from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        return [word.strip() for word in file.readlines()]

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES.get(c, 0) for c in word.upper()])

def max_word_value(wordlist=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    # max returns the item of wordlist and determine max by function calc_word_value
    return max(wordlist or load_words(), key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
