from collections import deque
l = [
        (0, '6'),
        (0, '4'),
        (0, '2'),
        (0, '1'),
        (2, 0),
        (3, 5),
        (3, 4),
        (4, 5),
        (4, 6),
        (4, 3)
    ]

def graph(l):
    _graph = dict()
    for k, v in l:
        _graph[k] = _graph.get(k, [])
        _graph[k].append(v)
    return _graph

print(graph(l))