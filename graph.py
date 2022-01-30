class Graph:
    def __init__(self, edges) -> None:
        # self.edges = edges
        self.graph_dict = {}

        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print(self.graph_dict)

    def get_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            new_path = self.get_path(node, end, path)
            for p in new_path:
                paths.append(p)

        return paths

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    g = Graph(routes)

    start = "Mumbai"
    end = "New York"

    print(f"All paths between: {start} and {end}: ",g.get_path(start,end))
    # print(f"Shortest path between {start} and {end}: ", route_graph.get_shortest_path(start,end))