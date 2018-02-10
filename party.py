'''element [i][j] = 1 if "i" knows "j" '''
def test():
    matrix1 = [[1, 0, 1, 1, 0, 0, 0],
               [1, 1, 1, 0, 0, 1, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 1, 0],
               [1, 0, 1, 1, 1, 1, 0],
               [0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 0, 0, 1]]
    assert find_star(matrix1) == 2

def test_no_star():
    matrix1 = [[1, 0, 0, 1, 0, 0, 0],
               [1, 1, 1, 0, 0, 1, 0],
               [0, 0, 1, 0, 0, 0, 0],
               [1, 1, 1, 1, 0, 1, 0],
               [1, 0, 1, 1, 1, 1, 0],
               [0, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 0, 0, 0, 1]]
    assert find_star(matrix1) == -1

def find_star(matrix):
    n = len(matrix)
    # If m[i][j] = 1, "i" isn't a star. If m[i][j] = 0, "j" isn't a star.
    # Let's go through all values of j, considering the pairs (i,j).
    # And "x" will be assigned by numbers which can still be a star.
    i = 0
    for j in range(1, n):
        if matrix[i][j]:
            i = j
    s = i # Star?
    # Now let's check that all elements in column "s" =1 and 
    # that all elements in row "s" =0 except element [s][s].
    if all(matrix[i][s] for i in range(n)) and not matrix[s].count(1)-1:
        return s
    else:
        return -1
