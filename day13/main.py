[positions, instructions] = open("day13/input").read().strip().split("\n\n")

coords = []
for position in positions.split("\n"):
    [x, y] = position.split(",")
    coords.append((int(x), int(y)))

grid = [[False for _ in range(max(x for (x,_) in coords) + 1)] for _ in range(max(y for (_, y) in coords) + 1)] 
for (x, y) in coords:
    grid[y][x] = True

def print_grid():
    print("\n\n")
    for line in grid:
        print("".join(["#" if pos else "." for pos in line]))

print_grid()

def fold(instruction):
    [dir, coord] = instruction[len("fold along "):].split("=")
    fold_line = int(coord)
    if dir == "y":
        for y in range(1, len(grid) - fold_line):
            if fold_line - y >= 0:
                for x in range(len(grid[0])):
                    grid[fold_line - y][x] |= grid[fold_line + y][x]
                    grid[fold_line + y][x] = False
    if dir == "x":
        for y in range(len(grid)):
            for x in range(1, len(grid[0]) - fold_line):
                if fold_line - x >= 0:
                    grid[y][fold_line - x] |= grid[y][fold_line + x]
                    grid[y][fold_line + x] = False


# Part1
fold(instructions.split("\n")[0])
print(sum(sum(line) for line in grid))

# Part2
for instruction in instructions.split("\n")[1:]:
    fold(instruction)
print_grid()