def substrings(string):
    l = len(string)
    for n in range(l, 0, -1):
        for i in range(l - n + 1):
            yield string[i:n+i]

def longest_palindromic(string):
    return next(sub for sub in substrings(string) if sub == sub[::-1])