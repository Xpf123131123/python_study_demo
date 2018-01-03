import re
VOWELS = "aeiouy"

def translate(phrase):
    phrase = re.sub(r'([^'+VOWELS+r'\s])['+VOWELS+']',r'\1',phrase)
    phrase = re.sub(r'(['+VOWELS+r'])\1{2}',r'\1',phrase)
    return phrase

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"