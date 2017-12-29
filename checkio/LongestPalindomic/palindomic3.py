def longest_palindromic(line):
    if line:
        for i in range(len(line), 0, -1):
            for j in range(len(line)-i+1):
                if all([line[j:j+i][charIndex]== line[j:j+i][-charIndex-1] for charIndex in range(len(line[j:j+i]))]):
                    return line[j:j+i]
    else:
        return ''

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"