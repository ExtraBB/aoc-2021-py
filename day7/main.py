nums = [int(i) for i in open("day7/input").read().strip().split(",")]

def calculate_fuel1(nums, goal):
    return sum([abs(i - goal) for i in nums])

def calculate_fuel2(nums, goal):
    return sum([sum(range(abs(i - goal) + 1)) for i in nums])

print(min([calculate_fuel1(nums, i) for i in range(min(nums), max(nums) + 1)]))
print(min([calculate_fuel2(nums, i) for i in range(min(nums), max(nums) + 1)]))

