from enum import Enum

class Roman(Enum):
    M  = 1000
    CM = 900
    D  = 500
    CD = 400
    C  = 100
    XC = 90
    L  = 50
    XL = 40
    X  = 10
    IX = 9
    V  = 5
    IV = 4
    I  = 1

    @classmethod
    def encode(cls, n):
        for numeral in cls:
            print(cls)
            print(numeral)
            rep, n = divmod(n, numeral.value)
            yield numeral.name * rep

checkio = lambda n: ''.join(Roman.encode(n))


if __name__ == '__main__':
    assert checkio(3999) == 'MMMCMXCIX'