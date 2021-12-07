nums = [int(i) for i in open("day7/input").read().strip().split(",")]

def calculate_fuel1(nums, goal):
    return sum([abs(i - goal) for i in nums])

def calculate_fuel2(nums, goal):
    return sum([sum(range(abs(i - goal) + 1)) for i in nums])

def binary_search(goals, minIndex, maxIndex, func):
    if maxIndex - minIndex < 2:
        return min(func(nums, goals[minIndex]), func(nums, goals[maxIndex]))
    else:
        mid = minIndex + (maxIndex - minIndex) // 2
        goal1 = func(nums, goals[mid])
        goal2 = func(nums, goals[mid - 1])
        return binary_search(goals, minIndex, mid, func) if goal1 > goal2 else binary_search(goals, mid, maxIndex, func)

start = min(nums)
end = max(nums) + 1
goals = range(start, max(nums) + 1)
print(binary_search(goals, start, end, calculate_fuel1))
print(binary_search(goals, start, end, calculate_fuel2))
