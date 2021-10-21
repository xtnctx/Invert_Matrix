m = [[0,0,0],
     [0,0,0],
     [0,0,0,0],
     [0,0,0,0]]

n = [[1,1,1],
     [1,1,1],
     [1,1,1]]

""" invert a 2D matirx """
def invert(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 0:
                matrix[row][column] = 1
            else:
                matrix[row][column] = 0
    return matrix
    

print(invert(n))
        

