"""
This is the Bellman-Ford algorithm, which creates 
random edges with varying weights and vertices. It proceeds 
to display the randomly generated graph, request the source node, 
and then reveals the shortest path from the source node to all other nodes.
"""
#----------------------------------------------------------------------------------------------------------------------
#CODE

import random

INF = float("inf")

# Function to perform the Bellman-Ford algorithm
def bellman_ford(graph, num_vertices, source):
    distance = [INF] * num_vertices
    distance[source] = 0

    for _ in range(num_vertices - 1):
        for u in range(num_vertices):
            for v in range(num_vertices):
                if graph[u][v] != INF and distance[u] != INF and distance[u] + graph[u][v] < distance[v]:
                    distance[v] = distance[u] + graph[u][v]

    # Check for negative weight cycles
    for u in range(num_vertices):
        for v in range(num_vertices):
            if graph[u][v] != INF and distance[u] != INF and distance[u] + graph[u][v] < distance[v]:
                print("Graph contains a negative weight cycle!")
                return

    # Print the shortest distances from the source to all other vertices
    print(f"Shortest distances from vertex {source} to all other vertices:")
    for i in range(num_vertices):
        print(f"Vertex {i}: {distance[i]}")

if __name__ == "__main__":
    random.seed()  # Seed for random number generation

    num_vertices = int(input("Enter the number of vertices: "))

    graph = [[INF] * num_vertices for _ in range(num_vertices)]
    num_edges = 0

    # Generate random edges
    print("Randomly generated edges:")
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j:
                weight = random.randint(0, 99)  # Random edge weight between 0 and 99
                graph[i][j] = weight
                if weight != INF:
                    num_edges += 1
                    print(f"Edge {i} -> {j} with weight {weight}")

    source = int(input("Enter the source vertex: "))

    bellman_ford(graph, num_vertices, source)
