'''def creatmatrix(n):
    matrix = []
    for i in range(2*n-1):
        add = []
        for j in range(2*n-1):
            add.append(0)
        matrix.append(add)
    return matrix
def xx(n,m):
    b = 0
    numm = m
    for x in range(n, 0,-1):
        for i in range( 2 * x -1):
            for j in range( 2 * x-1 ):
                    matrix[i+b][j+b] = numm[b]
        b += 1
    return matrix
def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end =' ')
        print()
def cho1():
    odd = []
    even = []
    for i in range(1,n+1):
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    numcho = odd+even
    return xx(n,numcho)
def cho2():
    odd = []
    even = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    numcho = even+odd
    return xx(n, numcho)

n = int(input('Input the maze\'s size (only 1 to 9): '))
f = int(input('Input the type of maze (only 1 to 2): '))
matrix = creatmatrix(n)
if f == 1:
    print_matrix(cho1())
else:
    print_matrix(cho2())
'''
