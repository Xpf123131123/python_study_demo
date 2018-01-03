def numberToRoman(p):
    roman  = ['M',   'CM',   'D',    'CD',   'C',    'XC',   'L',    'XL',   'X',    'IX',   'V',    'IV',   'I']
    number = [1000,   900,    500,    400,    100,    90,     50,     40,     10,     9,      5,      4,      1]

    str = ''
    for i in number:
        rep, p = divmod(p, i)
        str += ''.join(roman[number.index(i)] * rep)

    return str



if __name__ == '__main__':
    assert numberToRoman(3999) == 'MMMCMXCIX'