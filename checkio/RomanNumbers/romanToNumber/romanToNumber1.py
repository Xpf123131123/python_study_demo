# ------------------------------------------ #
def reverse_roman(roman_string):
    N = 'IVXLCDM'
    roman = [5 ** ((N.index(ch) + 1) // 2) * 2 ** (N.index(ch) // 2) for ch in roman_string]
    return sum(-x if x < y else x for x, y in zip(roman, roman[1:]+[0]))

# ------------------------------------------ #
def reverse_roman1(roman):
    m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    r=0
    for i in range(len(roman)):
        r+=m[roman[i]]*(1 if i==len(roman)-1 or m[roman[i]]>=m[roman[i+1]] else -1)
    return r

# ------------------------------------------ #
from operator import add
from functools import reduce
from itertools import zip_longest


def reverse_roman2(roman_string):
    #replace this for solution
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if roman_string:
        return reduce(add, ((-d[x], d[x])[y is None or d[x] >= d[y]] for x, y in
                            zip_longest(roman_string, roman_string[1:])))

# ------------------------------------------ #
reverse_roman3=lambda n,f='IVXLCDM'.index:sum((1,5)[f(i)%2]*10**(f(i)//2)*(-1,1)[f(i)>=f(j)]for i,j in zip(n,n[1:]+n[-1]))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');