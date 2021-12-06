from collections import Counter

nums = [int(i) for i in open("day6/input").read().strip().split(",")]

def simulate_fish(days):
    counter = Counter(nums)
    for i in range(days):
        copy = counter.copy()
        copy[8] = counter[0]
        copy[7] = counter[8]
        copy[6] = counter[0] + counter[7]
        copy[5] = counter[6]
        copy[4] = counter[5]
        copy[3] = counter[4]
        copy[2] = counter[3]
        copy[1] = counter[2]
        copy[0] = counter[1]
        counter = copy
    return sum(counter.values())

print(simulate_fish(80))
print(simulate_fish(256))