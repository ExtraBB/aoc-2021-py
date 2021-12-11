lines = open("day10/input").read().strip().split("\n")

char_map = { ')': '(', ']': '[', '}': '{', '>': '<'}

def check_line(line):
    lastOpen = []
    for char in line:
        if char in char_map.values():
            lastOpen.append(char)
        elif char in char_map.keys():
            if lastOpen[len(lastOpen) - 1] != char_map[char]:
                return char
            lastOpen.pop()
    return lastOpen

def char_value(char, part):
    if char in ['(', ')']:
        return 3 if part == 1 else 1
    if char in ['[', ']']:
        return 57 if part == 1 else 2
    if char in ['{', '}']:
        return 1197 if part == 1 else 3
    if char in ['<', '>']:
        return 25137 if part == 1 else 4
    return 0

def calculate_incomplete_scores():
    scores = []
    for stack in [result for result in map(check_line, lines) if isinstance(result, list)]:
        score = 0
        for c in reversed(stack):
            score *= 5
            score += char_value(c, 2)
        scores.append(score)
    return scores

corrupt_line_scores = [char_value(check_line(line), 1) for line in lines]
incomplete_line_scores = sorted(calculate_incomplete_scores()) 

print(sum(corrupt_line_scores))
print(incomplete_line_scores[len(incomplete_line_scores) // 2])