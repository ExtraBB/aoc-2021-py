from collections import defaultdict
from math import inf as INFINITY
import heapq

# Parse input
lines = open("day15/input").read().strip().split("\n")
width = len(lines[0])
height = len(lines)

grid = [int(n) for line in lines for n in line]

def neighbours(i):
    x = i % width
    y = i // width

    if x - 1 >= 0: yield y * width + x - 1
    if x + 1 < width: yield y * width + x + 1
    if y - 1 >= 0: yield (y - 1) * width + x
    if y + 1 < height: yield (y + 1) * width + x

# Calculate shortest path
def dijkstra(distances, source, target):
    dist = defaultdict(lambda: INFINITY, {source: 0})
    Q = [(0, source)]
    visited = set()

    while Q:
        u_dist, u = heapq.heappop(Q)

        if u == target:
            return u_dist

        if u in visited:
            continue
        
        visited.add(u)

        for v in neighbours(u):
            if v not in visited:
                alt = u_dist + distances[v]
                if alt < dist[v]:
                    dist[v] = alt
                    heapq.heappush(Q, (alt, v))
    
    return INFINITY


print(dijkstra(grid, 0, len(grid) - 1))

rows = [[int(n) for n in line] for line in lines]

for _ in range(4):
    for row in rows:
        tail = row[-width:]
        row.extend((int(x) + 1) if int(x) < 9 else 1 for x in tail)
    
for _ in range(4):
	for row in rows[-height:]:
		rows.append([(x + 1) if x < 9 else 1 for x in row])

grid = [item for row in rows for item in row]
width *= 5
height *= 5

print(dijkstra(grid, 0, len(grid) - 1))