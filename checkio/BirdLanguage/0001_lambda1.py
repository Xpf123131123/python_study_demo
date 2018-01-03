import re
translate = lambda phrase : " ".join(["".join([token[0] for token in re.findall("[^%s][%s]|[%s]{3}"%(("aeiouy",)*3), word)]) for word in phrase.split(" ")])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"