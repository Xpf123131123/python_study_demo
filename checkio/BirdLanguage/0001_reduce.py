import functools

VOWELS = "aeiouy"

def translate(phrase):
    return functools.reduce(lambda res, ch: res.replace(ch*3, ch*2), VOWELS, phrase).replace(' ', '  ')[::2]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"