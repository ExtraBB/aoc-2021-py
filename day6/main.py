from collections import Counter

nums = [int(i) for i in open("day6/input").read().strip().split(",")]

def simulate_fish(days):
    counter = Counter(nums)
    for _ in range(days):
        copy = counter.copy()
        for i in range(9):
            copy[i] = counter[(i + 1) % 9]
        copy[6] += counter[0]
        counter = copy
    return sum(counter.values())

print(simulate_fish(80))
print(simulate_fish(256))