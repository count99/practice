#coding="utf-8"

def count_neighbours(grid, row, col):
    get_list = [list(x) for x in grid]
    get_row = [x for x in range(row-1, row+2) if x>=0 and x<len(grid)]
    get_col = [x for x in range(col-1, col+2) if x>=0 and x<len(grid[0])]
    get_list[row][col]=0
    get_answer = [get_list[x][y] for x in get_row for y in get_col]
    count=0
    for i in range(len(get_answer)):
        if get_answer[i] == 1:
            count += 1
    return count
   
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
