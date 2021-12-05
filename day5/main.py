lines = open("day5/input").read().strip().split("\n")
coords = [line.split(' -> ') for line in lines]

def pointsBetween(c1, c2):
    direction = 1 if c2 >= c1 else -1
    return list(range(c1, c2 + direction, direction))

def points(x1, y1, x2, y2):
    pointsBetweenX = pointsBetween(x1, x2)
    pointsBetweenY = pointsBetween(y1, y2)
    maxLen = max(len(pointsBetweenX), len(pointsBetweenY))
    return [(x * 1000) + y for (x,y) in zip(pad(pointsBetweenX, maxLen), pad(pointsBetweenY, maxLen))]

def pad(xs, n):
    return xs + [xs[0]] * (n - len(xs))

def countOverlaps(skipDiagonal):
    seen = {}
    for [c1, c2] in coords:
        [x1, y1] = [int(c) for c in c1.split(',')]
        [x2, y2] = [int(c) for c in c2.split(',')]
        if skipDiagonal and x1 != x2 and y1 != y2:
            continue
        for p in points(x1, y1, x2, y2):
            seen[p] = seen[p] + 1 if p in seen else 1
    
    return len([key for key in seen if seen[key] > 1])

print(countOverlaps(True))
print(countOverlaps(False))    