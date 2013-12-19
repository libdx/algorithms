map = [
  [4, 4, 4, 4],
  [4, 4, 3, 3],
  [5, 4, 4, 4],
  [2, 4, 4, 3],
  ]

#  [5, 4, 4],
#  [3, 4, 3],
#  [5, 5, 3],
#  [2, 5, 4],
#  [4, 3, 0],
#  [3, 3, 2]

def to_row(cols, idx):
    return idx / cols

def to_col(cols, idx):
    return idx % cols

def to_idx(cols, row, col):
    return cols * row + col

visited = []
rows = len(map)
cols = len(map[0])
areas = 0
calls = 0

def traversal(row, col):
    global visited, rows, cols, areas, calls

    calls += 1

    if to_idx(cols, row, col) in visited:
        return

    val = map[row][col]
    west = None
    south = None
    if col < cols - 1:
        west = map[row][col + 1]
    if row < rows - 1:
        south = map[row + 1][col]

    if val == west and to_idx(cols, row, col + 1) not in visited:
        traversal(row, col + 1)
    elif val == south and to_idx(cols, row + 1, col) not in visited:
        traversal(row + 1, col)
    else:
        areas += 1

    visited.append(to_idx(cols, row, col))
    return

if __name__ == '__main__':
    for row in xrange(rows):
        for col in xrange(cols):
            traversal(row, col)
    print "areas: %d" % areas
    print "visited idx: %s" % visited
    print "visited [row, col]: %s" % [[to_row(cols, x), to_col(cols, x)] for x in visited]
    print "calls: %d" % calls

