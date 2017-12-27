longest_palindromic = lambda inp: "".join(next(t for n in range(len(inp), 0, -1) for t in zip(*(__import__("itertools").islice(inp, i, None) for i in range(n))) if t == t[::-1]))


# python2.7
longest_palindromic1 = lambda text: filter(lambda x: len(x) == max(list(map(len, [char for char in [text[index:i] for index in range(len(text)) for i in range(index, len(text)+1) if text[index:i] == text[index:i][::-1]]]))), [char for char in [text[index:i] for index in range(len(text)) for i in range(index, len(text)+1) if text[index:i] == text[index:i][::-1]]])[0]

longest_palindromic2=l=lambda t:t*(t==t[::-1])or max(l(t[:-1]),l(t[1:]),key=len)
