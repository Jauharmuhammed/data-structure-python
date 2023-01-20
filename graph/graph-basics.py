class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dict = {}
        for start, end in edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start] = [end]

    
    def get_paths(self, start, end , path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.dict:
            return []

        paths = []
        for node in self.dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end , path)
                for p in new_paths:
                    paths.append(p)
        
        return paths

if __name__ == '__main__':
    routes = [
        ('Kozhikode', 'Dubai'),
        ('Kozhikode', 'Delhi'),
        ('Kozhikode', 'Banglore'),
        ('Banglore', 'Dubai'),
        ('Dubai', 'London'),
        ('Dubai', 'Paris'),
        ('Dubai', 'Instanbul'),
        ('Instanbul', 'London'),
        ('Paris', 'London'),
    ]

    graph = Graph(routes)
    start = 'Kozhikode'
    end = 'London'
    print(f'Path between {start} and {end}: ', )
    for i in graph.get_paths(start, end):
        print(i)



