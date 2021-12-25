from typing import Counter

[template, rules] = open("day14/input").read().strip().split("\n\n")
rules = dict([rule.split(" -> ") for rule in rules.split("\n")])

pairs = Counter([a + b for (a, b) in zip(list(template), list(template)[1:])])
chars = Counter(template)

for _ in range(40):
    for [pair, count] in pairs.most_common():
        if pair in rules:
            pairs[pair] -= count
            pairs[pair[0] + rules[pair]] += count
            pairs[rules[pair] + pair[1]] += count
            chars[rules[pair]] += count

print(chars.most_common()[0][1] - chars.most_common()[-1][1])