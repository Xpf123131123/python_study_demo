def longest_palindromic(text):

    def p1(i): return i == i[::-1]
    def p2(i): return p1(i[1])

    def longest(text, ind):
        if 1 == len(text): return (ind, text)
        if p1(text):       return (ind, text)
        r    = range(1+ind, 1+ind + len(text))
        sub  = [(ind, text[:i-ind]) for i in r]
        sub  = [(a, b) for (a, b) in sub if b[0] == b[-1]]
        sub  = list(filter(p2, sub))
        sub  = sub + [longest(text[1:], ind+1)]
        sub  = sorted(sub, key=lambda x:len(x[1]))
        a, b = sub[-1]
        blen = len(b)
        sub  = list(filter(lambda x: len(x[1]) == blen, sub))
        sub  = sorted(sub, key=lambda x:x[0])
        return sub[0]

    return longest(text, 0)[1]