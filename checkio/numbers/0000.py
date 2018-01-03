class memorize:
    dict = {}
    def __init__(self, f):
        self.dict = {}
        self._f = f

    def __call__(self, *args, **kwargs):
        if args[0] in self.dict:
            return self.dict[args[0]]
        else:
            self.dict[args[0]] = self._f(*args, **kwargs)
            return self.dict[args[0]]

@memorize
def res(number):
    l = []
    for i in range(2, number):

        if number % i == 0:
            l.append([i, number // i])

    if len(l) >= 1: return l
    return 0

def checkio1(number):
    list1 = res(number)
    if not list1:
        return 0
    for i, p in enumerate(list1):
        for index, p1 in enumerate(p):
            l = res(p1)
            if not l: continue
            ls = list1[i].copy()
            ls.remove(p1)
            for q in l:
                ls1 = ls.copy()
                ls1 += q
                if ls1 not in list1:
                    list1.append(ls1)

    list2 = []
    for i in list1:
        if len(''.join([str(j) for j in i])) == len(i):
            list2.append(int(''.join([str(j) for j in i])))
            pass

    if not len(list2): return 0
    s = sorted(list2)
    return s[0]

print('9999', checkio(9999))

def checkio(left):
    ans = []
    for i in reversed(range(2,10)):
        while left % i ==0:
            print(left)
            left = left/i
            ans.append(str(i))
    if ans == [] or left > 9:
        return (0)
    else:
        return int(''.join(reversed(ans)))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(20) == 45, "1st example"#45
    assert checkio(21) == 37, "2nd example"#37
    assert checkio(17) == 0, "3rd example"
    assert checkio(33) == 0, "4th example"
    assert checkio(3125) == 55555, "5th example"
    assert checkio(9973) == 0, "6th example"
