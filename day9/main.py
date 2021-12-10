from math import prod

lines = [[int(n) for n in line] for line in open("day9/input").read().strip().split("\n")]
all_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def valid_coordinates(x, y):
    return y >= 0 and y < len(lines) and x >= 0 and x < len(lines[y])

def valid_neighbours(x, y, directions):
    return [(x + dx, y + dy) for (dx, dy) in directions if valid_coordinates(x + dx, y + dy)]

def is_low_point(x, y, directions):
    return all([lines[y2][x2] > lines[y][x] for (x2, y2) in valid_neighbours(x, y, directions)])

def find_low_points():
    points = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if is_low_point(x, y, all_directions):
                points.append((x, y))
    return points

def filter_directions(x, y, basin):
    filtered = []

    for (dx, dy) in all_directions:
        if not valid_coordinates(x + dx, y + dy):
            continue
        if (x + dx, y + dy) in basin:
            continue
        if lines[y + dy][x + dx] == 9:
            continue
        filtered.append((dx, dy))
    
    return filtered

def find_basins():
    basins = []
    for (x, y) in find_low_points():
        basin = set()
        extend_basin(basin, x, y)
        basins.append(basin)
    return basins

def extend_basin(basin, x, y):  
    basin.add((x, y))
    directions = filter_directions(x, y, basin)
    for (dx, dy) in directions:
        extend_basin(basin, x + dx, y + dy)


print(sum([lines[y][x] + 1 for (x,y) in find_low_points()]))
print(prod(sorted([len(basin) for basin in find_basins()], reverse=True)[:3]))