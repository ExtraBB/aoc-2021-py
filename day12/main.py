lines = open("day12/input").read().strip().split("\n")

paths = {}
for line in lines:
    [a, b] = line.split('-')
    if not a in paths:
        paths[a] = set()
    if not b in paths:
        paths[b] = set()
    paths[a].add(b)
    paths[b].add(a) 

def solve(node, seen=set(), can_visit_twice=True):
    if node == "end":
        return 1
    
    if node in seen:
        if node == "start": return 0
        if node.islower():
            if not can_visit_twice:
                return 0
            else:
                can_visit_twice = False
    
    return sum(solve(loc, seen|{node}, can_visit_twice) for loc in paths[node])

print(str(solve("start", can_visit_twice=False)))
print(str(solve("start", can_visit_twice=True)))