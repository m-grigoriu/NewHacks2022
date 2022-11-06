def pathfinder(start: int, dist: float, graph: list[list[int]]) -> list[int]:
    """Docstring"""
    half = dist / 2
    visited = set()
    visited.add(start)

    return find_path(start, half, visited, graph)[1]

def find_path(start: int, dist: float, visited: set[int], graph: list[list[int]]) -> list:
    """Docstring"""
    path = [start]
    v = visited.copy()

    best_so_far = []
    best_length = 0

    for adj in range(len(graph[start])):
        if adj in v:
            continue

        l = graph[start][adj]

        if l >= 9999:
            continue

        if abs(dist - l) > abs(dist - best_length):
            continue
        elif dist == l:
            path.append(adj)
            return (True, path)

        v.add(adj)
        res = find_path(adj, dist - l, v, graph)
        if res[0]:
            path = path + res[1]
            return (True, path)
        else:
            d = 0
            curr = start
            for step in res[1]:
                d += graph[curr][step]
                curr = step

            if abs(d - dist) < abs(best_length - dist):
                best_length = d
                best_so_far = res[1]

    path = path + best_so_far

    print(path)
    return (False, path)