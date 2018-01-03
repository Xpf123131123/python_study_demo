def romanToNumber(str):
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    p = 0
    _break = False
    for i in range(len(str)):
        if _break:
            _break = False
            continue
        if i + 1 < len(str) and str[i:i+2] in roman:
            p += number[roman.index(str[i:i+2])]
            _break = True
        elif str[i] in roman:
            p += number[roman.index(str[i])]

    return p



if __name__ == '__main__':
    assert romanToNumber('VI') == 6
    assert romanToNumber('LXXVI') == 76
    assert romanToNumber('CDXCIX') == 499
    assert romanToNumber('MMMDCCCLXXXVIII') == 3888