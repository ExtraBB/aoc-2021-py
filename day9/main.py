from math import prod

lines = [[int(n) for n in line] for line in open("day9/input").read().strip().split("\n")]
all_directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def valid_coordinates(x, y):
    return y >= 0 and y < len(lines) and x >= 0 and x < len(lines[y])

def valid_neighbours(x, y):
    return [(x + dx, y + dy) for (dx, dy) in all_directions if valid_coordinates(x + dx, y + dy)]

def is_low_point(x, y):
    return all([lines[y2][x2] > lines[y][x] for (x2, y2) in valid_neighbours(x, y)])

def find_low_points():
    points = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if is_low_point(x, y):
                points.append((x, y))
    return points

def find_basins():
    return [follow_basin(set(), x, y) for (x,y) in find_low_points()]

def follow_basin(basin, x, y):  
    basin.add((x, y))
    for (x2, y2) in valid_neighbours(x, y):
        if lines[y2][x2] != 9 and (x2, y2) not in basin:
            follow_basin(basin, x2, y2)
    return basin

print(sum([lines[y][x] + 1 for (x,y) in find_low_points()]))
print(prod(sorted([len(basin) for basin in find_basins()], reverse=True)[:3]))