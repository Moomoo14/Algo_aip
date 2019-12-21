from collections import deque, defaultdict

# l = [
#     (0, 6),
#     (0, 4),
#     (0, 2),
#     (0, 1),
#     (2, 0),
#     (3, 5),
#     (3, 4),
#     (3, 6),
#     (4, 5),
#     (4, 6),
#     (4, 3)
# ]

l = [
    (2, 1),
    (2, 4),
    (2, 6),
    (2, 7),
    (2, 3),
    (3, 4),
    (3, 5),
    (8, 9),
    (4, 5),
]


def graph(l):
    _graph = defaultdict(deque)
    for k, v in l:
        _graph[k] = _graph.get(k, [])
        _graph[v] = _graph.get(v, [])
        _graph[k].append(v)
        _graph[v].append(k)

    return _graph


def connected(start, end, _graph):
    current_graph = _graph
    print(current_graph)
    _connected = False
    _stack = [start]
    _visited = []
    current_item = 0
    while len(_stack):
        node_value = current_graph.get(_stack[current_item])
        if _stack[current_item] not in _visited:
            _visited.append(_stack[current_item])
            if end in _visited:
                _connected = True
                return _connected
        # print(f'this is the current stack{_stack}')
        _stack.remove(_stack[current_item])
        # print(f'this is the current visited list :{_visited}')
        if node_value:
            _stack += [i for i in node_value if i not in _visited]

    return _connected


print(connected(2, 6, graph(l)))
