def tuplize_matrix(matrix):
    return tuple(tuple(row) for row in matrix)

class WDState:

    def __init__(self, max_row_sums, ncols, matrix):
        self.__max_row_sums = tuple(max_row_sums)
        self.__ncols = ncols
        self.__matrix = tuplize_matrix(matrix)
    
    def __eq__(self, other):
        return self.__matrix == other.__matrix

    def __hash__(self):
        return hash(self.__matrix)

    def __repr__(self):
        return repr(self.__matrix)

    def __str__(self):
        return str(self.__matrix)

    def modify_matrix(self, ri_to, ri_from, ci):
        nrows = len(self.__max_row_sums)
        mutable = [
            [self.__matrix[r][c] for c in range(self.__ncols)]
            for r in range(nrows)]
        mutable[ri_from][ci] -= 1
        mutable[ri_to][ci] += 1
        return tuplize_matrix(mutable)

    def neighbors(self):
        nrows = len(self.__max_row_sums)
        for ri in range(nrows):
            if sum(self.__matrix[ri]) < self.__max_row_sums[ri]:
                adjacent_rows = []
                if ri > 0:
                    adjacent_rows.append(ri - 1)
                if ri < nrows - 1:
                    adjacent_rows.append(ri + 1)
                for adj_ri in adjacent_rows:
                    for ci in range(self.__ncols):
                        if self.__matrix[adj_ri][ci] > 0:
                            yield WDState(self.__max_row_sums,
                                          self.__ncols,
                                          self.modify_matrix(ri, adj_ri, ci))


wd3x3_s0 = WDState( (3,3,3),
                     3,
                   ((2,0,0),
                    (0,3,0),
                    (0,0,3)) )

wd4x4_s0 = WDState( (4,4,4,4),
                     4,
                   ((3,0,0,0),
                    (0,4,0,0),
                    (0,0,4,0),
                    (0,0,0,4)) )

wd5x5_s0 = WDState( (5,5,5,5,5),
                     5,
                   ((4,0,0,0,0),
                    (0,5,0,0,0),
                    (0,0,5,0,0),
                    (0,0,0,5,0),
                    (0,0,0,0,5)) )

# max. distance & the number of antipodes for 3x3 and 4x4:
# http://cubezzz.dyndns.org/drupal/?q=node/view/238/2528#comment-2528
# full distribution for 5x5:
# http://cubezzz.dyndns.org/drupal/?q=node/view/238/2496#comment-2496

import bfs

print('# WD 3x3')
bfs.bfs( [ wd3x3_s0 ], lambda st: st.neighbors() )

print('# WD 4x4')
bfs.bfs( [ wd4x4_s0 ], lambda st: st.neighbors() )

print('# WD 5x5')
bfs.bfs( [ wd5x5_s0 ], lambda st: st.neighbors() )
