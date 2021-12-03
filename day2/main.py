input = open("day2/input").read().strip().split("\n")

class State:
    def __init__(self, depth, pos, aim):
        self.depth, self.pos, self.aim = depth, pos, aim

actions1 = {
    "forward":  lambda state, n: State(state.depth, state.pos + n, state.aim),
    "up":       lambda state, n: State(state.depth - n, state.pos, state.aim),
    "down":     lambda state, n: State(state.depth + n, state.pos, state.aim)
}

actions2 = {
    "forward":  lambda state, n: State(state.depth + state.aim * n, state.pos + n, state.aim),
    "up":       lambda state, n: State(state.depth, state.pos, state.aim - n),
    "down":     lambda state, n: State(state.depth, state.pos, state.aim + n)
}

def runMoves(lines, actions):
    state = State(0,0,0)
    for line in lines:
        command, n = line.split(' ')
        state = actions[command](state, int(n))
    return state.depth * state.pos

print(runMoves(input, actions1))
print(runMoves(input, actions2))