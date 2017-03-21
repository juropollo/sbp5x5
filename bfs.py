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
