from collections import deque, defaultdict
# import networkx as nx

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
# We create some sample search problems to check our algorithms
#this class will create a 2D grid of row x colums and its graph.
#Some of the cells can be disabled by putting it into walls
#for example SearchGrid(3,4,walls=[0,10]) will create a grid that has cell 0 and 10 are disabled.

class SearchGrid :
    def __init__(self, rows=5, columns=5, walls=[], diagonal=False ) : #walls -> [ list of index ]
        self.rows = rows
        self.columns = columns
        self.N = rows * columns #total cells
        self.walls = walls
        self.diagonal = diagonal #falg to check if can move diagonally
        
    def edges(self) : 
        """return edges of the graph in a list of tuples (u,v)"""
        edges = []

        #Just a convenient funtion
        def _add_edge(u, v) :
            #we add the edge if source and destinations are not walls
            #and within the grid
            if v % self.columns == 0 : #check if at the edge.
                return
            if u not in self.walls and v not in self.walls and u < self.N and v < self.N :
                edges.append( (u,v) )
        
        #first the forward links to the right
        for i in range(self.N) :
            #if (i+1) % self.columns != 0 :#checking if it is an edge cell
            _add_edge(i, i+1)            #connect to next cell
            _add_edge(i,i+self.columns)  #connect to the cell below; it is i+width
            if self.diagonal : #add diagonal edges as well
                _add_edge(i,i+self.columns+1)  #connect to the cell below + 1
                #_add_edge(i,i+self.columns-1)  #connect to the cell below + 1
                
        return edges
    
    #pretty print the grid and path if given. path -> [ list of nodes ]
    def print(self, path=[]) :
        for i in range(self.N) :
            if i in self.walls :
                print('# ', end='')
            elif i in path :
                print('^ ', end='')
            else :
                print('. ', end='')
            if (i+1) % self.columns == 0 :
                print("")
#build a graph
def graph(l):
    _graph = defaultdict(deque)
    for k, v in l:
        _graph[k] = _graph.get(k, [])
        _graph[v] = _graph.get(v, [])
        _graph[k].append(v)
        _graph[v].append(k)

    return _graph


def connected(start, end, _graph):
    _connected = False
    _stack = [start]
    _visited = []
    while len(_stack):
        _start = _stack.pop(0)
        if _start not in _visited:
            _visited.append(_start)
            if end == _start:
                return True
        # print(_visited)
        node_value = _graph.get(_start)

        if node_value:
            for i in node_value:
                if not (i in _visited):
                    _stack.append(i)
        print(_stack)
            # print(f'this is the node_values :  {node_value}')
            # _stack += [i for i in node_value if not (i in _visited)]
            # print(f'this is the _stack : {_stack}')
    return _connected


if __name__ == "__main__":
    _searchGrid = SearchGrid(20,20,walls=[2,5,8,9,20])
    # _searchGrid.print()
    # G = nx.Graph()
    # G.add_edges_from(_searchGrid.edges())
    # print(G)
    # print(connected(2,8,graph(l)))
    print(connected(0,20, graph(_searchGrid.edges())))
    # print(f'The values you\'ve provided are not not connect because they are : {isConnect}')
