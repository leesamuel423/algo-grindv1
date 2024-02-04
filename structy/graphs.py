from collections import deque

# Graphs DFS and BFS #
# Iterative DFS Implementation
"""

def depth_first_print(graph, start):
    stack = [start]
    while stack:
        current = stack.pop()
        print(current)
        for neighbor in graph[current]:
            stack.append(neighbor)


"""


# Recursive DFS Implementation
def depth_first_print(graph, current):
    print(current)
    for neighbor in graph[current]:
        depth_first_print(graph, neighbor)


# Iterative BFS Implementation
def breadth_first_print(graph, start):
    queue = deque([start])
    while queue:
        current = queue.popleft()
        print(current)
        for neighbor in graph[current]:
            queue.append(neighbor)


graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

breadth_first_print(graph, "a")


# ----------> HAS PATH <----------
def has_path(graph, src, dst):
    """
    Will be using dfs -> utilize an iterative approach -> stack
    follow down stack and if dst exists return True
    return False at end
    """
    stack = [src]
    while stack:
        current = stack.pop()
        if current == dst:
            return True
        for neighbor in graph[current]:
            stack.append(neighbor)

    return False


# ----------> UNDIRECTED PATH <----------
def undirected_path(edges, node_A, node_B):
    """
    convert edge list to adjacency list
    """
    graph = build_graph(edges)
    return check(graph, node_A, node_B, set())


def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    print("this is graph", graph)
    return graph


def check(graph, current, target, set):
    if current == target:
        return True
    if current in set:
        return False
    set.add(current)
    for neighbor in graph[current]:
        if check(graph, neighbor, target, set):
            return True
    return False


edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

undirected_path(edges, "j", "m")


# ---------> CONNECTED COMPONENTS COUNT <--------
"""

def connected_components_count(graph):
    seen = set()
    count = 0
    for node in graph:
        if node in seen:
            continue
        count += dfs_traversal(graph, node, seen)
    return count


def dfs_traversal(graph, value, seen):
    stack = [value]
    while stack:
        current = stack.pop()
        seen.add(current)
        for neighbor in graph[current]:
            if neighbor not in seen:
                stack.append(neighbor)
    return 1
"""


def connected_components_count(graph):
    visited = set()
    count = 0

    for node in graph:
        if explore(graph, node, visited):
            count += 1
    return count


def explore(graph, current, visited):
    if current in visited:
        return False
    visited.add(current)
    for neighbor in graph[current]:
        explore(graph, neighbor, visited)
    return True


# ----------> LARGEST COMPONENT <----------
def largest_component(graph):
    max_count = 0
    visited = set()

    for node in graph:
        count = dfs_traverse(graph, node, visited)
        print("this is count", count)
        if count:
            max_count = max(max_count, count)

    return max_count


def dfs_traverse(graph, current, visited):
    if current in visited:
        return 0
    visited.add(current)
    size = 1
    for neighbor in graph[current]:
        size += dfs_traverse(graph, neighbor, visited)
    return size


# ----------> SHORTEST PATH <----------
def shortest_path(edges, node_A, node_B):
    """
    bfs would make the most sense here instead of dfs
    """
    visited = set()
    graph = create_graph(edges)  # gives us adjacency list
    return bfs_shortest_path(graph, node_A, node_B, visited)


def create_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph


def bfs_shortest_path(graph, start, target, visited):
    queue = deque([(start, 0)])

    while queue:
        a, b = queue.popleft()
        if a == target:
            return b
        visited.add(a)

        for neighbor in graph[a]:
            if neighbor not in visited:
                queue.append((neighbor, b + 1))

    return -1


# ------------> ISLAND COUNT <------------
"""
Think of each position as (x, y)
DFS each time you hit land and explore all land from there
"""


def island_count(grid):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            count += explore_land(grid, row, column, visited)
    return count


def explore_land(grid, row, column, visited):
    row_boundary = 0 <= row < len(grid)
    column_boundary = 0 <= column < len(grid[0])

    if (
        not row_boundary
        or not column_boundary
        or grid[row][column] == "W"
        or (row, column) in visited
    ):
        return 0

    visited.add((row, column))

    visited.add((row, column))
    explore_land(grid, row - 1, column, visited)
    explore_land(grid, row + 1, column, visited)
    explore_land(grid, row, column - 1, visited)
    explore_land(grid, row, column + 1, visited)

    return 1


# ------------> MINIMUM ISLAND <------------
def minimum_island(grid):
    visited = set()
    count = float("inf")
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            size = dora(grid, r, c, visited)
            if size:
                count = min(count, size)

    return count


def dora(grid, r, c, visited):
    row_range = 0 <= r < len(grid)
    column_range = 0 <= c < len(grid[0])
    if not row_range or not column_range or (r, c) in visited or grid[r][c] == "W":
        return 0

    visited.add((r, c))

    land_count = 1
    land_count += dora(grid, r - 1, c, visited)
    land_count += dora(grid, r + 1, c, visited)
    land_count += dora(grid, r, c - 1, visited)
    land_count += dora(grid, r, c + 1, visited)

    return land_count


# ------------> CLOSEST CARROT <------------
def closest_carrot(grid, starting_row, starting_col):
    """
    utilize bfs in order to get to carrot
    """
    visited = set()
    queue = deque([starting_row, starting_col])
    count = 0

    while queue:
        r, c = deque.popleft()
        if grid[r][c] == "C":
            return count


# def bfs_shortest_path(graph, start, target, visited):
#     queue = deque([(start, 0)])
#
#     while queue:
#         a, b = queue.popleft()
#         if a == target:
#             return b
#         visited.add(a)
#
#         for neighbor in graph[a]:
#             if neighbor not in visited:
#                 queue.append((neighbor, b + 1))
#
#     return -1
#
