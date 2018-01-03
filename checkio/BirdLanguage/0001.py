'''
Vowels letters == "aeiouy".

The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Precondition: 
- re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)

规则:
1.非元音字母会随机携带一个元音字母(l ⇒ la or le)
2.元音字母会重复出现三次(a ⇒ aaa)
提示:
re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
'''
import re
VOWELS = "aeiouy"

def translate(phrase):



    for i in VOWELS:
        s = '' + i + '{3}'
        phrase = re.sub(s, i,phrase)

    print(phrase)
    p = re.findall('[^aeiouy ][aeiouy]', phrase)
    print(p)
    p1 = []
    for i in p:
        if i not in p1:
            p1.append(i)
    print(p1)
    for i in p1:
        phrase = re.sub(i, i[0] + '-', phrase)
        print(phrase)

    return phrase.replace('-', '')


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzuziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa") == "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"