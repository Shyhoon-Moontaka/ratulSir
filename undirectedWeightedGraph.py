def create_graph():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    
    for i in range(num_vertices):
        vertex = input("Enter the vertex: ")
        connections = input("Enter the vertices connected to {}: ".format(vertex)).split()
        edges = []
        for connection in connections:
            neighbor, weight = connection.split(",")
            edges.append((vertex, neighbor, int(weight)))
        graph[vertex] = edges
    return graph

graph = create_graph()
print("Graph:", graph)
