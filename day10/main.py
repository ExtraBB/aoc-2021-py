lines = open("day10/input").read().strip().split("\n")

char_map = { ')': '(', ']': '[', '}': '{', '>': '<'}

def check_line(line):
    lastOpen = []
    for char in line:
        if char in char_map.values():
            lastOpen.append(char)
        elif char in char_map.keys():
            if len(lastOpen) == 0:
                return char
            if lastOpen[len(lastOpen) - 1] != char_map[char]:
                return char
            lastOpen.pop()
    return ''

def char_value(char):
    if char in ['(', ')']:
        return 3
    if char in ['[', ']']:
        return 57
    if char in ['{', '}']:
        return 1197
    if char in ['<', '>']:
        return 25137
    return 0

print(sum([char_value(check_line(line)) for line in lines ]))