def checkio(matrix):
    print(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(4):
                if sdk(matrix,i,j,1,k)>3:
                    return True
    else:
        return False

def sdk(matrix,i,j,S,k):
    if S > 3:
        return 4
    Li = len(matrix)-1
    Lj = len(matrix[j])-1
    print(S,'[',k,']','i=',i,Li,'j=',j,Lj,matrix[i][j])
    if i < Li and j > 0 and k == 0:
        if matrix[i+1][j-1] == matrix[i][j]:
            S = sdk(matrix, i + 1, j - 1, S+1,k)
    if i < Li and k == 1:
        if matrix[i+1][j] == matrix[i][j]:
            S = sdk(matrix, i + 1, j, S+1,k)
    if i < Li and j < Lj and k == 2:
        if matrix[i+1][j+1] == matrix[i][j]:
            S = sdk(matrix, i + 1, j + 1, S+1,k)
    if  j < Lj and k == 3:
        if matrix[i][j+1] == matrix[i][j]:
            S = sdk(matrix, i, j + 1, S+1,k)
    return S

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
        [1, 1, 9, 1, 2, 1]
    ]) == True, "Diagonal"
    print('you win')