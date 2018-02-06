matrix = [[1, 0, 1, 1, 0, 1, 0],
          [1, 1, 1, 1, 0, 1, 0],
          [0, 0, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 0, 1, 0],
          [1, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 0, 0, 1, 0],
          [1, 1, 1, 0, 0, 0, 1]]

i = 0
for j in range(1, len(matrix)):
    if matrix[i][j] == 1:
        i = j  

answer = True
for j in range(len(matrix)):
    if matrix[j][i] == 0:
        answer = False
        break
if answer == True:        
    for j in range(len(matrix)):
        if matrix[i][j] == 1 and j != i:
            answer = False
            break
if answer == True:
    print('Wow! Guest №{} is a star!'.format(i+1))
else:
    print('There is no star at the party.')
