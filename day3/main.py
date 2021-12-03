import pathlib

input = list(map(lambda line: line.strip(), open(str(pathlib.Path(__file__).parent.resolve()) + "/input")))

bit_length = len(input[0])

def mostCommonAt(lines, n):
    return "1" if sum([int(line[n]) for line in lines]) >= len(lines) // 2 else "0"

def mostCommon(lines):
    return ''.join([mostCommonAt(lines, i) for i in range(bit_length)])

def flip(bin):
    return ''.join(["0" if x == "1" else "1" for x in bin])

def part1(lines):
    gamma = mostCommon(lines)
    return int(gamma, 2) * int(flip(gamma), 2)

def part2(lines):
    mostCommon = lines
    leastCommon = lines
    for i in range(bit_length):
        mostCommonBit = mostCommonAt(mostCommon, i)
        leastCommonBit = flip(mostCommonAt(leastCommon, i))
        mostCommon = [line for line in mostCommon if line[i] == mostCommonBit] if len(mostCommon) > 1 else mostCommon
        leastCommon = [line for line in leastCommon if line[i] == leastCommonBit] if len(leastCommon) > 1 else leastCommon
    return int(mostCommon[0], 2) * int(leastCommon[0], 2)


print(part1(input))
print(part2(input))