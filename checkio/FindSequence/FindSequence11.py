import re
def checkio(matrix):
    diag1 = list(zip(*[[" "]*i + matrix[i] + [" "]*(len(matrix)-i-1) for i in range(len(matrix))]))
    diag2 = list(zip(*[[" "]*(len(matrix)-i-1) + matrix[i] + [" "]*i for i in range(len(matrix))]))
    matrices = [list(map(lambda x: "".join(list(map(str, x))), m)) for m in [matrix, list(zip(*matrix)), diag1, diag2]]
    return bool(sum([sum([bool(re.findall(r"1{4}|2{4}|3{4}|4{4}|5{4}|6{4}|7{4}|8{4}|9{4}", row)) for row in m]) for m in matrices]))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True, "Vertical"
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False, "Nothing here"
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True, "Long Horizontal"
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    assert checkio([
        [1, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 2, 1, 1, 4],
        [4, 6, 5, 1, 1, 1],
        [1, 1, 9, 1, 2, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    print('you win')