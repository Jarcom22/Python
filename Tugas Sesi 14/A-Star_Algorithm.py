import heapq

def astar(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    closed_list = set()

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        closed_list.add(current)

        for neighbor, cost in graph[current].items():
            tentative_g = g_score[current] + cost

            if neighbor in closed_list and tentative_g >= g_score[neighbor]:
                continue

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    # Rekonstruksi jalur
    path = []
    node = goal
    while node:
        path.append(node)
        node = came_from.get(node)
    path.reverse()

    return g_score[goal], path


# GRAPH SESUAI SOAL
graph = {
    'A': {'C': 2},
    'B': {'C': 4, 'D': 5, 'E': 10},
    'C': {'A': 2, 'B': 4, 'D': 4, 'F': 4},
    'D': {'B': 5, 'C': 4},
    'E': {'B': 10, 'G': 6},
    'F': {'C': 4, 'G': 1},
    'G': {'F': 1, 'E': 6}
}

heuristic = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 5,
    'E': 3,
    'F': 1,
    'G': 0
}

distance, path = astar(graph, heuristic, 'A', 'G')

print("A-Star")
print("Jalur Terpendek:", " -> ".join(path))
print("Total Jarak:", distance)
