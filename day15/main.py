# Parse input
lines = open("day15/input").read().strip().split("\n")
width = len(lines[0])
height = len(lines)

grid = [int(n) for line in lines for n in line]

# Set up dijkstra variables
dist = [float("inf") for _ in range(height * width)]
dist[0] = 0
prev = [None for _ in range(height * width)]
Q = set([i for i in range(height * width)])


def neighbours(i):
    x = i % width
    y = i // width

    result = []
    if x - 1 >= 0: result.append(y * width + x - 1)
    if x + 1 < width: result.append(y * width + x + 1)
    if y - 1 >= 0: result.append((y - 1) * width + x)
    if y + 1 < height: result.append((y + 1) * width + x)
    return result

# Calculate shortest path
while len(Q) > 0:
    u = min(Q, key=lambda v: dist[v])
    Q.remove(u)

    if u == len(grid) - 1:
        break

    for v in neighbours(u):
        if v in Q:
            alt = dist[u] + grid[v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

print(dist[len(grid) - 1])