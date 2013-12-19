MAP = [
#  0  1  2  3
#  [4, 4, 4, 4], # 0
#  [4, 4, 3, 3], # 1
#  [5, 4, 3, 3], # 2
#  [2, 4, 4, 4], # 3

#  0  1  2
  [5, 4, 4], # 0
  [3, 4, 3], # 1
  [5, 5, 3], # 2
  [2, 5, 4], # 3
  [4, 3, 0], # 4
  [3, 3, 2]  # 5

    ]

def to_row(COLS, idx):
    return idx / COLS

def to_col(COLS, idx):
    return idx % COLS

def to_idx(COLS, row, col):
    return COLS * row + col

visited = []
ROWS = len(MAP)
COLS = len(MAP[0])
areas = 0
calls = 0

def traversal(row, col):
    global visited, areas, calls

    calls += 1

    if to_idx(COLS, row, col) in visited:
        return

    visited.append(to_idx(COLS, row, col))

    val = MAP[row][col]
    west = None
    east = None
    south = None
    if col < COLS - 1:
        west = MAP[row][col + 1]
    if col > 0:
        east = MAP[row][col - 1]
    if row < ROWS - 1:
        south = MAP[row + 1][col]

    if val == west and to_idx(COLS, row, col + 1) not in visited:
        traversal(row, col + 1)
    # for traversal element at left-bottom position
    if val == east and to_idx(COLS, row, col - 1) not in visited:
        traversal(row, col - 1)
    if val == south and to_idx(COLS, row + 1, col) not in visited:
        traversal(row + 1, col)

    return

import sys

if __name__ == '__main__':
    for row in xrange(ROWS):
        for col in xrange(COLS):
            if to_idx(COLS, row, col) not in visited:
                areas += 1
                visited.append(None) #tmp
                traversal(row, col)

    print "areas: %d" % areas

    if '-debug' in sys.argv:
        print "visited idx: %s" % visited
        print map(lambda x: [to_row(COLS, x), to_col(COLS, x)] if x is not None else None, visited)
        print "calls: %d" % calls


