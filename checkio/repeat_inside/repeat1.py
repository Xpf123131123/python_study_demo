def repeat_inside(line):
    """
        first the longest repeating substring
    """

    def longest_repeat(i, d, s):
        if i + d <= len(line) and line[i:i + d] == s:
            return s + longest_repeat(i + d, d, s)
        else:
            return ''

    list = []
    for i in range(len(line)):
        for j in range(i, len(line)):
            d = j - i + 1
            str = longest_repeat(i, d, line[i:i + d])
            if str == line[i:i + d] or str in list:
                continue
            list.append(str)
    return max(list, key=lambda x:len(x)) if len(list) else ''

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert repeat_inside('aaaaa') == 'aaaaa', "First"
    assert repeat_inside('aabbff') == 'aa', "Second"
    assert repeat_inside('aababcc') == 'abab', "Third"
    assert repeat_inside('abc') == '', "Forth"
    assert repeat_inside('abcabcabab') == 'abcabc', "Fifth"
    print('"Run" is good. How is "Check"?')