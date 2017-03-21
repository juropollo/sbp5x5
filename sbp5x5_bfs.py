# Partially confirm http://cubezzz.dyndns.org/drupal/?q=node/view/238/2521#comment-2521

import bfs

def run(rows, cols, comment):

    def adj_func(u, v):
        dx = u % cols - v % cols
        dy = u // cols - v // cols
        taxicab = abs(dx) + abs(dy)
        return 1 == taxicab

    adj = tuple(
        tuple(adj_func(u, v) for u in range(rows * cols))
        for v in range(rows * cols))

    def expand(st):
        st = list(st)
        empty = st.index(0)
        for v in range(rows * cols):
            if adj[empty][v]:
                st[empty], st[v] = st[v], 0
                yield tuple(st)
                st[v], st[empty] = st[empty], 0

    print('# %s' % (comment))
    bfs.bfs([ tuple(range(rows * cols)) ], expand)

# run(3, 3, 'the 3x3 puzzle')
# run(5, 2, 'the 5x2 puzzle')
run(5, 5, 'the 5x5 puzzle')
