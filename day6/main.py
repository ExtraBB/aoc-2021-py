from collections import Counter

nums = [int(i) for i in open("day6/input").read().strip().split(",")]

def simulate_fish(days):
    counter = Counter(nums)
    for _ in range(days):
        newFish = counter[0]
        for i in range(8):
            counter[i] = counter[(i + 1) % 9]
        counter[6] += newFish
        counter[8] = newFish
    return sum(counter.values())

print(simulate_fish(80))
print(simulate_fish(256))