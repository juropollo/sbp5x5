# Partially confirm http://cubezzz.dyndns.org/drupal/?q=node/view/238/2521#comment-2521

def bfs_log_hr(symbol):
    print(symbol * 36)

def bfs_log(depth, states, cumulative):
    print('%6s%15s%15s' % (str(depth), str(states), str(cumulative)))

def bfs(layer0, expand_func):
    prev_set = set()
    curr_set = set(layer0)
    cumulative = 0
    depth = 0
    bfs_log_hr('=')
    bfs_log('depth', 'states', 'cumulative')
    bfs_log_hr('-')
    while len(curr_set) > 0:
        states = len(curr_set)
        cumulative += states
        bfs_log(depth, states, cumulative)
        depth += 1
        next_set = set(next_st
                       for curr_st in curr_set
                       for next_st in expand_func(curr_st)
                       if (next_st not in prev_set) and
                          (next_st not in curr_set))
        prev_set = curr_set
        curr_set = next_set
    bfs_log_hr('=')

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
    bfs([ tuple(range(rows * cols)) ], expand)

run(3, 3, 'the 3x3 puzzle')
run(5, 2, 'the 5x2 puzzle')
run(5, 5, 'the 5x5 puzzle')
