def rotate_right(grid):
    rgrid = []
    for y in range(len(grid[0])):
        add = []
        for x in range(len(grid)-1,-1,-1):
            add.append(grid[x][y])
        rgrid.append(add)
    return rgrid
def rotate_left(grid):
    lgrid = []
    for y in range(len(grid[0])-1,-1,-1):
        add = []
        for x in range(len(grid)):
            add.append(grid[x][y])
        lgrid.append(add)
    return lgrid
def rotate_180(grid):
    mirror = rotate_right(rotate_right(grid))
    return mirror
def mirror(grid):
    mirror = []
    for y in range(len(grid)-1,-1,-1):
        add = []
        for x in range(len(grid[0])-1,-1,-1):
            add.append(grid[y][x])
        mirror.append(add)
    return mirror
def print_grid(grid):
    for x in range(len(grid)) :
        for y in range(len(grid[0])):
            print(grid[x][y],end ='')
        print()
grid1 = [['.','.','.','.','.','.'],
         ['.','o','o','.','.','.'],
         ['o','o','o','o','.','.'],
         ['o','o','o','o','o','.'],
         ['.','o','o','o','o','o'],
         ['o','o','o','o','o','.'],
         ['o','o','o','o','.','.'],
         ['.','o','o','.','.','.'],
         ['.','.','.','.','.','.']]
grid2 = [['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','o','.','o'],
         ['o','o','.','o','.','o','.'],
         ['o','o','o','o','o','.','.'],
         ['o','o','.','o','.','o','.'],
         ['.','.','.','.','o','.','o'],
         ['.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.']]
grid3 = [[' ',' ',' ',' ','o','o',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' '],
         [' ','o','o','o',' ',' ','o',' ',' ',' ','o'],
         ['o',' ',' ',' ','o',' ','o',' ',' ','o',' '],
         ['o',' ',' ',' ','o','o','o','o','o',' ',' '],
         ['o',' ',' ',' ','o',' ','o',' ',' ','o',' '],
         [' ','o','o','o',' ',' ','o',' ',' ',' ','o'],
         [' ',' ',' ',' ',' ',' ','o',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ','o','o',' ',' ']]
grid = mirror(rotate_left(grid1))
print_grid(grid)
