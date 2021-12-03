import itertools

input = [int(i) for i in open("day1/input").read().strip().split("\n")]

def part1(nums):
    return len([pair for pair in itertools.pairwise(nums) if pair[1] > pair[0]])

def part2(nums):
    return part1(map(sum, zip(nums, nums[1:], nums[2:])))

print("Part 1: " + str(part1(input)))
print("Part 2: " + str(part2(input)))