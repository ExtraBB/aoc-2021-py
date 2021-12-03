import pathlib
import itertools

nums = list(map(int, open(str(pathlib.Path(__file__).parent.resolve()) + "/input")))

def part1(nums):
    return len([pair for pair in itertools.pairwise(nums) if pair[1] > pair[0]])

def part2(nums):
    return part1(map(sum, zip(nums, nums[1:], nums[2:])))

print("Part 1: " + str(part1(nums)))
print("Part 2: " + str(part2(nums)))