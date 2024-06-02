import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist, parent):
        print("Vertex\tShortest Path Cost\tPath")
        for node in range(self.V):
            print(node, "\t", dist[node], "\t\t\t", end="")
            self.print_path(parent, node)
            print()

    def print_path(self, parent, j):
        if parent[j] == -1:
            print(j, end="")
            return
        self.print_path(parent, parent[j])
        print(" ->", j, end="")

    def min_distance(self, dist, spt_set):
        min_dist = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if dist[v] < min_dist and not spt_set[v]:
                min_dist = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        parent = [-1] * self.V
        dist[src] = 0
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt_set[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u

        self.print_solution(dist, parent)

    def add_edge(self, u, v, cost):
        self.graph[u][v] = cost
        self.graph[v][u] = cost

# Main function
if __name__ == "__main__":
    num_nodes = int(input("Enter the number of nodes (up to 10): "))
    if num_nodes > 10 or num_nodes < 2:
        print("Number of nodes should be between 2 and 10")
        sys.exit()

    g = Graph(num_nodes)

    print("Enter the link costs:")
    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            cost = int(input(f"Enter cost between node {i} and node {j}: "))
            g.add_edge(i, j, cost)

    source_node = int(input("Enter the source node: "))

    g.dijkstra(source_node)
