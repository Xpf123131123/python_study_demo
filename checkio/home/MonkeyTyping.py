"""

"""
import re
def count_words_my(text, words):
    count = 0
    text = text.lower()
    for word in words:
        search = re.search(r'.*{}.*'.format(word), text, re.S)
        if search:
            count += 1
    return count

def count_words(text, words):
    return sum(map(lambda word: int(word.lower() in text.lower()), words))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")