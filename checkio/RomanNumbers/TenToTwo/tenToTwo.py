
def tenToTwo(p):
    while p:
        p, rep = divmod(p, 2)
        print(rep, p)
    return 0

if __name__ == '__main__':
    assert tenToTwo(2) == 11
    assert tenToTwo(9) == 1001
    assert tenToTwo(59) == 111011
    assert tenToTwo(120) == 1111000
    assert tenToTwo(1234) == 10011010010
