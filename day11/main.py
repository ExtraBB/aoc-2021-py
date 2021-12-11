lines = open("day11/input").read().strip().split("\n")
grid = [[int(c) for c in line] for line in lines]
grid_size = len(grid)

all_directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]

def valid_coordinates(x, y):
    return y >= 0 and y < len(lines) and x >= 0 and x < len(lines[y])

def valid_neighbours(x, y):
    return [(x + dx, y + dy) for (dx, dy) in all_directions if valid_coordinates(x + dx, y + dy)]

def print_grid(step):
    print("=== After step: " + str(step) + " ===")
    for row in grid:
        print("".join([str(i) for i in row]))

def try_flash(x, y, already_flashed):
    if grid[y][x] > 9 and (x, y) not in already_flashed:
        already_flashed.add((x, y))
        neighbours = valid_neighbours(x, y)
        for (x2, y2) in neighbours:
            if (x2, y2) not in already_flashed:
                grid[y2][x2] += 1
                already_flashed |= try_flash(x2, y2, already_flashed)

    return already_flashed

def step():
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1

    flashed = set()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            flashed |= try_flash(x, y, flashed)

    for (x, y) in flashed:
        grid[y][x] = 0

    return len(flashed)

def run_steps(n):
    count = last_flashes = i = 0
    while last_flashes != grid_size**2:
        i += 1
        last_flashes = step()
        count += last_flashes
        if i == n:
            print("Total flashes after " + str(n) + " steps: " + str(count))
    print("First simultaneous flash: " + str(i))

run_steps(100)