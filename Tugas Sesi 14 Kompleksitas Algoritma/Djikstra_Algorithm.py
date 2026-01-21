import heapq

def dijkstra(graph, start, goal):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == goal:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Rekonstruksi jalur
    path = []
    node = goal
    while node:
        path.append(node)
        node = previous.get(node)
    path.reverse()

    return distances[goal], path


# Graph Dijkstra
graph_dijkstra = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5, 'E': 10},
    'C': {'A': 2, 'D': 8, 'F': 4},
    'D': {'B': 5, 'C': 8},
    'E': {'B': 10, 'G': 6},
    'F': {'C': 4, 'G': 1},
    'G': {'F': 1, 'E': 6}
}

distance, path = dijkstra(graph_dijkstra, 'A', 'G')
print("Dijkstra")
print("Jalur Terpendek:", " -> ".join(path))
print("Total Jarak:", distance)
