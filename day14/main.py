from typing import Counter

[template, rules] = open("day14/input").read().strip().split("\n\n")
rules = {a : b for [a, b] in [rule.split(" -> ") for rule in rules.split("\n")]}

def run_steps(input, n):
    pairs = Counter([a + b for (a, b) in zip(list(input), list(input)[1:])])
    for _ in range(n):
        for [pair, count] in pairs.most_common():
            if pair in rules:
                pairs[pair] -= count
                pairs[pair[0] + rules[pair]] += count
                pairs[rules[pair] + pair[1]] += count
    return pairs

pairs = run_steps(template, 40)
counter = Counter()
for pair in pairs.most_common():
    counter[pair[0][0]] += pair[1] / 2
    counter[pair[0][1]] += pair[1] / 2

print(counter.most_common()[0][1] - counter.most_common()[-1][1])